-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: localhost    Database: smart_firm
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `feedback_daily_task`
--

DROP TABLE IF EXISTS `feedback_daily_task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `feedback_daily_task` (
  `FeedbackId` int(11) NOT NULL AUTO_INCREMENT,
  `DailyTaskId` int(11) DEFAULT NULL,
  `ManagerId` int(11) DEFAULT NULL,
  `feedback` varchar(100) DEFAULT NULL,
  `Remarks` varchar(100) DEFAULT NULL,
  `Date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`FeedbackId`),
  KEY `DailyTaskId_idx` (`DailyTaskId`),
  KEY `ManagerId_idx` (`ManagerId`),
  CONSTRAINT `DailyTaskId` FOREIGN KEY (`DailyTaskId`) REFERENCES `emp_daily_task` (`emp_dt_id`),
  CONSTRAINT `ManagerId` FOREIGN KEY (`ManagerId`) REFERENCES `man_registration` (`man_rid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback_daily_task`
--

LOCK TABLES `feedback_daily_task` WRITE;
/*!40000 ALTER TABLE `feedback_daily_task` DISABLE KEYS */;
INSERT INTO `feedback_daily_task` VALUES (1,5,1,'nice','no','2019-03-21 18:09:11'),(2,10,1,'very nice','no','2019-03-21 22:30:11'),(3,11,1,'very bad','improvement','2019-03-21 22:35:24');
/*!40000 ALTER TABLE `feedback_daily_task` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-04 23:52:39
