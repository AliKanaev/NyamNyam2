from db import db

class CafeModel(db.Model):
    __tablename__ = 'cafes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    managers = db.relationship('ManagerModel', lazy='dynamic') #if lazy='dynamic', managers is a query builder

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'managers': list(map(lambda x: x.json(), self.managers.all()))}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
