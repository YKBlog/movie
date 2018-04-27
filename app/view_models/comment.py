# -*- coding: utf-8 -*-
# @Time    : 2018/4/27 14:46
# @Contact : gedongdonghappy@gmail.com


class CommentViewModel:
    def __init__(self, comment):
        self.id = comment.id
        self.douban_id = comment.douban_id
        self.nickname = comment.nickname
        self.score = comment.score
        self.comment_time = str(comment.comment_time)
        self.content = comment.content


class CommentCollection:
    def __init__(self):
        self.comments = []
        self.page = 1
        self.total_page = 0

    def fill(self, comments, page, total_page):
        self.page = page
        self.total_page = total_page
        self.comments = [CommentViewModel(comment) for comment in comments]
