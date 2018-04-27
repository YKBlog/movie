# -*- coding: utf-8 -*-
# @Time    : 2018/4/9 18:51
# @Contact : gedongdonghappy@gmail.com

from app import create_app

app = create_app()

if __name__ == '__main__':
    # 生产环境是nginx+uwsgi，uwsgi以模块的形式调用入口文件，所以不会启动run方法，
    # 保证不会有两个web服务器运行
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=8889)
