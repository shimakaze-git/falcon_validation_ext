# coding: utf-8

from book.serializers import BookDeleteSchema, BookPostSchema

class BookAPI:
    serializers = {
        'post': BookPostSchema,
        'delete': BookDeleteSchema
    }
    
    def on_get(self, req, resp):
        # serializer = req.context['serializer']
        print(req.context)
        print(req)
        print(resp)

    def on_post(self, req, resp):
        serializer = req.context['serializer']
        # req.context['serializer'] contains data sent by user
        # for example: print(serializer['title'])

    def on_delete(self, req, resp):
        serializer = req.context['serializer']
        print(serializer['book_id'])

    def on_put(self, req, resp):
        # no schema for delete method == no data validation
        print(req, resp)

