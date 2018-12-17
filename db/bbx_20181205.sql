-- MySQL dump 10.13  Distrib 8.0.12, for macos10.13 (x86_64)
--
-- Host: localhost    Database: bbxsystem
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
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
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
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
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
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
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add 船舶基础信息',7,'add_bbxinfo'),(20,'Can change 船舶基础信息',7,'change_bbxinfo'),(21,'Can delete 船舶基础信息',7,'delete_bbxinfo'),(22,'Can add 船舶基础数据（空间信息）',8,'add_bbxspaceinfo'),(23,'Can change 船舶基础数据（空间信息）',8,'change_bbxspaceinfo'),(24,'Can delete 船舶基础数据（空间信息）',8,'delete_bbxspaceinfo'),(25,'Can add 船舶基础数据（临时表）',9,'add_bbxspacetempinfo'),(26,'Can change 船舶基础数据（临时表）',9,'change_bbxspacetempinfo'),(27,'Can delete 船舶基础数据（临时表）',9,'delete_bbxspacetempinfo'),(28,'Can add 水文要素历史表',10,'add_hydrologydata'),(29,'Can change 水文要素历史表',10,'change_hydrologydata'),(30,'Can delete 水文要素历史表',10,'delete_hydrologydata'),(31,'Can add 气象要素',11,'add_meteorologicaldata'),(32,'Can change 气象要素',11,'change_meteorologicaldata'),(33,'Can delete 气象要素',11,'delete_meteorologicaldata'),(34,'Can add 志愿船的水文气象要素（临时表）',12,'add_realtimedata'),(35,'Can change 志愿船的水文气象要素（临时表）',12,'change_realtimedata'),(36,'Can delete 志愿船的水文气象要素（临时表）',12,'delete_realtimedata');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
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
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
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
-- Table structure for table `bbx_bbxinfo`
--

DROP TABLE IF EXISTS `bbx_bbxinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `bbx_bbxinfo` (
  `bid` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) NOT NULL,
  `area` varchar(2) NOT NULL,
  `desc` varchar(200) NOT NULL,
  `shipton` double NOT NULL,
  `shiptype` varchar(2) NOT NULL,
  `sort` int(11) NOT NULL,
  PRIMARY KEY (`bid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bbx_bbxinfo`
--

LOCK TABLES `bbx_bbxinfo` WRITE;
/*!40000 ALTER TABLE `bbx_bbxinfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `bbx_bbxinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bbx_bbxspaceinfo`
--

DROP TABLE IF EXISTS `bbx_bbxspaceinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `bbx_bbxspaceinfo` (
  `bsid` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) NOT NULL,
  `nowdate` datetime(6) NOT NULL,
  `lat` double NOT NULL,
  `lon` double NOT NULL,
  `heading` double DEFAULT NULL,
  `speed` double DEFAULT NULL,
  `bid_id` int(11) NOT NULL,
  PRIMARY KEY (`bsid`),
  KEY `bbx_bbxspaceinfo_bid_id_c7b0b953_fk_bbx_bbxinfo_bid` (`bid_id`),
  CONSTRAINT `bbx_bbxspaceinfo_bid_id_c7b0b953_fk_bbx_bbxinfo_bid` FOREIGN KEY (`bid_id`) REFERENCES `bbx_bbxinfo` (`bid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bbx_bbxspaceinfo`
--

LOCK TABLES `bbx_bbxspaceinfo` WRITE;
/*!40000 ALTER TABLE `bbx_bbxspaceinfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `bbx_bbxspaceinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bbx_bbxspacetempinfo`
--

