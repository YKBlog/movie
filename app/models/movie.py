# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 14:25
# @Contact : gedongdonghappy@gmail.com
from sqlalchemy import Column, Integer, String, Float, Text

from app.models.base import Base


class Movie(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    douban_id = Column(Integer, default=0, server_default='0', comment='豆瓣id')
    title = Column(String(50), nullable=False, default='', server_default='', comment='标题')
    rate = Column(Float, default=0, server_default='0', comment='评分')
    cover = Column(String(200), default='', server_default='', comment='封面图')
    summary = Column(Text(), default='', server_default='', comment='摘要')
