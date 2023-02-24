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
-- Table structure for table `emp_daily_task`
--

DROP TABLE IF EXISTS `emp_daily_task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `emp_daily_task` (
  `emp_dt_id` int(11) NOT NULL AUTO_INCREMENT,
  `task_name` varchar(45) DEFAULT NULL,
  `project_name` varchar(45) DEFAULT NULL,
  `dt_d_id` int(11) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `dt_emp_id` int(11) DEFAULT NULL,
  `status` varchar(45) DEFAULT 'Pending',
  `man_id` int(11) DEFAULT '2',
  PRIMARY KEY (`emp_dt_id`),
  KEY `dt_d_id_idx` (`dt_d_id`),
  KEY `empdt_id_idx` (`dt_emp_id`),
  KEY `man_id_idx` (`man_id`),
  CONSTRAINT `dt_d_id` FOREIGN KEY (`dt_d_id`) REFERENCES `department` (`d_id`),
  CONSTRAINT `empdt_id` FOREIGN KEY (`dt_emp_id`) REFERENCES `emp_registration` (`emp_rid`),
  CONSTRAINT `man_id` FOREIGN KEY (`man_id`) REFERENCES `man_registration` (`man_rid`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emp_daily_task`
--

LOCK TABLES `emp_daily_task` WRITE;
/*!40000 ALTER TABLE `emp_daily_task` DISABLE KEYS */;
INSERT INTO `emp_daily_task` VALUES (5,'php2','php2',3,'tejas',4,'Accepted',2),(6,'css','css1',2,'enjoy',4,'Accepted',2),(7,'upload','document ',5,'upload document',4,'Accepted',2),(8,'project3','jio',1,'database',4,'REJECTED',2),(9,'data update','spark',3,'it is important',4,'Accepted',2),(10,'java','java solr',1,'hadoop',4,'Accepted',1),(11,'java1','java solr1',2,'hadoop1',4,'Rejected',1),(12,'java2','java solr2',3,'hadoop2',4,'Pending',2),(13,'java3','java solr3',4,'hadoop3',4,'Pending',2);
/*!40000 ALTER TABLE `emp_daily_task` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-04 23:52:35
