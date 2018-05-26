# coding: utf-8

import falcon

from core.middleware.serializers import SerializerMiddleware
from api import BookAPI

app = falcon.API(middleware=[
    SerializerMiddleware(),
])
app.add_route("/", BookAPI())


if __name__ == "__main__":
    from wsgiref import simple_server
    # httpd = simple_server.make_server("127.0.0.1", 8000, app)
    httpd = simple_server.make_server("0.0.0.0", 8080, app)
    httpd.serve_forever()