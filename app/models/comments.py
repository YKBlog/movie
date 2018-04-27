# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 14:25
# @Contact : gedongdonghappy@gmail.com
from sqlalchemy import Column, Integer, String, Float, Text, DateTime

from app.models.base import Base


class Comments(Base):
    __tablename__ = 'movie_comments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    douban_id = Column(Integer, default=0, server_default='0', comment='豆瓣id')
    nickname = Column(String(50), nullable=False, default='', server_default='', comment='昵称')
    score = Column(Float, default=0, server_default='0', comment='评分')
    comment_time = Column(DateTime(), default='', server_default='', comment='评论时间')
    content = Column(Text(), default='', server_default='', comment='内容')
