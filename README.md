# Python Flask 豆瓣电影展示网站

## demo展示：[http://movie.elnmp.com](http://movie.elnmp.com)

**该代码为学习代码，不涉及商业利益，如有任何问题请及时联系我删除**

## 运行环境
 Apache2.4 + mod_wsgi + mysql
 
 ## Python软件包
 
 * flask
 * flask-sqlalchemy
 * cymysql
 
 ## Apache配置
 
 ```
 <VirtualHost *>
    ServerName movie.elnmp.com
    WSGIDaemonProcess movie user=apache group=apache threads=5
    WSGIScriptAlias / /data/movie/movie.wsgi
    ErrorLog /var/log/httpd/movie_error_log
    CustomLog /var/log/httpd/movie_access_log combined
    <Directory /data/movie>
        ServerSignature Off
        Options Includes ExecCGI FollowSymLinks
        WSGIProcessGroup movie
        WSGIApplicationGroup %{GLOBAL}
        require all granted
    </Directory>
</VirtualHost>
 ```
 
 ## movie.wsgi文件配置
 
 ```
 activate_this = '/home/virtualenvs/movie-3QK-yS3b/bin/activate_this.py'  # activate_this.py文件目录，跟下面Python包目录对应
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys
sys.path.insert(0, '/home/virtualenvs/movie-3QK-yS3b/lib/python3.6/site-packages/')  # Python包目录
sys.path.insert(0, '/data/movie')  # 项目根目录

from movie import app as application
 ```
 
## 表结构

movie表：
```
CREATE TABLE `movie` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `douban_id` int(10) unsigned NOT NULL DEFAULT '0',
  `title` varchar(50) CHARACTER SET utf8mb4 NOT NULL DEFAULT '' COMMENT '标题',
  `rate` float NOT NULL DEFAULT '0' COMMENT '评分',
  `cover` varchar(200) CHARACTER SET utf8mb4 NOT NULL DEFAULT '' COMMENT '封面图',
  `summary` text COLLATE utf8mb4_unicode_520_ci NOT NULL COMMENT '摘要',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=327 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
```

movie_comments表：
```
CREATE TABLE `movie_comments` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `douban_id` int(10) unsigned NOT NULL DEFAULT '0',
  `nickname` varchar(50) CHARACTER SET utf8mb4 NOT NULL DEFAULT '' COMMENT '用户名',
  `score` tinyint(3) unsigned NOT NULL DEFAULT '0' COMMENT '评分',
  `comment_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00' COMMENT '评论日期',
  `content` text CHARACTER SET utf8mb4 NOT NULL COMMENT '评论内容',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=145765 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
```
