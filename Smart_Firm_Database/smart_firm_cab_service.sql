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
-- Table structure for table `cab_service`
--

DROP TABLE IF EXISTS `cab_service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `cab_service` (
  `tid` int(11) NOT NULL AUTO_INCREMENT,
  `eid` int(11) DEFAULT NULL,
  `SOURCEID` int(11) DEFAULT NULL,
  `T_DATE` varchar(45) DEFAULT NULL,
  `STATUS` varchar(45) DEFAULT NULL,
  `DESTINATIONID` int(11) DEFAULT NULL,
  `T_TIME` varchar(45) DEFAULT NULL,
  `AR_STATUS` varchar(45) DEFAULT 'Pending',
  PRIMARY KEY (`tid`),
  KEY `DESTINATIONID_idx` (`DESTINATIONID`),
  KEY `SOURCEID_idx` (`SOURCEID`),
  KEY `t_eid_idx` (`eid`),
  CONSTRAINT `DESTINATIONID` FOREIGN KEY (`DESTINATIONID`) REFERENCES `stations` (`sid`),
  CONSTRAINT `SOURCEID` FOREIGN KEY (`SOURCEID`) REFERENCES `stations` (`sid`),
  CONSTRAINT `t_eid` FOREIGN KEY (`eid`) REFERENCES `emp_w_w` (`eid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cab_service`
--

LOCK TABLES `cab_service` WRITE;
/*!40000 ALTER TABLE `cab_service` DISABLE KEYS */;
INSERT INTO `cab_service` VALUES (1,4,1,'2019-03-02','presentation',5,'08:30','Accepted'),(2,4,1,'2019-03-10','its important',5,'10:00','Rejected');
/*!40000 ALTER TABLE `cab_service` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-04 23:52:41
