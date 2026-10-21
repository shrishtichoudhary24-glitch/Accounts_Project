"""Route tests"""
import unittest
from service import app, talisman
from service.models import Account, db

BASE_URL = "/accounts"
HTTPS_ENVIRON = {"wsgi.url_scheme": "https"}
DATA = {"name": "Jane Doe", "email": "jane@example.com", "address": "1 Main St", "phone_number": "555-1234"}


class TestAccountService(unittest.TestCase):
    """Account service tests"""

    @classmethod
    def setUpClass(cls):
        talisman.force_https = False

    def setUp(self):
        db.session.query(Account).delete()
        db.session.commit()
        self.client = app.test_client()

    def tearDown(self):
        db.session.remove()

    def _create(self):
        resp = self.client.post(BASE_URL, json=DATA)
        self.assertEqual(resp.status_code, 201)
        return resp.get_json()

    def test_index_and_health(self):
        """Index and health"""
        self.assertEqual(self.client.get("/").status_code, 200)
        resp = self.client.get("/health")
        self.assertEqual(resp.get_json()["status"], "OK")

    def test_create_account(self):
        """Create"""
        resp = self.client.post(BASE_URL, json=DATA)
        self.assertEqual(resp.status_code, 201)
        self.assertIsNotNone(resp.headers.get("Location"))
        self.assertEqual(resp.get_json()["name"], "Jane Doe")

    def test_create_bad_data_and_media_type(self):
        """Create errors"""
        self.assertEqual(self.client.post(BASE_URL, json={"name": "x"}).status_code, 400)
        resp = self.client.post(BASE_URL, data="x", content_type="text/plain")
        self.assertEqual(resp.status_code, 415)
        self.assertEqual(self.client.post(BASE_URL).status_code, 415)

    def test_list_accounts(self):
        """List"""
        self._create()
        self._create()
        resp = self.client.get(BASE_URL)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.get_json()), 2)

    def test_read_account(self):
        """Read"""
        acct = self._create()
        resp = self.client.get(f"{BASE_URL}/{acct['id']}")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json()["email"], "jane@example.com")

    def test_read_not_found(self):
        """Read 404"""
        self.assertEqual(self.client.get(f"{BASE_URL}/0").status_code, 404)

    def test_update_account(self):
        """Update"""
        acct = self._create()
        acct["name"] = "New Name"
        resp = self.client.put(f"{BASE_URL}/{acct['id']}", json=acct)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json()["name"], "New Name")

    def test_update_not_found(self):
        """Update 404"""
        self.assertEqual(self.client.put(f"{BASE_URL}/0", json=DATA).status_code, 404)

    def test_delete_account(self):
        """Delete"""
        acct = self._create()
        self.assertEqual(self.client.delete(f"{BASE_URL}/{acct['id']}").status_code, 204)
        self.assertEqual(self.client.get(f"{BASE_URL}/{acct['id']}").status_code, 404)

    def test_method_not_allowed(self):
        """405"""
        self.assertEqual(self.client.delete(BASE_URL).status_code, 405)


class TestSecurity(unittest.TestCase):
    """Security headers and CORS tests"""

    @classmethod
    def setUpClass(cls):
        talisman.force_https = True

    @classmethod
    def tearDownClass(cls):
        talisman.force_https = False

    def setUp(self):
        self.client = app.test_client()

    def test_security_headers(self):
        """Talisman headers present"""
        resp = self.client.get("/", environ_overrides=HTTPS_ENVIRON)
        self.assertEqual(resp.status_code, 200)
        headers = {
            "X-Frame-Options": "SAMEORIGIN",
            "X-Content-Type-Options": "nosniff",
            "Content-Security-Policy": "default-src 'self'; object-src 'none'",
            "Referrer-Policy": "strict-origin-when-cross-origin",
        }
        for key, value in headers.items():
            self.assertEqual(resp.headers.get(key), value)

    def test_cors_header(self):
        """CORS header present"""
        resp = self.client.get("/", environ_overrides=HTTPS_ENVIRON)
        self.assertEqual(resp.headers.get("Access-Control-Allow-Origin"), "*")
