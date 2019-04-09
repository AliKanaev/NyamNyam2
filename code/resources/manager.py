from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.manager import ManagerModel

class Manager(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('cafe_id',
        type=int,
        required=True,
        help="Every manager needs a cafe id."
    )

    def get(self, name):
        manager = ManagerModel.find_by_name(name)
        if manager:
            return manager.json()
        return {'message': 'Managers not found'}, 404

    @jwt_required()
    def post(self, name):
        if ManagerModel.find_by_name(name):
            return {'message': "A manager with name '{}' already exists.".format(name)}, 400

        data = Manager.parser.parse_args()

        manager = ManagerModel(name, **data) # (name, data['name'], data['school_id'])

        try:
            manager.save_to_db()
        except:
            return {'message': 'An error ocurred inserting the manager.'}, 500

        return manager.json(), 201

    @jwt_required()
    def delete(self, name):
        manager = ManagerModel.find_by_name(name)
        if manager:
            manager.delete_from_db()

        return {'message': 'Manager deleted'}

class ManagerList(Resource):
    def get(self):
        return {'managers': list(map(lambda x: x.json(), ManagerModel.query.all()))}
