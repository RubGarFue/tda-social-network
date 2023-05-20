-- MySQL dump 10.13  Distrib 8.0.31, for Linux (x86_64)
--
-- Host: localhost    Database: prueba
-- ------------------------------------------------------
-- Server version	8.0.31-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(400) NOT NULL,
  `created_at` int DEFAULT NULL,
  `retrieved_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=223761 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES
(1,'1',NULL,'2022-11-04 16:44:33'),
(2,'2',NULL,'2022-11-04 16:44:34'),
(3,'3',NULL,'2022-11-04 16:44:34'),
(4,'4',NULL,'2022-11-04 16:44:34'),
(5,'5',NULL,'2022-11-04 16:44:34'),
(6,'6',NULL,'2022-11-04 16:44:34'),
(7,'7',NULL,'2022-11-04 16:44:34'),
(8,'8',NULL,'2022-11-04 16:44:34'),
(9,'9',NULL,'2022-11-04 16:44:34'),
(10,'10',NULL,'2022-11-04 16:44:34'),
(11,'11',NULL,'2022-11-04 16:44:34'),
(12,'12',NULL,'2022-11-04 16:44:34'),
(13,'13',NULL,'2022-11-04 16:44:34'),
(14,'14',NULL,'2022-11-04 16:44:35'),
(15,'15',NULL,'2022-11-04 16:44:35'),
-- Nuevos usuarios
(16,'16',NULL,'2022-11-04 16:44:35'),
(17,'17',NULL,'2022-11-04 16:44:35'),
(18,'18',NULL,'2022-11-04 16:44:35'),
(19,'19',NULL,'2022-11-04 16:44:35');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;


--
-- Table structure for table `tweet`
--

DROP TABLE IF EXISTS `tweet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tweet` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tweet_id` varchar(200) NOT NULL,
  `author_id` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `lang` varchar(4) DEFAULT NULL,
  `conversation_id` varchar(200) DEFAULT NULL,
  `text` varchar(900) NOT NULL,
  `retrieved_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tweet_id_2` (`tweet_id`),
  KEY `conversation_id` (`conversation_id`),
  KEY `tweet_id` (`tweet_id`),
  KEY `author_id` (`author_id`),
  CONSTRAINT `tweet_ibfk_1` FOREIGN KEY (`author_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13585217 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tweet`
--

LOCK TABLES `tweet` WRITE;
/*!40000 ALTER TABLE `tweet` DISABLE KEYS */;
INSERT INTO `tweet` VALUES
(1,'1',2,'2019-11-16 23:01:52','es','1195839428578750464','Tweet 1','2022-11-04 16:44:34'),
(2,'2',2,'2019-11-16 23:01:53','es','1195839428578750464','Tweet 2','2022-11-04 16:44:34'),
(3,'3',2,'2019-11-16 23:01:54','es','1195839428578750464','Tweet 3','2022-11-04 16:44:34'),
(4,'4',2,'2019-11-16 23:01:55','es','1195839428578750464','Tweet 4','2022-11-04 16:44:34'),
(5,'5',2,'2019-11-16 23:01:56','es','1195839428578750464','Tweet 5','2022-11-04 16:44:34'),
(6,'6',2,'2019-11-16 23:01:57','es','1195839428578750464','Tweet 6','2022-11-04 16:44:34'),
(7,'7',2,'2019-11-16 23:01:58','es','1195839428578750464','Tweet 7','2022-11-04 16:44:34'),

(8,'8',3,'2019-11-16 23:01:59','es','1195839428578750464','Tweet 8','2022-11-04 16:44:34'),
(9,'9',3,'2019-11-16 23:02:00','es','1195839428578750464','Tweet 9','2022-11-04 16:44:34'),
(10,'10',3,'2019-11-16 23:02:01','es','1195839428578750464','Tweet 10','2022-11-04 16:44:34'),
(11,'11',3,'2019-11-16 23:02:02','es','1195839428578750464','Tweet 11','2022-11-04 16:44:34'),

(12,'12',4,'2019-11-16 23:02:03','es','1195839428578750464','Tweet 12','2022-11-04 16:44:34'),
(13,'13',4,'2019-11-16 23:02:04','es','1195839428578750464','Tweet 13','2022-11-04 16:44:34'),
(14,'14',4,'2019-11-16 23:02:05','es','1195839428578750464','Tweet 14','2022-11-04 16:44:34'),
(15,'15',4,'2019-11-16 23:02:06','es','1195839428578750464','Tweet 15','2022-11-04 16:44:34'),
(16,'16',4,'2019-11-16 23:02:07','es','1195839428578750464','Tweet 16','2022-11-04 16:44:34'),

(17,'17',5,'2019-11-16 23:02:08','es','1195839428578750464','Tweet 17','2022-11-04 16:44:34'),
(18,'18',5,'2019-11-16 23:02:09','es','1195839428578750464','Tweet 18','2022-11-04 16:44:34'),

(19,'19',6,'2019-11-16 23:02:10','es','1195839428578750464','Tweet 19','2022-11-04 16:44:34'),
(20,'20',6,'2019-11-16 23:02:11','es','1195839428578750464','Tweet 20','2022-11-04 16:44:34'),
(21,'21',6,'2019-11-16 23:02:12','es','1195839428578750464','Tweet 21','2022-11-04 16:44:34'),
(22,'22',6,'2019-11-16 23:02:13','es','1195839428578750464','Tweet 22','2022-11-04 16:44:34'),
(23,'23',6,'2019-11-16 23:02:14','es','1195839428578750464','Tweet 23','2022-11-04 16:44:34'),
(24,'24',6,'2019-11-16 23:02:15','es','1195839428578750464','Tweet 24','2022-11-04 16:44:34'),
(25,'25',6,'2019-11-16 23:02:16','es','1195839428578750464','Tweet 25','2022-11-04 16:44:34'),
(26,'26',6,'2019-11-16 23:02:17','es','1195839428578750464','Tweet 26','2022-11-04 16:44:34'),
(27,'27',6,'2019-11-16 23:02:18','es','1195839428578750464','Tweet 27','2022-11-04 16:44:34'),

(28,'28',7,'2019-11-16 23:02:19','es','1195839428578750464','Tweet 28','2022-11-04 16:44:34'),
(29,'29',7,'2019-11-16 23:02:20','es','1195839428578750464','Tweet 29','2022-11-04 16:44:34'),
(30,'30',7,'2019-11-16 23:02:21','es','1195839428578750464','Tweet 30','2022-11-04 16:44:34'),
(31,'31',7,'2019-11-16 23:02:22','es','1195839428578750464','Tweet 31','2022-11-04 16:44:34'),
(32,'32',7,'2019-11-16 23:02:23','es','1195839428578750464','Tweet 32','2022-11-04 16:44:34'),
(33,'33',7,'2019-11-16 23:02:24','es','1195839428578750464','Tweet 33','2022-11-04 16:44:34'),
(34,'34',7,'2019-11-16 23:02:25','es','1195839428578750464','Tweet 34','2022-11-04 16:44:34'),
(35,'35',7,'2019-11-16 23:02:26','es','1195839428578750464','Tweet 35','2022-11-04 16:44:34'),

(36,'36',8,'2019-11-16 23:02:27','es','1195839428578750464','Tweet 36','2022-11-04 16:44:34'),
(37,'37',8,'2019-11-16 23:02:28','es','1195839428578750464','Tweet 37','2022-11-04 16:44:34'),
(38,'38',8,'2019-11-16 23:02:29','es','1195839428578750464','Tweet 38','2022-11-04 16:44:34'),
(39,'39',8,'2019-11-16 23:02:30','es','1195839428578750464','Tweet 39','2022-11-04 16:44:34'),
(40,'40',8,'2019-11-16 23:02:31','es','1195839428578750464','Tweet 40','2022-11-04 16:44:34'),
(41,'41',8,'2019-11-16 23:02:32','es','1195839428578750464','Tweet 41','2022-11-04 16:44:34'),
(42,'42',8,'2019-11-16 23:02:33','es','1195839428578750464','Tweet 42','2022-11-04 16:44:34'),
(43,'43',8,'2019-11-16 23:02:34','es','1195839428578750464','Tweet 43','2022-11-04 16:44:34'),
(44,'44',8,'2019-11-16 23:02:35','es','1195839428578750464','Tweet 44','2022-11-04 16:44:34'),
(45,'45',8,'2019-11-16 23:02:36','es','1195839428578750464','Tweet 45','2022-11-04 16:44:34'),

(46,'46',9,'2019-11-16 23:02:37','es','1195839428578750464','Tweet 46','2022-11-04 16:44:34'),
(47,'47',9,'2019-11-16 23:02:38','es','1195839428578750464','Tweet 47','2022-11-04 16:44:34'),
(48,'48',9,'2019-11-16 23:02:39','es','1195839428578750464','Tweet 48','2022-11-04 16:44:34'),
(49,'49',9,'2019-11-16 23:02:40','es','1195839428578750464','Tweet 49','2022-11-04 16:44:34'),
(50,'50',9,'2019-11-16 23:02:41','es','1195839428578750464','Tweet 50','2022-11-04 16:44:34'),
(51,'51',9,'2019-11-16 23:02:42','es','1195839428578750464','Tweet 51','2022-11-04 16:44:34'),
(52,'52',9,'2019-11-16 23:02:43','es','1195839428578750464','Tweet 52','2022-11-04 16:44:34'),
(53,'53',9,'2019-11-16 23:02:44','es','1195839428578750464','Tweet 53','2022-11-04 16:44:34'),

(54,'54',10,'2019-11-16 23:02:45','es','1195839428578750464','Tweet 54','2022-11-04 16:44:34'),
(55,'55',10,'2019-11-16 23:02:46','es','1195839428578750464','Tweet 55','2022-11-04 16:44:34'),
(56,'56',10,'2019-11-16 23:02:47','es','1195839428578750464','Tweet 56','2022-11-04 16:44:34'),
(57,'57',10,'2019-11-16 23:02:48','es','1195839428578750464','Tweet 57','2022-11-04 16:44:34'),
(58,'58',10,'2019-11-16 23:02:49','es','1195839428578750464','Tweet 58','2022-11-04 16:44:34'),
(59,'59',10,'2019-11-16 23:02:50','es','1195839428578750464','Tweet 59','2022-11-04 16:44:34'),
(60,'60',10,'2019-11-16 23:02:51','es','1195839428578750464','Tweet 60','2022-11-04 16:44:34'),
(61,'61',10,'2019-11-16 23:02:52','es','1195839428578750464','Tweet 61','2022-11-04 16:44:34'),
(62,'62',10,'2019-11-16 23:02:53','es','1195839428578750464','Tweet 62','2022-11-04 16:44:34'),

(63,'63',11,'2019-11-16 23:02:54','es','1195839428578750464','Tweet 63','2022-11-04 16:44:34'),
(64,'64',11,'2019-11-16 23:02:55','es','1195839428578750464','Tweet 64','2022-11-04 16:44:34'),

(65,'65',12,'2019-11-16 23:02:56','es','1195839428578750464','Tweet 65','2022-11-04 16:44:34'),
(66,'66',12,'2019-11-16 23:02:57','es','1195839428578750464','Tweet 66','2022-11-04 16:44:34'),
(67,'67',12,'2019-11-16 23:02:58','es','1195839428578750464','Tweet 67','2022-11-04 16:44:34'),

(68,'68',15,'2019-11-16 23:02:59','es','1195839428578750464','Tweet 68','2022-11-04 16:44:34'),
(69,'69',15,'2019-11-16 23:03:00','es','1195839428578750464','Tweet 69','2022-11-04 16:44:34'),
(70,'70',15,'2019-11-16 23:03:01','es','1195839428578750464','Tweet 70','2022-11-04 16:44:34'),
(71,'71',15,'2019-11-16 23:03:02','es','1195839428578750464','Tweet 71','2022-11-04 16:44:34'),
(72,'72',15,'2019-11-16 23:03:03','es','1195839428578750464','Tweet 72','2022-11-04 16:44:34'),
(73,'73',15,'2019-11-16 23:03:04','es','1195839428578750464','Tweet 73','2022-11-04 16:44:34'),
(74,'74',15,'2019-11-16 23:03:05','es','1195839428578750464','Tweet 74','2022-11-04 16:44:34'),
(75,'75',15,'2019-11-16 23:03:06','es','1195839428578750464','Tweet 75','2022-11-04 16:44:34'),
(76,'76',15,'2019-11-16 23:03:07','es','1195839428578750464','Tweet 76','2022-11-04 16:44:34'),
(77,'77',15,'2019-11-16 23:03:08','es','1195839428578750464','Tweet 77','2022-11-04 16:44:34'),
(78,'78',15,'2019-11-16 23:03:09','es','1195839428578750464','Tweet 78','2022-11-04 16:44:34'),

-- Nuevos tweets
(79,'79',16,'2019-11-16 23:03:10','es','1195839428578750464','Tweet 79','2022-11-04 16:44:34'),
(80,'80',16,'2019-11-16 23:03:11','es','1195839428578750464','Tweet 80','2022-11-04 16:44:34'),

(81,'81',17,'2019-11-16 23:03:12','es','1195839428578750464','Tweet 81','2022-11-04 16:44:34'),

(82,'82',18,'2019-11-16 23:03:13','es','1195839428578750464','Tweet 82','2022-11-04 16:44:34'),
(83,'83',18,'2019-11-16 23:03:14','es','1195839428578750464','Tweet 83','2022-11-04 16:44:34'),
(84,'84',18,'2019-11-16 23:03:15','es','1195839428578750464','Tweet 84','2022-11-04 16:44:34'),

(85,'85',19,'2019-11-16 23:03:16','es','1195839428578750464','Tweet 85','2022-11-04 16:44:34'),
(86,'86',19,'2019-11-16 23:03:17','es','1195839428578750464','Tweet 86','2022-11-04 16:44:34');
/*!40000 ALTER TABLE `tweet` ENABLE KEYS */;
UNLOCK TABLES;


--
-- Table structure for table `like_tweet`
--

DROP TABLE IF EXISTS `like_tweet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `like_tweet` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `tweet_id` int NOT NULL,
  `action_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `tweet_id` (`tweet_id`),
  KEY `like_tweet_ibfk_2` (`user_id`),
  CONSTRAINT `like_tweet_ibfk_1` FOREIGN KEY (`tweet_id`) REFERENCES `tweet` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `like_tweet_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=380 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `like_tweet`
--

LOCK TABLES `like_tweet` WRITE;
/*!40000 ALTER TABLE `like_tweet` DISABLE KEYS */;
INSERT INTO `like_tweet` VALUES
(1,1,8,'2022-11-04 17:00:48'),
(2,1,9,'2022-11-04 17:00:48'),
(3,1,10,'2022-11-04 17:00:48'),
(4,1,11,'2022-11-04 17:00:48'),

(5,1,17,'2022-11-04 17:00:48'),
(6,1,18,'2022-11-04 17:00:48'),


(7,2,19,'2022-11-04 17:00:48'),
(8,2,20,'2022-11-04 17:00:48'),
(9,2,21,'2022-11-04 17:00:48'),
(10,2,22,'2022-11-04 17:00:48'),
(11,2,23,'2022-11-04 17:00:48'),
(12,2,24,'2022-11-04 17:00:48'),
(13,2,25,'2022-11-04 17:00:48'),
(14,2,26,'2022-11-04 17:00:48'),
(15,2,27,'2022-11-04 17:00:48'),


(16,3,12,'2022-11-04 17:00:48'),
(17,3,13,'2022-11-04 17:00:48'),
(18,3,14,'2022-11-04 17:00:48'),

(19,3,28,'2022-11-04 17:00:48'),
(20,3,29,'2022-11-04 17:00:48'),
(21,3,30,'2022-11-04 17:00:48'),
(22,3,31,'2022-11-04 17:00:48'),


(23,4,1,'2022-11-04 17:00:48'),
(24,4,2,'2022-11-04 17:00:48'),
(25,4,3,'2022-11-04 17:00:48'),
(26,4,4,'2022-11-04 17:00:48'),
(27,4,5,'2022-11-04 17:00:48'),
(28,4,6,'2022-11-04 17:00:48'),
(29,4,7,'2022-11-04 17:00:48'),

(30,4,28,'2022-11-04 17:00:48'),
(31,4,29,'2022-11-04 17:00:48'),
(32,4,30,'2022-11-04 17:00:48'),
(33,4,31,'2022-11-04 17:00:48'),
(34,4,32,'2022-11-04 17:00:48'),
(35,4,33,'2022-11-04 17:00:48'),
(36,4,34,'2022-11-04 17:00:48'),
(37,4,35,'2022-11-04 17:00:48'),


(38,5,54,'2022-11-04 17:00:48'),
(39,5,55,'2022-11-04 17:00:48'),
(40,5,56,'2022-11-04 17:00:48'),
(41,5,57,'2022-11-04 17:00:48'),
(42,5,58,'2022-11-04 17:00:48'),
(43,5,59,'2022-11-04 17:00:48'),
(44,5,60,'2022-11-04 17:00:48'),


(45,6,36,'2022-11-04 17:00:48'),
(46,6,37,'2022-11-04 17:00:48'),
(47,6,38,'2022-11-04 17:00:48'),
(48,6,39,'2022-11-04 17:00:48'),
(49,6,40,'2022-11-04 17:00:48'),
(50,6,41,'2022-11-04 17:00:48'),
(51,6,42,'2022-11-04 17:00:48'),
(52,6,43,'2022-11-04 17:00:48'),

(53,6,46,'2022-11-04 17:00:48'),


(54,7,17,'2022-11-04 17:00:48'),

(55,7,43,'2022-11-04 17:00:48'),
(56,7,44,'2022-11-04 17:00:48'),
(57,7,45,'2022-11-04 17:00:48'),


(58,8,1,'2022-11-04 17:00:48'),
(59,8,4,'2022-11-04 17:00:48'),
(60,8,7,'2022-11-04 17:00:48'),

(61,8,12,'2022-11-04 17:00:48'),
(62,8,13,'2022-11-04 17:00:48'),
(63,8,14,'2022-11-04 17:00:48'),
(64,8,15,'2022-11-04 17:00:48'),
(65,8,16,'2022-11-04 17:00:48'),

(66,8,46,'2022-11-04 17:00:48'),
(67,8,47,'2022-11-04 17:00:48'),
(68,8,48,'2022-11-04 17:00:48'),
(69,8,49,'2022-11-04 17:00:48'),


(70,11,28,'2022-11-04 17:00:48'),
(71,11,29,'2022-11-04 17:00:48'),
(72,11,34,'2022-11-04 17:00:48'),
(73,11,35,'2022-11-04 17:00:48'),

(74,11,54,'2022-11-04 17:00:48'),
(75,11,55,'2022-11-04 17:00:48'),
(76,11,56,'2022-11-04 17:00:48'),
(77,11,57,'2022-11-04 17:00:48'),
(78,11,58,'2022-11-04 17:00:48'),
(79,11,59,'2022-11-04 17:00:48'),
(80,11,60,'2022-11-04 17:00:48'),
(81,11,61,'2022-11-04 17:00:48'),


(82,12,36,'2022-11-04 17:00:48'),
(83,12,37,'2022-11-04 17:00:48'),
(84,12,38,'2022-11-04 17:00:48'),
(85,12,39,'2022-11-04 17:00:48'),
(86,12,40,'2022-11-04 17:00:48'),
(87,12,41,'2022-11-04 17:00:48'),
(88,12,42,'2022-11-04 17:00:48'),
(89,12,43,'2022-11-04 17:00:48'),
(90,12,44,'2022-11-04 17:00:48'),
(91,12,45,'2022-11-04 17:00:48'),

(92,12,46,'2022-11-04 17:00:48'),
(93,12,47,'2022-11-04 17:00:48'),

(94,12,63,'2022-11-04 17:00:48'),
(95,12,64,'2022-11-04 17:00:48'),

(96,12,68,'2022-11-04 17:00:48'),
(97,12,69,'2022-11-04 17:00:48'),
(98,12,70,'2022-11-04 17:00:48'),
(99,12,71,'2022-11-04 17:00:48'),
(100,12,72,'2022-11-04 17:00:48'),
(101,12,73,'2022-11-04 17:00:48'),
(102,12,74,'2022-11-04 17:00:48'),
(103,12,75,'2022-11-04 17:00:48'),
(104,12,76,'2022-11-04 17:00:48'),
(105,12,77,'2022-11-04 17:00:48'),


(106,13,46,'2022-11-04 17:00:48'),
(107,13,47,'2022-11-04 17:00:48'),
(108,13,48,'2022-11-04 17:00:48'),
(109,13,49,'2022-11-04 17:00:48'),
(110,13,50,'2022-11-04 17:00:48'),
(111,13,51,'2022-11-04 17:00:48'),
(112,13,52,'2022-11-04 17:00:48'),
(113,13,53,'2022-11-04 17:00:48'),

(114,13,65,'2022-11-04 17:00:48'),


(115,14,54,'2022-11-04 17:00:48'),
(116,14,55,'2022-11-04 17:00:48'),
(117,14,56,'2022-11-04 17:00:48'),
(118,14,57,'2022-11-04 17:00:48'),
(119,14,58,'2022-11-04 17:00:48'),
(120,14,59,'2022-11-04 17:00:48'),

(121,14,68,'2022-11-04 17:00:48'),
(122,14,69,'2022-11-04 17:00:48'),
(123,14,70,'2022-11-04 17:00:48'),
(124,14,71,'2022-11-04 17:00:48'),
(125,14,72,'2022-11-04 17:00:48'),
(126,14,73,'2022-11-04 17:00:48'),
(127,14,74,'2022-11-04 17:00:48'),
(128,14,75,'2022-11-04 17:00:48'),

-- Nuevos likes
(129,16,68,'2022-11-04 17:00:48'), -- Like a Usuario 15
(130,16,65,'2022-11-04 17:00:48'), -- Like a Usuario 12
(131,16,63,'2022-11-04 17:00:48'), -- Like a Usuario 11
(132,16,17,'2022-11-04 17:00:48'), -- Like a Usuario 5

(133,17,85,'2022-11-04 17:00:48'), -- Like a Usuario 19
(134,17,81,'2022-11-04 17:00:48'), -- Like a Usuario 17
(135,17,65,'2022-11-04 17:00:48'), -- Like a Usuario 12
(136,17,54,'2022-11-04 17:00:48'), -- Like a Usuario 10
(137,17,1,'2022-11-04 17:00:48'), -- Like a Usuario 2

(138,18,81,'2022-11-04 17:00:48'), -- Like a Usuario 17
(139,18,85,'2022-11-04 17:00:48'), -- Like a Usuario 19

(140,19,82,'2022-11-04 17:00:48'), -- Like a Usuario 18
(141,19,68,'2022-11-04 17:00:48'), -- Like a Usuario 15
(142,19,46,'2022-11-04 17:00:48'), -- Like a Usuario 9
(143,19,28,'2022-11-04 17:00:48'), -- Like a Usuario 7
(144,19,19,'2022-11-04 17:00:48'), -- Like a Usuario 6
(145,19,1,'2022-11-04 17:00:48'); -- Like a Usuario 2
/*!40000 ALTER TABLE `like_tweet` ENABLE KEYS */;
UNLOCK TABLES;