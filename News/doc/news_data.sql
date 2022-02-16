SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for hs_media
-- ----------------------------
DROP TABLE IF EXISTS `news_data`;
CREATE TABLE `news_data`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `author` varchar(255)  DEFAULT NULL COMMENT '作者',
  `comment` text  DEFAULT NULL COMMENT '评论',
  `content` longtext  DEFAULT NULL COMMENT '文章内容 纯文本',
  `creationTime` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `excavateDataFileList` longtext  DEFAULT NULL COMMENT '附件(包含图片、PDF、其他)',
  `imgList` text  DEFAULT NULL COMMENT '文章图片原链接',
  `keywords`  varchar(255)  DEFAULT NULL COMMENT '关键词',
  `publicDate` varchar(255)  DEFAULT NULL COMMENT '文章发布日期格式，例: 2020-01-30$yyyy-MM-dd',
  `publicDateTime` varchar(255)  DEFAULT NULL COMMENT '文章发布时间',
  `refernceUrl` varchar(255)  DEFAULT NULL COMMENT '文章域名',
  `region` varchar(255)  DEFAULT NULL COMMENT '网站所属国家',

  `siteCofId` varchar(255)  DEFAULT NULL COMMENT '媒体板块名称ID，对应hs_media_section表mediaSectionId字段',
  `siteCofName` varchar(255)  DEFAULT NULL COMMENT '媒体板块名称，对应hs_media_section表mediaSectionName字段',
  `title` varchar(255)  DEFAULT NULL COMMENT '文章标题',
  `url` varchar(1000)  DEFAULT NULL COMMENT '文章URL链接',
  `tag` tinyint(4) DEFAULT 0,
    
  PRIMARY KEY (`id`) USING BTREE
)ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;
