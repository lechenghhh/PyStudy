/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50635
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50635
File Encoding         : 65001

Date: 2018-08-08 15:08:30
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for employee
-- ----------------------------
DROP TABLE IF EXISTS `employee`;
CREATE TABLE `employee` (
  `FIRST_NAME` char(20) NOT NULL,
  `LAST_NAME` char(20) DEFAULT NULL,
  `AGE` int(11) DEFAULT NULL,
  `SEX` char(1) DEFAULT NULL,
  `INCOME` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of employee
-- ----------------------------
INSERT INTO `employee` VALUES ('Mac', 'Mohan', '20', 'M', '2000');
INSERT INTO `employee` VALUES ('Mac', 'Mohan', '20', 'M', '2000');
INSERT INTO `employee` VALUES ('Mac', 'Mohan222', '20', 'M', '2000');
