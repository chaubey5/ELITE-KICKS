// // Main JavaScript for Shoe Store
// document.addEventListener('DOMContentLoaded', function() {
    
//     // Initialize tooltips
//     var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
//     var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
//         return new bootstrap.Tooltip(tooltipTriggerEl);
//     });

//     // Add loading states to forms
//     const forms = document.querySelectorAll('form');
//     forms.forEach(form => {
//         form.addEventListener('submit', function() {
//             const submitBtn = form.querySelector('button[type="submit"]');
//             if (submitBtn) {
//                 submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Processing...';
//                 submitBtn.disabled = true;
//                 submitBtn.classList.add('loading');
//             }
//         });
//     });

//     // Enhanced search functionality
//     const searchInput = document.querySelector('input[name="q"]');
//     if (searchInput) {
//         let searchTimeout;
//         searchInput.addEventListener('input', function() {
//             clearTimeout(searchTimeout);
//             searchTimeout = setTimeout(() => {
//                 if (this.value.length >= 2) {
//                     // Add search suggestions or live search here
//                     console.log('Searching for:', this.value);
//                 }
//             }, 300);
//         });
//     }

//     // Add to cart animation
//     const addToCartButtons = document.querySelectorAll('button[type="submit"][action*="add_to_cart"]');
//     addToCartButtons.forEach(button => {
//         button.addEventListener('click', function(e) {
//             // Add a small animation
//             this.style.transform = 'scale(0.95)';
//             setTimeout(() => {
//                 this.style.transform = 'scale(1)';
//             }, 150);
//         });
//     });

//     // Smooth scroll for anchor links (only for internal page anchors)
//     document.querySelectorAll('a[href^="#"]').forEach(anchor => {
//         anchor.addEventListener('click', function (e) {
//             e.preventDefault();
//             const target = document.querySelector(this.getAttribute('href'));
//             if (target) {
//                 target.scrollIntoView({
//                     behavior: 'smooth',
//                     block: 'start'
//                 });
//             }
//         });
//     });

//     // Lazy loading for images
//     if ('IntersectionObserver' in window) {
//         const imageObserver = new IntersectionObserver((entries, observer) => {
//             entries.forEach(entry => {
//                 if (entry.isIntersecting) {
//                     const img = entry.target;
//                     img.src = img.dataset.src;
//                     img.classList.remove('lazy');
//                     imageObserver.unobserve(img);
//                 }
//             });
//         });

//         document.querySelectorAll('img[data-src]').forEach(img => {
//             imageObserver.observe(img);
//         });
//     }

//     // Enhanced card hover effects
//     const cards = document.querySelectorAll('.shoe-card, .brand-card, .category-card');
//     cards.forEach(card => {
//         card.addEventListener('mouseenter', function() {
//             this.style.transform = 'translateY(-10px) scale(1.02)';
//         });
        
//         card.addEventListener('mouseleave', function() {
//             this.style.transform = 'translateY(0) scale(1)';
//         });
//     });

//     // Price formatting
//     const priceElements = document.querySelectorAll('.price, .discount-price');
//     priceElements.forEach(element => {
//         const price = parseFloat(element.textContent.replace('$', ''));
//         if (!isNaN(price)) {
//             element.textContent = '$' + price.toFixed(2);
//         }
//     });

//     // Add to wishlist functionality
//     const wishlistButtons = document.querySelectorAll('.wishlist-btn');
//     wishlistButtons.forEach(button => {
//         button.addEventListener('click', function(e) {
//             e.preventDefault();
//             const icon = this.querySelector('i');
//             if (icon.classList.contains('far')) {
//                 icon.classList.remove('far');
//                 icon.classList.add('fas', 'text-danger');
//                 this.classList.add('active');
//             } else {
//                 icon.classList.remove('fas', 'text-danger');
//                 icon.classList.add('far');
//                 this.classList.remove('active');
//             }
//         });
//     });

