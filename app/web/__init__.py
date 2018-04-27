# -*- coding: utf-8 -*-
# @Time    : 2018/4/11 13:23
# @Contact : gedongdonghappy@gmail.com
from flask import Blueprint

web = Blueprint('web', __name__)


# @web.app_errorhandler(404)
# def not_found(e):
#     return render_template('404.html'), 404


from app.web import movie
