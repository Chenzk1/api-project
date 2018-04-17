-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: 2018-04-17 07:00:35
-- 服务器版本： 5.7.19
-- PHP Version: 7.1.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `myproject`
--

-- --------------------------------------------------------

--
-- 表的结构 `person`
--

DROP TABLE IF EXISTS `person`;
CREATE TABLE IF NOT EXISTS `person` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `department` varchar(40) NOT NULL,
  `days` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `person`
--

INSERT INTO `person` (`id`, `name`, `department`, `days`) VALUES
(1, '陶昌诚', 'HR', 5),
(2, '孔平栋', 'HR', 22),
(3, '霍策克', 'HR', 17),
(4, '古伦鹏', 'HR', 11),
(5, '谢晓波', 'manager', 30),
(6, '何伟', 'manager', 4),
(7, '李娟娟', 'manager', 21),
(8, '余鹏', 'manager', 30),
(9, '钱裕', 'manager', 22),
(10, '余安琛', 'manager', 3),
(11, '蔡昌奇', 'product', 25),
(12, '姜启', 'product', 12),
(13, '叶辉仁', 'product', 24),
(14, '周康松', 'product', 24),
(15, '冯勇振', 'product', 22),
(16, '戚若栋', 'product', 5),
(17, '钟弘腾', 'electrical', 5),
(18, '简河海', 'electrical', 10),
(19, '雷弘世', 'electrical', 8),
(20, '简有江', 'electrical', 19),
(21, '侯永旭', 'electrical', 24),
(22, '刘鹏', 'electrical', 16),
(23, '胡超', 'electrical', 14),
(24, '程彪', 'electrical', 12);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
