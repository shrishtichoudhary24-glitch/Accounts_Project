"""Model tests"""
import unittest
from service import app
from service.models import Account, DataValidationError, db

DATA = {"name": "Jane Doe", "email": "jane@example.com", "address": "1 Main St", "phone_number": "555-1234"}


class TestAccountModel(unittest.TestCase):
    """Account model tests"""

    def setUp(self):
        db.session.query(Account).delete()
        db.session.commit()

    def tearDown(self):
        db.session.remove()

    def test_create_and_find(self):
        """Create then find"""
        account = Account().deserialize(DATA)
        account.create()
        self.assertIsNotNone(account.id)
        self.assertEqual(Account.find(account.id).name, "Jane Doe")
        self.assertEqual(len(Account.all()), 1)

    def test_update_and_delete(self):
        """Update then delete"""
        account = Account().deserialize(DATA)
        account.create()
        account.name = "Changed"
        account.update()
        self.assertEqual(Account.find(account.id).name, "Changed")
        account.delete()
        self.assertEqual(Account.all(), [])

    def test_update_no_id(self):
        """Update with no id fails"""
        account = Account().deserialize(DATA)
        self.assertRaises(DataValidationError, account.update)

    def test_serialize_repr(self):
        """Serialize and repr"""
        account = Account().deserialize(DATA)
        account.create()
        self.assertIn("Jane Doe", repr(account))
        self.assertEqual(account.serialize()["email"], "jane@example.com")

    def test_deserialize_errors(self):
        """Bad data"""
        self.assertRaises(DataValidationError, Account().deserialize, {"name": "x"})
        bad = dict(DATA, date_joined="not-a-date")
        self.assertRaises(DataValidationError, Account().deserialize, bad)
        self.assertRaises(DataValidationError, Account().deserialize, None)

    def test_app_loaded(self):
        """App exists"""
        self.assertIsNotNone(app)