//     // Quantity selector enhancement
//     const quantityInputs = document.querySelectorAll('input[name="quantity"]');
//     quantityInputs.forEach(input => {
//         const container = input.parentElement;
//         const minusBtn = document.createElement('button');
//         const plusBtn = document.createElement('button');
        
//         minusBtn.innerHTML = '<i class="fas fa-minus"></i>';
//         plusBtn.innerHTML = '<i class="fas fa-plus"></i>';
//         minusBtn.className = 'btn btn-outline-secondary btn-sm';
//         plusBtn.className = 'btn btn-outline-secondary btn-sm';
        
//         minusBtn.addEventListener('click', function() {
//             const currentValue = parseInt(input.value) || 1;
//             if (currentValue > 1) {
//                 input.value = currentValue - 1;
//             }
//         });
        
//         plusBtn.addEventListener('click', function() {
//             const currentValue = parseInt(input.value) || 1;
//             input.value = currentValue + 1;
//         });
        
//         container.insertBefore(minusBtn, input);
//         container.appendChild(plusBtn);
//     });

//     // Filter enhancement
//     const filterForm = document.querySelector('.filters-section form');
//     if (filterForm) {
//         const filterInputs = filterForm.querySelectorAll('select, input');
//         filterInputs.forEach(input => {
//             input.addEventListener('change', function() {
//                 // Auto-submit form after a short delay
//                 clearTimeout(window.filterTimeout);
//                 window.filterTimeout = setTimeout(() => {
//                     filterForm.submit();
//                 }, 500);
//             });
//         });
//     }

//     // Mobile menu enhancement
//     const navbarToggler = document.querySelector('.navbar-toggler');
//     const navbarCollapse = document.querySelector('.navbar-collapse');
    
//     if (navbarToggler && navbarCollapse) {
//         navbarToggler.addEventListener('click', function() {
//             navbarCollapse.classList.toggle('show');
//         });
        
//         // Close mobile menu when clicking outside
//         document.addEventListener('click', function(e) {
//             if (!navbarToggler.contains(e.target) && !navbarCollapse.contains(e.target)) {
//                 navbarCollapse.classList.remove('show');
//             }
//         });
//     }

//     // Scroll progress indicator
//     const progressBar = document.createElement('div');
//     progressBar.className = 'scroll-progress';
//     progressBar.style.cssText = `
//         position: fixed;
//         top: 0;
//         left: 0;
//         width: 0%;
//         height: 3px;
//         background: linear-gradient(90deg, var(--primary-color), var(--accent-color));
//         z-index: 9999;
//         transition: width 0.1s ease;
//     `;
//     document.body.appendChild(progressBar);

//     window.addEventListener('scroll', function() {
//         const scrolled = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100;
//         progressBar.style.width = scrolled + '%';
//     });

//     // Add fade-in animation to elements
//     const observerOptions = {
//         threshold: 0.1,
//         rootMargin: '0px 0px -50px 0px'
//     };

//     const observer = new IntersectionObserver((entries) => {
//         entries.forEach(entry => {
//             if (entry.isIntersecting) {
//                 entry.target.classList.add('fade-in-up');
//                 observer.unobserve(entry.target);
//             }
//         });
//     }, observerOptions);

//     document.querySelectorAll('.card, .section-title, .hero-content').forEach(el => {
//         observer.observe(el);
//     });
// });

// // Utility functions
// function formatPrice(price) {
//     return new Intl.NumberFormat('en-US', {
//         style: 'currency',
//         currency: 'USD'
//     }).format(price);
// }

// function debounce(func, wait) {
//     let timeout;
//     return function executedFunction(...args) {
//         const later = () => {
//             clearTimeout(timeout);
//             func(...args);
//         };
//         clearTimeout(timeout);
//         timeout = setTimeout(later, wait);
//     };
// }

// // Export for use in other scripts
// window.ShoeStore = {
//     formatPrice,
//     debounce
// };
