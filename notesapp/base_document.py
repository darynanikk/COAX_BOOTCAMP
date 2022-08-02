from bson import ObjectId

from database import Database
from marshmallow.exceptions import ValidationError

database = Database().get_db()


class BaseDocument:
    meta = {}

    @classmethod
    def get_collection(cls):
        collection_name = cls.meta.get("collection", None)
        print(collection_name)

        if collection_name is None:
            raise ValidationError("No collection name provided")

        return database[collection_name]

    @classmethod
    def validate_schema(cls, **kwargs):
        try:
            schema = cls.meta.get("schema")
            return schema().load(kwargs)
        except ValidationError as error:
            print(error.messages)
            print(error.valid_data)
            raise Exception(error)

    @classmethod
    def create(cls, **kwargs):
        doc = cls.validate_schema(**kwargs)
        result = cls.get_collection().insert_one(doc)
        return cls.get(id=result.inserted_id)

    @classmethod
    def get(cls, **kwargs):
        if "id" in kwargs:
            kwargs["_id"] = (
                ObjectId(kwargs.pop("id")) if type(kwargs["id"]) is str else kwargs.pop("id")
            )
        result = cls.get_collection().find_one(kwargs)
        schema = cls.meta.get("schema")
        return schema().load(result)

    @classmethod
    def update(cls):
        pass

    @classmethod
    def delete(cls, note_id):
        cls.get_collection().delete_one({"_id": note_id})

    @classmethod
    def list(cls, *args, **kwargs):
        pass
