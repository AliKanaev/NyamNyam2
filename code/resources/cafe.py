from flask_restful import Resource
from models.cafe import CafeModel

class Cafe(Resource):
    def get(self, name):
        cafe = CafeModel.find_by_name(name)
        if cafe:
            return cafe.json()
        return {'message': 'Cafe not found'}, 404

    def post(self, name):
        if CafeModel.find_by_name(name):
            return {'message': "Cafe '{}' already exists".format(name)}, 400

        cafe = CafeModel(name)
        try:
            cafe.save_to_db()
        except:
            return {'message': 'An error occurred while creating the cafe'}, 500

        return cafe.json(), 201

    def delete(self, name):
        cafe = CafeModel.find_by_name(name)
        if cafe:
            cafe.delete_from_db()

        return {'message': 'Cafe deleted'}

class CafeList(Resource):
    def get(self):
        return {'cafe': list(map(lambda x: x.json(), CafeModel.query.all()))}
