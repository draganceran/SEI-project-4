from app import db
from pony.orm import Required, Set
from marshmallow import Schema, fields, post_load
from .Product import Product


class Farm(db.Entity):
    name = Required(str)
    country = Required(str)
    region = Required(str)
    address = Required(str)
    products = Set('Category')
    image = Required(str)
    accommodation = Required(bool, default=False)
    dissable_acces = Required(bool, default=False)
    user = Required('User')
    description = Required(str)


class FarmSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    country = fields.Str(required=True)
    region = fields.Str(required=True)
    address = fields.Str(required=True)
    products = fields.Nested('ProductSchema', exclude=('farm', ), dump_only=True)
    image = fields.Str(required=True)
    accommodation = fields.Bool()
    dissable_acces = fields.Bool()
    description = fields.Str(required=True)
    user = fields.Nested('UserSchema', exclude=('email', 'farm'))

    @post_load
    def load_products(self, data):
        data['products'] = [Product.get(id=product_id) for product_id in data['product_ids']]
        del data['product_ids']

        return data
