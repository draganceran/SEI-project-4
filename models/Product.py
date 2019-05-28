from app import db
from pony.orm import Required, Set
from marshmallow import Schema, fields, post_load

class Product(db.Entity):
    name = Required(str)
    farm = Set('Farm')

class ProductSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    farms = fields.Nested('FarmSchema', many=True, exclude=('farm', 'user',))

    @post_load
    def load_farms(self, data):
        data['farms'] = [Product.get(id=product_id) for product_id in data['farm_ids']]
        del data['farm_ids']

        return data
