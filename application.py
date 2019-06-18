#!/usr/bin/python
# -*- coding: utf-8 -*-

from sanic import Sanic
from urllib import response
from blueprints.globalRequest import global_requests
from blueprints.containers import application as containers
from blueprints.images import application as images

app = Sanic(__name__)
app.blueprint(containers)
app.blueprint(images)
app.blueprint(global_requests)


def main():
    app.run(host="0.0.0.0", port=5000, workers=1, debug=False)


if __name__ == '__main__':
    main()
