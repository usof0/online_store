from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    country = fields.Str(required=True)
    state = fields.Str()
    city = fields.Str()
    phone_number = fields.Str()
    created_at = fields.DateTime(dump_only=True)

class LoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)

class PlainBrandSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    logo_url = fields.Str(required=True)

class PlainProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Decimal(required=True)
    sku = fields.Str(required=True)
    quantity = fields.Int(required=True)
    weight = fields.Decimal(required=True)
    image_url = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)

class PlainCategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    parent_category_id = fields.Int(load_only=True)
    parent_category = fields.Nested(lambda: PlainCategorySchema(), dump_only=True)

class PlainMediaSchema(Schema):
# class MediaSchema(Schema):
    id = fields.Int(dump_only=True)
    url = fields.Str(required=True)
    media_type = fields.Str(required=True)
    alt_text = fields.Str()
    created_at = fields.DateTime(dump_only=True)


class BrandUpdateSchema(Schema):
    name = fields.Str()
    logo_url = fields.Str()


class ProductSchema(PlainProductSchema):
    brand_id = fields.Int(repuired=True, load_only=True)
    category_id = fields.Int(required=True, load_only=True)
    brand = fields.Nested(PlainBrandSchema(), dump_only=True)
    category = fields.Nested(PlainCategorySchema(), dump_only=True)
    media = fields.List(fields.Nested(PlainMediaSchema()), dump_only=True) # may let it be able to be loaded

class BrandSchema(PlainBrandSchema):
    products = fields.List(fields.Nested(PlainProductSchema()), dump_only=True)

class CategorySchema(PlainCategorySchema):
    products = fields.List(fields.Nested(PlainProductSchema()), dump_only=True)

class ProductUpdateSchema(Schema):
    name = fields.Str()
    description = fields.Str()
    price = fields.Decimal()
    sku = fields.Str()
    quantity = fields.Int()
    weight = fields.Decimal()
    image_url = fields.Str()
    brand_id = fields.Int()
    category_id = fields.Int()

class MediaSchema(PlainMediaSchema):
    # product_id = fields.Int(dump_only=True)
    product = fields.Nested(PlainProductSchema(), dump_only=True)

# class CategoryUpdateSchema(Schema):
#     name = fields.Str()
