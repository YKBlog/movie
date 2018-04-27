# -*- coding: utf-8 -*-
# @Time    : 2018/4/27 14:46
# @Contact : gedongdonghappy@gmail.com


class MovieViewModel:
    def __init__(self, movie):
        self.id = movie.id
        self.douban_id = movie.douban_id
        self.title = movie.title
        self.rate = movie.rate
        self.cover = movie.cover
        self.summary = movie.summary


class MovieCollection:
    def __init__(self):
        self.movies = []
        self.page = 1
        self.total_page = 0

    def fill(self, movies, page, total_page):
        self.page = page
        self.total_page = total_page
        self.movies = [MovieViewModel(movie) for movie in movies]
