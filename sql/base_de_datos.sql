/*
SQLyog Professional v13.1.1 (64 bit)
MySQL - 10.4.27-MariaDB : Database - apptecnoglass
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`apptecnoglass` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `apptecnoglass`;

/*Table structure for table `clientes` */

DROP TABLE IF EXISTS `clientes`;

CREATE TABLE `clientes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  `direccion` varchar(100) DEFAULT NULL,
  `telefono` varchar(100) DEFAULT NULL,
  `nacionalidad` varchar(100) DEFAULT NULL,
  `correo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `clientes` */

insert  into `clientes`(`id`,`nombre`,`direccion`,`telefono`,`nacionalidad`,`correo`) values 
(1,'Michael','calle 123','3005006444 ','Colombiana','msalas@test.com'),
(3,'Antony','calle 456','3773191','Colombiana','msalas@test.com'),
(4,'WIL','calle 789','3662345','Colombiana','msalas@test.com'),
(5,'Gabriel','calle 010','3552143','Colombiana','msalas@test.com');

/*Table structure for table `ordendetalle` */

DROP TABLE IF EXISTS `ordendetalle`;

CREATE TABLE `ordendetalle` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ordenId` int(11) DEFAULT NULL,
  `nombreItem` varchar(100) DEFAULT NULL,
  `largo` varchar(100) DEFAULT NULL,
  `ancho` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `ordendetalle` */

insert  into `ordendetalle`(`id`,`ordenId`,`nombreItem`,`largo`,`ancho`) values 
(4,6,'Vidrio laminado','10','10'),
(5,6,'Vidrio templado','20','30'),
(6,6,'Vidrio común','50','60'),
(7,7,'Vidrio laminado 1','10','10'),
(8,7,'Vidrio templado 1','20','30'),
(9,7,'Vidrio común 1','50','60');

/*Table structure for table `ordenes` */

DROP TABLE IF EXISTS `ordenes`;

CREATE TABLE `ordenes` (
  `ordenId` int(11) NOT NULL AUTO_INCREMENT,
  `orden` varchar(100) DEFAULT NULL,
  `clienteId` int(11) DEFAULT NULL,
  `fechaOrden` date DEFAULT NULL,
  `estado` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ordenId`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Data for the table `ordenes` */

insert  into `ordenes`(`ordenId`,`orden`,`clienteId`,`fechaOrden`,`estado`) values 
(6,'12345',1,'2023-05-02','solicitada'),
(7,'67890',1,'2023-05-15','aprobada');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
