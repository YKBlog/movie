# -*- coding: utf-8 -*-
# @Time    : 2018/4/26 11:54
# @Contact : gedongdonghappy@gmail.com
from math import ceil

from flask import current_app, render_template, jsonify, json

from app.models.comments import Comments
from app.models.movie import Movie
from app.view_models.comment import CommentCollection
from app.view_models.movie import MovieCollection
from app.web import web


@web.route('/')
def movie_list():
    v_list = Movie.query.limit(current_app.config['PER_PAGE']).all()
    return render_template('list.html', v_list=v_list, nav_bar='index')


@web.route('/movie/<id>')
def movie_detail(id):
    movie = Movie.query.get_or_404(id)
    first_20 = Comments.query.filter_by(douban_id=movie.douban_id).limit(20).all()
    return render_template('detail.html', movie=movie, comments=first_20, nav_bar='index')


@web.route('/list_more/<page>')
def list_more(page):
    offset = (int(page) - 1) * current_app.config['PER_PAGE']
    v_list = Movie.query.offset(offset).limit(current_app.config['PER_PAGE']).all()
    total = Movie.query.count()
    total_page = ceil(total / current_app.config['PER_PAGE'])
    view_model = MovieCollection()
    view_model.fill(v_list, int(page), total_page)
    return json.dumps(view_model, default=lambda o: o.__dict__), 200, {'content-type': 'application/json'}


@web.route('/comment_more/<douban_id>/<page>')
def comment_more(douban_id, page):
    offset = (int(page) - 1) * current_app.config['PER_PAGE']
    v_list = Comments.query.filter_by(douban_id=douban_id).offset(offset).limit(current_app.config['PER_PAGE']).all()
    total = Comments.query.filter_by(douban_id=douban_id).count()
    total_page = ceil(total / current_app.config['PER_PAGE'])
    view_model = CommentCollection()
    view_model.fill(v_list, int(page), total_page)
    return json.dumps(view_model, default=lambda o: o.__dict__), 200, {'content-type': 'application/json'}


@web.route('/data')
def web_data():
    return render_template('data.html', nav_bar='web')


@web.route('/tech')
def tech():
    return render_template('technology.html', nav_bar='web')


@web.route('/about')
def about():
    return render_template('about.html', nav_bar='about')
