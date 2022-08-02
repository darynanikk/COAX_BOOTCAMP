from marshmallow import Schema
from marshmallow.fields import Str, Int

from tasks.notesapp.custom_field import ObjectId
from tasks.notesapp.database import Database
from base_document import BaseDocument


class NoteSchema(Schema):
    _id = ObjectId(load_only=True)
    film_name = Str(required=True)
    note = Str(required=True)
    rating = Int(required=True)


class NoteModel(BaseDocument):
    db = Database().get_db()
    meta = {
        "collection": "notes",
        "schema": NoteSchema,
    }