DROP TABLE IF EXISTS `bbx_bbxspacetempinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `bbx_bbxspacetempinfo` (
  `bsid` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) NOT NULL,
  `nowdate` datetime(6) NOT NULL,
  `lat` double NOT NULL,
  `lon` double NOT NULL,
  `heading` double DEFAULT NULL,
  `speed` double DEFAULT NULL,
  `bid_id` int(11) NOT NULL,
  PRIMARY KEY (`bsid`),
  KEY `bbx_bbxspacetempinfo_bid_id_50e7d73c_fk_bbx_bbxinfo_bid` (`bid_id`),
  CONSTRAINT `bbx_bbxspacetempinfo_bid_id_50e7d73c_fk_bbx_bbxinfo_bid` FOREIGN KEY (`bid_id`) REFERENCES `bbx_bbxinfo` (`bid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bbx_bbxspacetempinfo`
--

LOCK TABLES `bbx_bbxspacetempinfo` WRITE;
/*!40000 ALTER TABLE `bbx_bbxspacetempinfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `bbx_bbxspacetempinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bbx_hydrologydata`
--

DROP TABLE IF EXISTS `bbx_hydrologydata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `bbx_hydrologydata` (
  `hid` int(11) NOT NULL AUTO_INCREMENT,
  `wt` double DEFAULT NULL,
  `wvs` double DEFAULT NULL,
  `wv` double DEFAULT NULL,
  `surge1d` double DEFAULT NULL,
  `surge1c` double DEFAULT NULL,
  `surge1h` double DEFAULT NULL,
  `surge2d` double DEFAULT NULL,
  `surge2c` double DEFAULT NULL,
  `surge2h` double DEFAULT NULL,
  `bid_id` int(11) NOT NULL,
  PRIMARY KEY (`hid`),
  KEY `bbx_hydrologydata_bid_id_310cf0b4_fk_bbx_bbxinfo_bid` (`bid_id`),
  CONSTRAINT `bbx_hydrologydata_bid_id_310cf0b4_fk_bbx_bbxinfo_bid` FOREIGN KEY (`bid_id`) REFERENCES `bbx_bbxinfo` (`bid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bbx_hydrologydata`
--

LOCK TABLES `bbx_hydrologydata` WRITE;
/*!40000 ALTER TABLE `bbx_hydrologydata` DISABLE KEYS */;
/*!40000 ALTER TABLE `bbx_hydrologydata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bbx_meteorologicaldata`
--

DROP TABLE IF EXISTS `bbx_meteorologicaldata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `bbx_meteorologicaldata` (
  `mid` int(11) NOT NULL AUTO_INCREMENT,
  `timestamp` datetime(6) NOT NULL,
  `rain` double DEFAULT NULL,
  `vis` double DEFAULT NULL,
  `cloudc` double DEFAULT NULL,
  `wd` double DEFAULT NULL,
  `ws` double DEFAULT NULL,
  `cwd` double DEFAULT NULL,
  `cws` double DEFAULT NULL,
  `at` double DEFAULT NULL,
  `dpt` double DEFAULT NULL,
  `bp` double DEFAULT NULL,
  `wetnow` double DEFAULT NULL,
  `wet1` double DEFAULT NULL,
  `wet2` double DEFAULT NULL,
  `cloudlc` double DEFAULT NULL,
  `clouds` double DEFAULT NULL,
  `cloudms` double DEFAULT NULL,
  `cloudhs` double DEFAULT NULL,
  `bid_id` int(11) NOT NULL,
  PRIMARY KEY (`mid`),
  KEY `bbx_meteorologicaldata_bid_id_25418f1a_fk_bbx_bbxinfo_bid` (`bid_id`),
  CONSTRAINT `bbx_meteorologicaldata_bid_id_25418f1a_fk_bbx_bbxinfo_bid` FOREIGN KEY (`bid_id`) REFERENCES `bbx_bbxinfo` (`bid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bbx_meteorologicaldata`
--

LOCK TABLES `bbx_meteorologicaldata` WRITE;
/*!40000 ALTER TABLE `bbx_meteorologicaldata` DISABLE KEYS */;
/*!40000 ALTER TABLE `bbx_meteorologicaldata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bbx_realtimedata`
--

DROP TABLE IF EXISTS `bbx_realtimedata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `bbx_realtimedata` (
  `rdid` int(11) NOT NULL AUTO_INCREMENT,
  `timestamp` datetime(6) NOT NULL,
  `rain` double DEFAULT NULL,
  `vis` double DEFAULT NULL,
  `cloudc` double DEFAULT NULL,
  `wd` double DEFAULT NULL,
  `ws` double DEFAULT NULL,
  `cwd` double DEFAULT NULL,
  `cws` double DEFAULT NULL,
  `at` double DEFAULT NULL,
  `dpt` double DEFAULT NULL,
  `bp` double DEFAULT NULL,
  `wetnow` double DEFAULT NULL,
  `wet1` double DEFAULT NULL,
  `wet2` double DEFAULT NULL,
  `cloudlc` double DEFAULT NULL,
  `clouds` double DEFAULT NULL,
  `cloudms` double DEFAULT NULL,
  `cloudhs` double DEFAULT NULL,
  `wt` double DEFAULT NULL,
  `wvs` double DEFAULT NULL,
  `wv` double DEFAULT NULL,
  `surge1d` double DEFAULT NULL,
  `surge1c` double DEFAULT NULL,
  `surge1h` double DEFAULT NULL,
  `surge2d` double DEFAULT NULL,
  `surge2c` double DEFAULT NULL,
  `surge2h` double DEFAULT NULL,
  `bid_id` int(11) NOT NULL,
  PRIMARY KEY (`rdid`),
  KEY `bbx_realtimedata_bid_id_b45869d4_fk_bbx_bbxinfo_bid` (`bid_id`),
  CONSTRAINT `bbx_realtimedata_bid_id_b45869d4_fk_bbx_bbxinfo_bid` FOREIGN KEY (`bid_id`) REFERENCES `bbx_bbxinfo` (`bid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bbx_realtimedata`
--

LOCK TABLES `bbx_realtimedata` WRITE;
/*!40000 ALTER TABLE `bbx_realtimedata` DISABLE KEYS */;
/*!40000 ALTER TABLE `bbx_realtimedata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(7,'bbx','bbxinfo'),(8,'bbx','bbxspaceinfo'),(9,'bbx','bbxspacetempinfo'),(10,'bbx','hydrologydata'),(11,'bbx','meteorologicaldata'),(12,'bbx','realtimedata'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'bbx','0001_initial','2018-12-05 07:24:30.498374'),(2,'contenttypes','0001_initial','2018-12-05 07:25:08.045966'),(3,'auth','0001_initial','2018-12-05 07:25:08.240065'),(4,'admin','0001_initial','2018-12-05 07:25:08.297990'),(5,'admin','0002_logentry_remove_auto_add','2018-12-05 07:25:08.306446'),(6,'admin','0003_logentry_add_action_flag_choices','2018-12-05 07:25:08.314410'),(7,'admin','0004_auto_20181015_1013','2018-12-05 07:25:08.323598'),(8,'contenttypes','0002_remove_content_type_name','2018-12-05 07:25:08.379348'),(9,'auth','0002_alter_permission_name_max_length','2018-12-05 07:25:08.401523'),(10,'auth','0003_alter_user_email_max_length','2018-12-05 07:25:08.419309'),(11,'auth','0004_alter_user_username_opts','2018-12-05 07:25:08.427342'),(12,'auth','0005_alter_user_last_login_null','2018-12-05 07:25:08.453692'),(13,'auth','0006_require_contenttypes_0002','2018-12-05 07:25:08.455501'),(14,'auth','0007_alter_validators_add_error_messages','2018-12-05 07:25:08.463378'),(15,'auth','0008_alter_user_username_max_length','2018-12-05 07:25:08.496157'),(16,'auth','0009_alter_user_last_name_max_length','2018-12-05 07:25:08.524496'),(17,'sessions','0001_initial','2018-12-05 07:25:08.541978');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
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
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-05 15:37:53
