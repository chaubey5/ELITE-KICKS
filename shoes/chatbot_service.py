import openai
from decouple import config
from django.db.models import Q, Avg, Count
from django.db import models

from .models import (
    Shoe, Brand, Category, Order,
    Review, ChatSession, ChatMessage
)

# Set OpenAI API key (correct way)
openai.api_key = config("OPENAI_API_KEY", default="")


class ChatbotService:

    def __init__(self):
        pass

    # ------------------------------------------------------------------
    # CONTEXT DATA
    # ------------------------------------------------------------------
    def get_context_data(self, request):
        price_data = Shoe.objects.filter(is_available=True).aggregate(
            min_price=models.Min("price"),
            max_price=models.Max("price")
        )

        popular_brands = Brand.objects.annotate(
            shoe_count=Count("shoes", filter=Q(shoes__is_available=True))
        ).filter(shoe_count__gt=0).order_by("-shoe_count")[:8]

        popular_categories = Category.objects.annotate(
            shoe_count=Count("shoes", filter=Q(shoes__is_available=True))
        ).filter(shoe_count__gt=0)

        popular_shoes = Shoe.objects.filter(is_available=True).annotate(
            avg_rating=Avg("reviews__rating"),
            review_count=Count("reviews")
        ).order_by("-avg_rating", "-review_count")[:5]

        context = {
            "total_shoes": Shoe.objects.filter(is_available=True).count(),
            "brands": [{"name": b.name, "count": b.shoe_count} for b in popular_brands],
            "categories": [{"name": c.name, "count": c.shoe_count} for c in popular_categories],
            "price_range": {
                "min": float(price_data["min_price"] or 29.99),
                "max": float(price_data["max_price"] or 299.99),
            },
            "popular_shoes": [
                {
                    "name": s.name,
                    "brand": s.brand.name,
                    "price": float(s.current_price),
                    "rating": round(s.avg_rating or 0, 1),
                    "review_count": s.review_count,
                }
                for s in popular_shoes
            ],
            "user_authenticated": request.user.is_authenticated,
            "username": request.user.username if request.user.is_authenticated else None,
        }

        if request.user.is_authenticated:
            context["user_orders"] = Order.objects.filter(user=request.user).count()
            recent_orders = Order.objects.filter(user=request.user).order_by("-created_at")[:3]
            context["recent_purchases"] = [
                {
                    "order_number": o.order_number,
                    "total": float(o.total_amount),
                    "status": o.status,
                }
                for o in recent_orders
            ]

        return context

    # ------------------------------------------------------------------
    # SEARCH SHOES
    # ------------------------------------------------------------------
    def search_shoes(self, query, limit=5):
        words = query.lower().split()
        search_q = Q()

        for w in words:
            search_q |= (
                Q(name__icontains=w)
                | Q(brand__name__icontains=w)
                | Q(category__name__icontains=w)
                | Q(description__icontains=w)
            )

        shoes = (
            Shoe.objects.filter(search_q, is_available=True)
            .annotate(avg_rating=Avg("reviews__rating"), review_count=Count("reviews"))
            .distinct()
            .order_by("-avg_rating", "-review_count", "price")[:limit]
        )

        return [
            {
                "id": s.id,
                "name": s.name,
                "brand": s.brand.name,
                "category": s.category.name,
                "price": float(s.current_price),
                "rating": round(s.avg_rating or 0, 1),
                "review_count": s.review_count,
                "stock": s.stock_quantity,
            }
            for s in shoes
        ]

    # ------------------------------------------------------------------
    # AI RESPONSE (NO HISTORY)
    # ------------------------------------------------------------------
    def get_ai_response(self, user_message, context, request):
        if not openai.api_key:
            return self.get_fallback_response(user_message, request)

        brand_list = ", ".join(
            [f"{b['name']} ({b['count']})" for b in context["brands"][:5]]
        )

        category_list = ", ".join(
            [f"{c['name']} ({c['count']})" for c in context["categories"][:6]]
        )

        popular_text = "\n".join(
            [
                f"• {s['brand']} {s['name']} - ${s['price']} ⭐{s['rating']}"
                for s in context["popular_shoes"][:3]
            ]
        )

        recent_purchases = context.get("recent_purchases", [])
        recent_text = ""
        if recent_purchases:
            recent_text = "- Recent purchases: " + ", ".join(
                ["#{} (${})".format(p["order_number"], p["total"]) for p in recent_purchases]
            )

        system_prompt = f"""
You are a helpful shoe store assistant.

STORE INFO:
- Total shoes: {context['total_shoes']}
- Brands: {brand_list}
- Categories: {category_list}
- Price range: ${context['price_range']['min']} - ${context['price_range']['max']}

POPULAR:
{popular_text}

USER:
- Logged in: {context['user_authenticated']}
{recent_text}

Keep replies short, friendly, and helpful.
"""

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ],
            max_tokens=250,
            temperature=0.7,
        )

        return {
            "text": response["choices"][0]["message"]["content"].strip(),
            "suggestions": self.generate_suggestions(user_message, context),
            "source": "ai",
        }

    # ------------------------------------------------------------------
    # SUGGESTIONS
    # ------------------------------------------------------------------
    def generate_suggestions(self, user_message, context):
        msg = user_message.lower()

        if "running" in msg:
            return ["Running shoes", "Size guide", "Best sellers", "Offers"]

        if "formal" in msg:
            return ["Formal shoes", "Office wear", "Leather styles", "Size guide"]

        if "cheap" in msg or "budget" in msg:
            return ["Under $50", "Best value", "Discounts", "Sale"]

        return ["Popular shoes", "Browse brands", "Size guide", "New arrivals"]

    # ------------------------------------------------------------------
    # FALLBACK
    # ------------------------------------------------------------------
    def get_fallback_response(self, user_message, request):
        return {
            "text": "I can help you find the perfect shoes! Try asking about running, casual, or formal styles 👟",
            "suggestions": ["Running shoes", "Casual shoes", "Formal shoes", "Size guide"],
            "source": "fallback",
        }

    # ------------------------------------------------------------------
    # CHAT SESSION
    # ------------------------------------------------------------------
    def get_or_create_session(self, request):
        if request.user.is_authenticated:
            session, _ = ChatSession.objects.get_or_create(
                user=request.user, is_active=True
            )
        else:
            if not request.session.session_key:
                request.session.create()
            session, _ = ChatSession.objects.get_or_create(
                session_key=request.session.session_key,
                is_active=True,
            )
        return session

    def save_message(self, session, message_type, content, metadata=None):
        return ChatMessage.objects.create(
            session=session,
            message_type=message_type,
            content=content,
            metadata=metadata or {},
        )
