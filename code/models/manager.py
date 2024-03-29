from db import db


class ManagerModel(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    cafe_id = db.Column(db.Integer, db.ForeignKey('cafes.id'))
    cafe = db.relationship('CafeModel')

    def __init__(self, name, cafe_id):
        self.name = name
        self.cafe_id = cafe_id

    def json(self):
        return {'name': self.name, 'cafe': self.cafe.name}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
