"""Account model"""
import logging
from datetime import date
from flask_sqlalchemy import SQLAlchemy

logger = logging.getLogger("flask.app")
db = SQLAlchemy()


def init_db(app):
    """Bind db to app and create tables"""
    db.init_app(app)
    app.app_context().push()
    db.create_all()


class DataValidationError(Exception):
    """Invalid data"""


class Account(db.Model):
    """Customer account"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    address = db.Column(db.String(256), nullable=False)
    phone_number = db.Column(db.String(32), nullable=True)
    date_joined = db.Column(db.Date(), nullable=False, default=date.today)

    def __repr__(self):
        return f"<Account {self.name} id=[{self.id}]>"

    def create(self):
        """Create account"""
        db.session.add(self)
        db.session.commit()

    def update(self):
        """Update account"""
        if not self.id:
            raise DataValidationError("Update called with empty ID field")
        db.session.commit()

    def delete(self):
        """Delete account"""
        db.session.delete(self)
        db.session.commit()

    def serialize(self):
        """To dict"""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "address": self.address,
            "phone_number": self.phone_number,
            "date_joined": self.date_joined.isoformat(),
        }

    def deserialize(self, data):
        """From dict"""
        try:
            self.name = data["name"]
            self.email = data["email"]
            self.address = data["address"]
            self.phone_number = data.get("phone_number")
            if data.get("date_joined"):
                self.date_joined = date.fromisoformat(data["date_joined"])
        except KeyError as error:
            raise DataValidationError("Invalid Account: missing " + error.args[0]) from error
        except (TypeError, ValueError) as error:
            raise DataValidationError("Invalid Account: bad data - " + str(error)) from error
        return self

    @classmethod
    def all(cls):
        """All accounts"""
        return cls.query.all()

    @classmethod
    def find(cls, account_id):
        """Find by id"""
        return cls.query.get(account_id)
