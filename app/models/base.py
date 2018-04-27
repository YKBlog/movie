# -*- coding: utf-8 -*-
# @Time    : 2018/4/16 18:21
# @Contact : gedongdonghappy@gmail.com

# from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True

    # @property
    # def create_datetime(self):
    #     if self.create_time:
    #         return datetime.fromtimestamp(self.create_time)
    #     else:
    #         return None
