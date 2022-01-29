## 要求二：建立資料庫和資料表

### 建立一個新的資料庫

CREATE DATABASE `website`;

### 使用 website 資料庫

USE `website`;

### 在資料庫中，建立會員資料表，取名字為 member。資料表必須包含以下欄位設定：

CREATE TABLE `member`(
`id` BIGINT AUTO_INCREMENT,
`name` VARCHAR(255) NOT NULL,
`username` VARCHAR(255) NOT NULL,
`password` VARCHAR(255) NOT NULL,
`follower_count` INT DEFAULT '0' NOT NULL,
`time` DATETIME NOT NULL DEFAULT NOW(),
PRIMARY KEY(`id`)
);

## 要求三：SQL CRUD

### 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。

INSERT INTO `member`(`name`,`username`,`password`,`follower_count`) VALUES("Jeff","test","test","600");
INSERT INTO `member`(`name`,`username`,`password`,`follower_count`) VALUES("Nick","aaaa","aaaa","1000");
INSERT INTO `member`(`name`,`username`,`password`,`follower_count`) VALUES("Benson","bbbb","bbbb","1200");
INSERT INTO `member`(`name`,`username`,`password`) VALUES("Tim","cccc","cccc");

### 使用 SELECT 指令取得所有在 member 資料表中的會員資料。

SELECT \* FROM `member`;

### 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由 近到遠排序。

SELECT \* FROM `member` ORDER BY `time` DESC;

### 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位， 由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )

SELECT \* FROM `member` ORDER BY `time` DESC LIMIT 1,3;

### 使用 SELECT 指令取得欄位 username 是 test 的會員資料。

SELECT \* FROM `member` WHERE `username` = "test";

### 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。

SELECT \* FROM `member` WHERE `username` = "test" AND `password` = "test";

### 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位 改成 test2。

UPDATE `member` SET `name` = "test2" WHERE `username` = "test";

## 要求四：SQL Aggregate Functions

### 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。

SELECT COUNT(\*) FROM `member`;

### 取得 member 資料表中，所有會員 follower_count 欄位的總和。

SELECT SUM(`follower_count`) FROM `member`;

### 取得 member 資料表中，所有會員 follower_count 欄位的平均數。

SELECT AVG(`follower_count`) FROM `member`;

## 要求五：SQL JOIN (Optional)

### 在資料庫中，建立新資料表，取名字為 message。資料表中必須包含以下欄位設定：

在資料庫中，建立新資料表，取名字為 message。資料表中必須包含以下欄位設定：
CREATE TABLE `message`(
`id` BIGINT AUTO_INCREMENT,
`member_id` BIGINT NOT NULL,
`content` VARCHAR(255) NOT NULL,
`time` DATETIME NOT NULL DEFAULT NOW(),
PRIMARY KEY(`id`),
FOREIGN KEY (`member_id`) REFERENCES member(`id`) ON DELETE CASCADE
);

INSERT INTO `message`(`member_id`,`content`) VALUES("1","Jeff 的留言");
INSERT INTO `message`(`member_id`,`content`) VALUES("2","Nick 的留言");
INSERT INTO `message`(`member_id`,`content`) VALUES("3","Benson 的留言");
INSERT INTO `message`(`member_id`,`content`) VALUES("4","Tim 的留言");

### 使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。

SELECT `member`.`id`,`member`.`name` , `message`.`content` FROM `member` JOIN `message` ON `member`.`id` = `message`.`member_id`;

### 使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有 留言，資料中須包含留言者會員的姓名。

SELECT `member`.`id`,`member`.`name` , `message`.`content` FROM `member` JOIN `message` ON `member`.`id` = `message`.`member_id`AND `member`.`username` = "test";
