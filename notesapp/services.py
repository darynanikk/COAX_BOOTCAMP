from model import NoteModel


class NoteService:
    @staticmethod
    def create(film_name: str, note: str, rating: int):
        params = dict()
        if film_name and note and rating:
            params['film_name'] = film_name
            params['note'] = note
            params['rating'] = rating
        else:
            raise Exception

        data = NoteModel.create(**params)
        return {'result': data, 'error': None}

    @staticmethod
    def get(note_id):
        try:
            data = NoteModel.get(id=note_id)
            return {"result": data, "error": None}
        except Exception as ex:
            return {"result": None, "error": ex}
