import bson
from marshmallow import fields, ValidationError


class ObjectId(fields.Field):
    """Custom marshmallow field for bson:ObjectId"""

    def _deserialize(self, value, attr, data, **kwargs):
        try:
            return bson.ObjectId(value)
        except (TypeError, bson.errors.InvalidId):
            raise ValidationError('Invalid ObjectId.')
