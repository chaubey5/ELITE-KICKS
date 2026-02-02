-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: localhost    Database: shoe_db
-- ------------------------------------------------------
-- Server version	8.0.45

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=89 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add brand',7,'add_brand'),(26,'Can change brand',7,'change_brand'),(27,'Can delete brand',7,'delete_brand'),(28,'Can view brand',7,'view_brand'),(29,'Can add category',8,'add_category'),(30,'Can change category',8,'change_category'),(31,'Can delete category',8,'delete_category'),(32,'Can view category',8,'view_category'),(33,'Can add color',9,'add_color'),(34,'Can change color',9,'change_color'),(35,'Can delete color',9,'delete_color'),(36,'Can view color',9,'view_color'),(37,'Can add shoe image',10,'add_shoeimage'),(38,'Can change shoe image',10,'change_shoeimage'),(39,'Can delete shoe image',10,'delete_shoeimage'),(40,'Can view shoe image',10,'view_shoeimage'),(41,'Can add size',11,'add_size'),(42,'Can change size',11,'change_size'),(43,'Can delete size',11,'delete_size'),(44,'Can view size',11,'view_size'),(45,'Can add shoe',12,'add_shoe'),(46,'Can change shoe',12,'change_shoe'),(47,'Can delete shoe',12,'delete_shoe'),(48,'Can view shoe',12,'view_shoe'),(49,'Can add shoe color',13,'add_shoecolor'),(50,'Can change shoe color',13,'change_shoecolor'),(51,'Can delete shoe color',13,'delete_shoecolor'),(52,'Can view shoe color',13,'view_shoecolor'),(53,'Can add shoe size',14,'add_shoesize'),(54,'Can change shoe size',14,'change_shoesize'),(55,'Can delete shoe size',14,'delete_shoesize'),(56,'Can view shoe size',14,'view_shoesize'),(57,'Can add review',15,'add_review'),(58,'Can change review',15,'change_review'),(59,'Can delete review',15,'delete_review'),(60,'Can view review',15,'view_review'),(61,'Can add wishlist',16,'add_wishlist'),(62,'Can change wishlist',16,'change_wishlist'),(63,'Can delete wishlist',16,'delete_wishlist'),(64,'Can view wishlist',16,'view_wishlist'),(65,'Can add cart',17,'add_cart'),(66,'Can change cart',17,'change_cart'),(67,'Can delete cart',17,'delete_cart'),(68,'Can view cart',17,'view_cart'),(69,'Can add cart item',18,'add_cartitem'),(70,'Can change cart item',18,'change_cartitem'),(71,'Can delete cart item',18,'delete_cartitem'),(72,'Can view cart item',18,'view_cartitem'),(73,'Can add order',19,'add_order'),(74,'Can change order',19,'change_order'),(75,'Can delete order',19,'delete_order'),(76,'Can view order',19,'view_order'),(77,'Can add order item',20,'add_orderitem'),(78,'Can change order item',20,'change_orderitem'),(79,'Can delete order item',20,'delete_orderitem'),(80,'Can view order item',20,'view_orderitem'),(81,'Can add chat session',21,'add_chatsession'),(82,'Can change chat session',21,'change_chatsession'),(83,'Can delete chat session',21,'delete_chatsession'),(84,'Can view chat session',21,'view_chatsession'),(85,'Can add chat message',22,'add_chatmessage'),(86,'Can change chat message',22,'change_chatmessage'),(87,'Can delete chat message',22,'delete_chatmessage'),(88,'Can view chat message',22,'view_chatmessage');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$870000$3QO0Sc2ephMcIAWh9kwujP$bMcVlSnEKxPK9urrQZwhvlFG1y92dcDdqEUtOkzdrnI=','2026-02-02 06:33:16.933814',1,'root','','','root@gmail.com',1,1,'2026-02-01 17:21:38.324171'),(2,'pbkdf2_sha256$870000$ctQ7UDG49GkP14zQochrfj$XY/Q5OI4t/zIDwpb25JKPLGpsDW0TgsHDddcZUmnA/A=',NULL,1,'root1','','','root@gmail.com',1,1,'2026-02-01 21:02:41.046211');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2026-02-01 21:08:22.350851','1','Adidas',1,'[{\"added\": {}}]',7,1),(2,'2026-02-01 21:10:05.602692','1','Men',1,'[{\"added\": {}}]',8,1),(3,'2026-02-01 21:10:45.251190','1','Adidas Adidas ultraboost',1,'[{\"added\": {}}]',12,1),(4,'2026-02-01 21:57:50.412573','7','7',1,'[{\"added\": {}}]',11,1),(5,'2026-02-01 21:57:54.720816','8','8',1,'[{\"added\": {}}]',11,1),(6,'2026-02-01 21:57:58.733955','9','9',1,'[{\"added\": {}}]',11,1),(7,'2026-02-01 21:58:02.422572','10','10',1,'[{\"added\": {}}]',11,1),(8,'2026-02-01 21:58:05.660351','11','11',1,'[{\"added\": {}}]',11,1),(9,'2026-02-02 06:47:54.189178','7','6',1,'[{\"added\": {}}]',19,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(7,'shoes','brand'),(17,'shoes','cart'),(18,'shoes','cartitem'),(8,'shoes','category'),(22,'shoes','chatmessage'),(21,'shoes','chatsession'),(9,'shoes','color'),(19,'shoes','order'),(20,'shoes','orderitem'),(15,'shoes','review'),(12,'shoes','shoe'),(13,'shoes','shoecolor'),(10,'shoes','shoeimage'),(14,'shoes','shoesize'),(11,'shoes','size'),(16,'shoes','wishlist');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2026-02-01 15:53:59.269643'),(2,'auth','0001_initial','2026-02-01 15:53:59.464981'),(3,'admin','0001_initial','2026-02-01 15:53:59.512044'),(4,'admin','0002_logentry_remove_auto_add','2026-02-01 15:53:59.512044'),(5,'admin','0003_logentry_add_action_flag_choices','2026-02-01 15:53:59.531489'),(6,'contenttypes','0002_remove_content_type_name','2026-02-01 15:53:59.573789'),(7,'auth','0002_alter_permission_name_max_length','2026-02-01 15:53:59.607021'),(8,'auth','0003_alter_user_email_max_length','2026-02-01 15:53:59.656683'),(9,'auth','0004_alter_user_username_opts','2026-02-01 15:53:59.674724'),(10,'auth','0005_alter_user_last_login_null','2026-02-01 15:53:59.715443'),(11,'auth','0006_require_contenttypes_0002','2026-02-01 15:53:59.731105'),(12,'auth','0007_alter_validators_add_error_messages','2026-02-01 15:53:59.747213'),(13,'auth','0008_alter_user_username_max_length','2026-02-01 15:53:59.787254'),(14,'auth','0009_alter_user_last_name_max_length','2026-02-01 15:53:59.809372'),(15,'auth','0010_alter_group_name_max_length','2026-02-01 15:53:59.825354'),(16,'auth','0011_update_proxy_permissions','2026-02-01 15:53:59.825354'),(17,'auth','0012_alter_user_first_name_max_length','2026-02-01 15:53:59.857093'),(18,'sessions','0001_initial','2026-02-01 15:53:59.883346'),(19,'shoes','0001_initial','2026-02-01 15:54:00.184417'),(20,'shoes','0002_cart_cartitem','2026-02-01 15:54:00.329984'),(21,'shoes','0003_alter_cartitem_unique_together_and_more','2026-02-01 15:54:00.606749'),(22,'shoes','0004_auto_20250824_1322','2026-02-01 15:54:00.606749'),(23,'shoes','0005_chatsession_chatmessage','2026-02-01 15:54:00.673191'),(24,'shoes','0006_alter_cartitem_color_alter_cartitem_size_and_more','2026-02-01 17:18:21.645944');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('r49ku4sny440gy115rycuy8kkvgcvf1j','.eJxVjDsOwjAQRO_iGln-rO1ASZ8zWOvdDQ4gR8qnQtwdIqWAbjTvzbxUxm2teVtkziOri7Lq9NsVpIe0HfAd223SNLV1HoveFX3QRfcTy_N6uH8HFZe6r4FiKeWcDIHhwQ3BIqFHT-GbBSJYCZENd0mYPHlvQzJAIuA6B1a9PwHROBo:1vmnUq:HYts-cIO9lLDgn_HBSFZQDqO9N92UIRQlgQH7GbQSaQ','2026-02-16 06:33:16.940351');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shoes_brand`
--

DROP TABLE IF EXISTS `shoes_brand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shoes_brand` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `logo` varchar(100) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shoes_brand`
--

LOCK TABLES `shoes_brand` WRITE;
/*!40000 ALTER TABLE `shoes_brand` DISABLE KEYS */;
INSERT INTO `shoes_brand` VALUES (1,'Adidas','What is the company description of adidas?\r\nAdidas AG is an international corporation that manufactures athletic footwear, clothing, accessories, and equipment. Headquartered in the Bavarian town of Herzogenaurach, Germany, Adidas is one of the world\'s leading shoe and sportswear manufacturers.','brands/adidas_ultraboost_22.jpg','2026-02-01 21:08:22.350851'),(2,'Hoka','','','2026-02-01 21:32:43.118983'),(3,'Nike','','','2026-02-01 21:32:43.153515'),(4,'Reebok','','','2026-02-01 21:32:43.190483'),(5,'Vans','','','2026-02-01 21:32:43.220694'),(6,'Jordan','','','2026-02-01 21:32:43.252173'),(7,'New Balance','','','2026-02-01 21:32:43.287110'),(8,'Puma','','','2026-02-01 21:32:43.319831'),(9,'Saucony','','','2026-02-01 21:32:43.363355');
/*!40000 ALTER TABLE `shoes_brand` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shoes_cart`
--

DROP TABLE IF EXISTS `shoes_cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shoes_cart` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `session_key` varchar(40) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `shoes_cart_user_id_a6b6d0b3_fk_auth_user_id` (`user_id`),
  CONSTRAINT `shoes_cart_user_id_a6b6d0b3_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shoes_cart`
--

LOCK TABLES `shoes_cart` WRITE;
/*!40000 ALTER TABLE `shoes_cart` DISABLE KEYS */;
INSERT INTO `shoes_cart` VALUES (1,'ru2ge9h2fpv2n64pzz9zbivevibw8u02','2026-02-01 16:08:00.740674','2026-02-01 16:08:00.748160',NULL),(2,NULL,'2026-02-01 17:22:12.396660','2026-02-01 17:22:12.396660',1),(3,'nqta9jxuxywko4axum10c3ef9fynjbjl','2026-02-01 22:48:02.761919','2026-02-01 22:48:02.761919',NULL);
/*!40000 ALTER TABLE `shoes_cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shoes_cartitem`
--

DROP TABLE IF EXISTS `shoes_cartitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shoes_cartitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int unsigned NOT NULL,
  `added_at` datetime(6) NOT NULL,
  `cart_id` bigint NOT NULL,
  `color_id` bigint DEFAULT NULL,
  `shoe_id` bigint NOT NULL,
  `size_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `shoes_cartitem_color_id_cf66cb64_fk_shoes_color_id` (`color_id`),
  KEY `shoes_cartitem_shoe_id_0b10ae00_fk_shoes_shoe_id` (`shoe_id`),
  KEY `shoes_cartitem_size_id_9c0f306a_fk_shoes_size_id` (`size_id`),
  KEY `shoes_cartitem_cart_id_4d4d3771` (`cart_id`),
  CONSTRAINT `shoes_cartitem_cart_id_4d4d3771_fk_shoes_cart_id` FOREIGN KEY (`cart_id`) REFERENCES `shoes_cart` (`id`),
  CONSTRAINT `shoes_cartitem_color_id_cf66cb64_fk_shoes_color_id` FOREIGN KEY (`color_id`) REFERENCES `shoes_color` (`id`),
  CONSTRAINT `shoes_cartitem_shoe_id_0b10ae00_fk_shoes_shoe_id` FOREIGN KEY (`shoe_id`) REFERENCES `shoes_shoe` (`id`),
  CONSTRAINT `shoes_cartitem_size_id_9c0f306a_fk_shoes_size_id` FOREIGN KEY (`size_id`) REFERENCES `shoes_size` (`id`),
  CONSTRAINT `shoes_cartitem_chk_1` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shoes_cartitem`
--

LOCK TABLES `shoes_cartitem` WRITE;
/*!40000 ALTER TABLE `shoes_cartitem` DISABLE KEYS */;
INSERT INTO `shoes_cartitem` VALUES (9,1,'2026-02-01 22:48:02.769562',3,NULL,2,NULL);
/*!40000 ALTER TABLE `shoes_cartitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shoes_category`
--

DROP TABLE IF EXISTS `shoes_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shoes_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shoes_category`
--

LOCK TABLES `shoes_category` WRITE;
/*!40000 ALTER TABLE `shoes_category` DISABLE KEYS */;
INSERT INTO `shoes_category` VALUES (1,'Men','Running shoes',''),(2,'Running','',''),(3,'Sports','',''),(4,'Casual','','');
/*!40000 ALTER TABLE `shoes_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shoes_chatmessage`
--

DROP TABLE IF EXISTS `shoes_chatmessage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shoes_chatmessage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message_type` varchar(10) NOT NULL,
  `content` longtext NOT NULL,
  `metadata` json NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `session_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `shoes_chatmessage_session_id_455d45c9_fk_shoes_chatsession_id` (`session_id`),
  CONSTRAINT `shoes_chatmessage_session_id_455d45c9_fk_shoes_chatsession_id` FOREIGN KEY (`session_id`) REFERENCES `shoes_chatsession` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shoes_chatmessage`
--

LOCK TABLES `shoes_chatmessage` WRITE;
/*!40000 ALTER TABLE `shoes_chatmessage` DISABLE KEYS */;
/*!40000 ALTER TABLE `shoes_chatmessage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shoes_chatsession`
--

DROP TABLE IF EXISTS `shoes_chatsession`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shoes_chatsession` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `session_key` varchar(40) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `shoes_chatsession_user_id_ed18406f_fk_auth_user_id` (`user_id`),
  CONSTRAINT `shoes_chatsession_user_id_ed18406f_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shoes_chatsession`
--

LOCK TABLES `shoes_chatsession` WRITE;
/*!40000 ALTER TABLE `shoes_chatsession` DISABLE KEYS */;
/*!40000 ALTER TABLE `shoes_chatsession` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shoes_color`
--

DROP TABLE IF EXISTS `shoes_color`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shoes_color` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `hex_code` varchar(7) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shoes_color`
--

LOCK TABLES `shoes_color` WRITE;
/*!40000 ALTER TABLE `shoes_color` DISABLE KEYS */;
INSERT INTO `shoes_color` VALUES (1,'Red','#FF0000'),(2,'Blue','#0000FF'),(3,'Black','#000000'),(4,'White','#FFFFFF');
/*!40000 ALTER TABLE `shoes_color` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shoes_order`
--

DROP TABLE IF EXISTS `shoes_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shoes_order` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `order_number` varchar(20) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `address` longtext NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `zip_code` varchar(10) NOT NULL,
  `country` varchar(50) NOT NULL,
  `payment_method` varchar(20) NOT NULL,
  `payment_status` varchar(20) NOT NULL,
  `subtotal` decimal(10,2) NOT NULL,
  `shipping_cost` decimal(10,2) NOT NULL,
  `tax` decimal(10,2) NOT NULL,
  `total_amount` decimal(10,2) NOT NULL,
  `status` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `order_number` (`order_number`),
  KEY `shoes_order_user_id_b8fd0ddf_fk_auth_user_id` (`user_id`),
  CONSTRAINT `shoes_order_user_id_b8fd0ddf_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shoes_order`
--

LOCK TABLES `shoes_order` WRITE;
/*!40000 ALTER TABLE `shoes_order` DISABLE KEYS */;
INSERT INTO `shoes_order` VALUES (1,'P4YO9E0T','RISHABH','CHAUBEY','root@gmail.com','+916376338088','LPU','GORAKHPUR','Uttar Pradesh','273002','United States','card','pending',5.00,9.99,0.40,15.39,'pending','2026-02-01 22:37:29.085673','2026-02-01 22:37:29.085673',1),(2,'VWM6V4EA','RISHABH','CHAUBEY','root@gmail.com','+916376338088','LPU','GORAKHPUR','Uttar Pradesh','273002','United States','cod','pending',22999.00,0.00,1839.92,24838.92,'pending','2026-02-01 22:39:31.006209','2026-02-01 22:39:31.006209',1),(3,'XN2MLGPE','RISHABH','CHAUBEY','','','LPU','GORAKHPUR','Uttar Pradesh','273002','India','credit_card','pending',22720.00,0.00,0.00,22720.00,'pending','2026-02-01 23:45:06.850400','2026-02-01 23:45:06.850400',1),(4,'XANKYX40','RISHABH','CHAUBEY','','','LPU','GORAKHPUR','Uttar Pradesh','273002','India','cash_on_delivery','pending',12000.00,0.00,0.00,12000.00,'pending','2026-02-01 23:50:56.602212','2026-02-01 23:50:56.603207',1),(5,'84OMBSVK','RISHABH','CHAUBEY','','','LPU','GORAKHPUR','Uttar Pradesh','273002','India','cash_on_delivery','pending',4500.00,0.00,0.00,4500.00,'pending','2026-02-01 23:52:55.222945','2026-02-01 23:52:55.222945',1),(6,'MVS73N74','RISHABH','CHAUBEY','','','LPU','GORAKHPUR','Uttar Pradesh','273002','India','cash_on_delivery','pending',110.00,0.00,0.00,110.00,'pending','2026-02-02 04:49:19.321006','2026-02-02 04:49:19.321006',1),(7,'6','RISHABH','CHAUBEY','chaubeyrishabh00@gmail.com','06376338088','LPU','GORAKHPUR','Uttar Pradesh','273002','India','cod','Delivered',1125.00,90.00,5.00,1220.00,'delivered','2026-02-02 06:47:54.185164','2026-02-02 06:47:54.185164',1);
/*!40000 ALTER TABLE `shoes_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shoes_orderitem`
--

DROP TABLE IF EXISTS `shoes_orderitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shoes_orderitem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int unsigned NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `color_id` bigint DEFAULT NULL,
  `order_id` bigint NOT NULL,
  `shoe_id` bigint NOT NULL,
  `size_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `shoes_orderitem_color_id_8804a124_fk_shoes_color_id` (`color_id`),
  KEY `shoes_orderitem_order_id_bde22ae7_fk_shoes_order_id` (`order_id`),
  KEY `shoes_orderitem_shoe_id_d92c2f31_fk_shoes_shoe_id` (`shoe_id`),
  KEY `shoes_orderitem_size_id_ae075fcd_fk_shoes_size_id` (`size_id`),
  CONSTRAINT `shoes_orderitem_color_id_8804a124_fk_shoes_color_id` FOREIGN KEY (`color_id`) REFERENCES `shoes_color` (`id`),
  CONSTRAINT `shoes_orderitem_order_id_bde22ae7_fk_shoes_order_id` FOREIGN KEY (`order_id`) REFERENCES `shoes_order` (`id`),
  CONSTRAINT `shoes_orderitem_shoe_id_d92c2f31_fk_shoes_shoe_id` FOREIGN KEY (`shoe_id`) REFERENCES `shoes_shoe` (`id`),
  CONSTRAINT `shoes_orderitem_size_id_ae075fcd_fk_shoes_size_id` FOREIGN KEY (`size_id`) REFERENCES `shoes_size` (`id`),
  CONSTRAINT `shoes_orderitem_chk_1` CHECK ((`quantity` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shoes_orderitem`
--

LOCK TABLES `shoes_orderitem` WRITE;
/*!40000 ALTER TABLE `shoes_orderitem` DISABLE KEYS */;
INSERT INTO `shoes_orderitem` VALUES (1,1,5.00,NULL,1,1,NULL),(2,1,9999.00,NULL,2,2,NULL),(3,1,13000.00,NULL,2,7,NULL),(4,1,4500.00,NULL,3,5,NULL),(5,1,12000.00,NULL,3,2,NULL),(6,1,6000.00,NULL,3,8,NULL),(7,2,110.00,NULL,3,1,NULL),(8,1,12000.00,NULL,4,2,NULL),(9,1,4500.00,NULL,5,5,NULL),(10,1,110.00,NULL,6,1,NULL);
/*!40000 ALTER TABLE `shoes_orderitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shoes_review`
--

DROP TABLE IF EXISTS `shoes_review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shoes_review` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rating` int NOT NULL,
  `comment` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  `shoe_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `shoes_review_shoe_id_user_id_a9e45501_uniq` (`shoe_id`,`user_id`),
  KEY `shoes_review_user_id_fa30d4d3_fk_auth_user_id` (`user_id`),
  CONSTRAINT `shoes_review_shoe_id_d42bf6e1_fk_shoes_shoe_id` FOREIGN KEY (`shoe_id`) REFERENCES `shoes_shoe` (`id`),
  CONSTRAINT `shoes_review_user_id_fa30d4d3_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shoes_review`
--

LOCK TABLES `shoes_review` WRITE;
/*!40000 ALTER TABLE `shoes_review` DISABLE KEYS */;
INSERT INTO `shoes_review` VALUES (1,5,'Very comfortable and stylish!','2026-02-01 21:55:36.259654',1,9),(2,5,'Awesome sneakers, highly recommended!','2026-02-01 21:55:36.259654',1,8),(3,5,'Value for money.','2026-02-01 21:55:36.277497',1,7),(4,5,'Perfect fit, love the color.','2026-02-01 21:55:36.282738',1,6),(5,5,'Awesome sneakers, highly recommended!','2026-02-01 21:55:36.290020',1,5),(6,4,'Perfect fit, love the color.','2026-02-01 21:55:36.297384',1,4),(7,5,'Value for money.','2026-02-01 21:55:36.305196',1,3),(8,4,'Value for money.','2026-02-01 21:55:36.305196',1,2),(9,5,'Awesome sneakers, highly recommended!','2026-02-01 21:55:36.313675',1,1);
/*!40000 ALTER TABLE `shoes_review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shoes_shoe`
--

DROP TABLE IF EXISTS `shoes_shoe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shoes_shoe` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `discount_price` decimal(10,2) DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  `gender` varchar(1) NOT NULL,
  `is_available` tinyint(1) NOT NULL,
  `stock_quantity` int unsigned NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `brand_id` bigint NOT NULL,
  `category_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `shoes_shoe_brand_id_c96037c5_fk_shoes_brand_id` (`brand_id`),
  KEY `shoes_shoe_category_id_17243719_fk_shoes_category_id` (`category_id`),
  CONSTRAINT `shoes_shoe_brand_id_c96037c5_fk_shoes_brand_id` FOREIGN KEY (`brand_id`) REFERENCES `shoes_brand` (`id`),
  CONSTRAINT `shoes_shoe_category_id_17243719_fk_shoes_category_id` FOREIGN KEY (`category_id`) REFERENCES `shoes_category` (`id`),
  CONSTRAINT `shoes_shoe_chk_1` CHECK ((`stock_quantity` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shoes_shoe`
--

LOCK TABLES `shoes_shoe` WRITE;
/*!40000 ALTER TABLE `shoes_shoe` DISABLE KEYS */;
INSERT INTO `shoes_shoe` VALUES (1,'Adidas ultraboost','Adidas AG (German pronunciation: [ˈadiˌdas]; stylized in all lowercase since 1949) is a German multinational athletic apparel and footwear corporation headquartered in Herzogenaurach, Germany. It is the largest sportswear manufacturer in Europe, and the second largest in the world, after Nike.',110.00,5.00,'shoes/adidas_ultraboost_22_Tki7vG0.jpg','M',1,12,'2026-02-01 21:10:45.243125','2026-02-01 21:10:45.243125',1,1),(2,'Hoka Clifton 8','Comfortable running shoes',12000.00,9999.00,'shoes/hoka_clifton_8.jpg','M',1,50,'2026-02-01 21:32:43.123844','2026-02-01 21:51:23.035380',2,2),(3,'Nike Air Max 270','Stylish and comfortable',15000.00,13500.00,'shoes/nike_air_max_270.jpg','U',1,40,'2026-02-01 21:32:43.161565','2026-02-01 21:51:23.032535',3,3),(4,'Reebok Classic Leather','Everyday casual shoes',5000.00,NULL,'shoes/reebok_classic_leather.jpg','U',1,35,'2026-02-01 21:32:43.192495','2026-02-01 21:51:23.027558',4,4),(5,'Vans Old Skool','Classic skate shoes',4500.00,4000.00,'shoes/vans_old_skool.jpg','U',1,40,'2026-02-01 21:32:43.220694','2026-02-01 21:51:23.015708',5,4),(6,'Jordan Air 1 Retro High','Iconic basketball shoes',18000.00,16500.00,'shoes/jordan_air_1_retro_high.jpg','M',1,30,'2026-02-01 21:32:43.268194','2026-02-01 21:32:43.268194',6,3),(7,'New Balance 990v5','Premium running shoes',14000.00,13000.00,'shoes/new_balance_990v5.jpg','U',1,25,'2026-02-01 21:32:43.300614','2026-02-01 21:32:43.300614',7,2),(8,'Puma RS-X','Trendy lifestyle sneakers',6000.00,5500.00,'shoes/puma_rs-x.jpg','U',1,35,'2026-02-01 21:32:43.331464','2026-02-01 21:32:43.331464',8,4),(9,'Saucony Ride 15','Smooth running experience',9000.00,8500.00,'shoes/saucony_ride_15.jpg','U',1,20,'2026-02-01 21:32:43.363355','2026-02-01 21:32:43.363355',9,2);
/*!40000 ALTER TABLE `shoes_shoe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shoes_shoe_additional_images`
--

DROP TABLE IF EXISTS `shoes_shoe_additional_images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shoes_shoe_additional_images` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `shoe_id` bigint NOT NULL,
  `shoeimage_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `shoes_shoe_additional_images_shoe_id_shoeimage_id_03331732_uniq` (`shoe_id`,`shoeimage_id`),
  KEY `shoes_shoe_additiona_shoeimage_id_b606c348_fk_shoes_sho` (`shoeimage_id`),
  CONSTRAINT `shoes_shoe_additiona_shoeimage_id_b606c348_fk_shoes_sho` FOREIGN KEY (`shoeimage_id`) REFERENCES `shoes_shoeimage` (`id`),
  CONSTRAINT `shoes_shoe_additional_images_shoe_id_2d0c02b2_fk_shoes_shoe_id` FOREIGN KEY (`shoe_id`) REFERENCES `shoes_shoe` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shoes_shoe_additional_images`
--

LOCK TABLES `shoes_shoe_additional_images` WRITE;
/*!40000 ALTER TABLE `shoes_shoe_additional_images` DISABLE KEYS */;
/*!40000 ALTER TABLE `shoes_shoe_additional_images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shoes_shoecolor`
--

DROP TABLE IF EXISTS `shoes_shoecolor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shoes_shoecolor` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `color_id` bigint NOT NULL,
  `shoe_id` bigint NOT NULL,
  `stock` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `shoes_shoecolor_shoe_id_color_id_ab5bfeeb_uniq` (`shoe_id`,`color_id`),
  KEY `shoes_shoecolor_color_id_8938f0d4_fk_shoes_color_id` (`color_id`),
  CONSTRAINT `shoes_shoecolor_color_id_8938f0d4_fk_shoes_color_id` FOREIGN KEY (`color_id`) REFERENCES `shoes_color` (`id`),
  CONSTRAINT `shoes_shoecolor_shoe_id_e984b147_fk_shoes_shoe_id` FOREIGN KEY (`shoe_id`) REFERENCES `shoes_shoe` (`id`),
  CONSTRAINT `shoes_shoecolor_chk_1` CHECK ((`stock` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shoes_shoecolor`
--

LOCK TABLES `shoes_shoecolor` WRITE;
/*!40000 ALTER TABLE `shoes_shoecolor` DISABLE KEYS */;
INSERT INTO `shoes_shoecolor` VALUES (1,1,2,50),(2,3,2,50),(3,2,3,40),(4,3,3,40),(5,4,4,35),(6,3,4,35),(7,3,5,40),(8,4,5,40),(9,1,6,30),(10,3,6,30),(11,4,7,25),(12,3,7,25),(13,2,8,35),(14,3,8,35),(15,1,9,20),(16,4,9,20);
/*!40000 ALTER TABLE `shoes_shoecolor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shoes_shoeimage`
--

DROP TABLE IF EXISTS `shoes_shoeimage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shoes_shoeimage` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `alt_text` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shoes_shoeimage`
--

LOCK TABLES `shoes_shoeimage` WRITE;
/*!40000 ALTER TABLE `shoes_shoeimage` DISABLE KEYS */;
/*!40000 ALTER TABLE `shoes_shoeimage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shoes_shoesize`
--

DROP TABLE IF EXISTS `shoes_shoesize`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shoes_shoesize` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `stock` int unsigned NOT NULL,
  `shoe_id` bigint NOT NULL,
  `size_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `shoes_shoesize_shoe_id_size_id_86e8a700_uniq` (`shoe_id`,`size_id`),
  KEY `shoes_shoesize_size_id_5d8baa1d_fk_shoes_size_id` (`size_id`),
  CONSTRAINT `shoes_shoesize_shoe_id_864af43a_fk_shoes_shoe_id` FOREIGN KEY (`shoe_id`) REFERENCES `shoes_shoe` (`id`),
  CONSTRAINT `shoes_shoesize_size_id_5d8baa1d_fk_shoes_size_id` FOREIGN KEY (`size_id`) REFERENCES `shoes_size` (`id`),
  CONSTRAINT `shoes_shoesize_chk_1` CHECK ((`stock` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shoes_shoesize`
--

LOCK TABLES `shoes_shoesize` WRITE;
/*!40000 ALTER TABLE `shoes_shoesize` DISABLE KEYS */;
INSERT INTO `shoes_shoesize` VALUES (1,50,2,3),(2,50,2,4),(3,50,2,5),(4,40,3,2),(5,40,3,3),(6,40,3,4),(7,40,3,5),(8,35,4,1),(9,35,4,2),(10,35,4,3),(11,40,5,1),(12,40,5,2),(13,40,5,3),(14,40,5,4),(15,30,6,3),(16,30,6,4),(17,30,6,5),(18,25,7,2),(19,25,7,3),(20,25,7,4),(21,25,7,5),(22,35,8,1),(23,35,8,2),(24,35,8,3),(25,35,8,4),(26,35,8,5),(27,20,9,2),(28,20,9,3),(29,20,9,4);
/*!40000 ALTER TABLE `shoes_shoesize` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shoes_size`
--

DROP TABLE IF EXISTS `shoes_size`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shoes_size` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `size_value` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shoes_size`
--

LOCK TABLES `shoes_size` WRITE;
/*!40000 ALTER TABLE `shoes_size` DISABLE KEYS */;
INSERT INTO `shoes_size` VALUES (1,'6'),(2,'7'),(3,'8'),(4,'9'),(5,'10'),(6,'11'),(7,'7'),(8,'8'),(9,'9'),(10,'10'),(11,'11');
/*!40000 ALTER TABLE `shoes_size` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shoes_wishlist`
--

DROP TABLE IF EXISTS `shoes_wishlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shoes_wishlist` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `shoe_id` bigint NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `shoes_wishlist_user_id_shoe_id_29864c67_uniq` (`user_id`,`shoe_id`),
  KEY `shoes_wishlist_shoe_id_1cad18a3_fk_shoes_shoe_id` (`shoe_id`),
  CONSTRAINT `shoes_wishlist_shoe_id_1cad18a3_fk_shoes_shoe_id` FOREIGN KEY (`shoe_id`) REFERENCES `shoes_shoe` (`id`),
  CONSTRAINT `shoes_wishlist_user_id_c18ca571_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shoes_wishlist`
--

LOCK TABLES `shoes_wishlist` WRITE;
/*!40000 ALTER TABLE `shoes_wishlist` DISABLE KEYS */;
INSERT INTO `shoes_wishlist` VALUES (1,'2026-02-01 21:55:36.281587',7,1),(2,'2026-02-01 21:55:36.302036',4,1),(3,'2026-02-01 21:55:36.313675',1,1);
/*!40000 ALTER TABLE `shoes_wishlist` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-02-02 12:25:51
