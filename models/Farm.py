from app import db
from pony.orm import Required, Set, Optional
from marshmallow import Schema, fields, post_load
from .Product import Product


class Comment(db.Entity):
    content = Required(str)
    user = Required('User')
    farm = Required('Farm')

class CommentSchema(Schema):
    id = fields.Int(dump_only=True)
    content = fields.String()
    farm = fields.Nested('FarmSchema')
    user = fields.Nested('UserSchema')

class Farm(db.Entity):
    name = Required(str)
    country = Required(str)
    region = Required(str)
    address = Required(str)
    products = Set('Product')
    image = Required(str)
    accommodation = Required(bool, default=False)
    dissable_acces = Required(bool, default=False)
    user = Required('User')
    description = Required(str)
    long = Optional(float)
    lat = Optional(float)
    comments = Set('Comment')


class FarmSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    country = fields.Str(required=True)
    region = fields.Str(required=True)
    address = fields.Str(required=True)
    products = fields.Nested('ProductSchema', many=True, dump_only=True)
    product_ids = fields.List(fields.Int(), load_only=True)
    image = fields.Str(required=True, many=True)
    accommodation = fields.Bool()
    dissable_acces = fields.Bool()
    description = fields.Str(required=True)
    user = fields.Nested('UserSchema', exclude=('email', 'farms'))
    long = fields.Float()
    lat = fields.Float()
    comments = fields.Nested('CommentSchema', many=True, exclude=('farm', 'user'))


    @post_load
    def load_products(self, data):
        data['products'] = [Product.get(id=product_id) for product_id in data['product_ids']]
        del data['product_ids']

    @post_load
    def load_comments(self, data):
        data['comments'] = [Comment.get(id=comment_id) for comment_id in data['comment_ids']]
        del data['comment_ids']

        return data
