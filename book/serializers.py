# coding: utf-8

from marshmallow import fields, Schema

class BookPostSchema(Schema):
    class Meta:
        strict = True

    title = fields.Str(required=True)

class BookDeleteSchema(Schema):
    class Meta:
        strict = True

    book_id = fields.Integer(required=True)