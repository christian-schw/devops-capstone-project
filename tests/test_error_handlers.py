"""
Error Handlers Test Suite
"""
import os
import logging
from unittest import TestCase
from service.common import status
from service.models import db, Account, init_db
from service.routes import app
from service import talisman

DATABASE_URI = os.getenv(
    "DATABASE_URI", "postgresql://postgres:postgres@localhost:5432/postgres"
)

BASE_URL = "/accounts"


######################################################################
#  T E S T   C A S E S
######################################################################
class TestFlaskErrorHandler(TestCase):
    """Test Flask Error Handler"""

    @classmethod
    def setUpClass(cls):
        """Run once before all tests"""
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
        app.logger.setLevel(logging.CRITICAL)
        init_db(app)
        # Talisman will force all requests to your REST API to use the https:// protocol.
        # This is a good thing, except perhaps when testing (-> all tests will fail).
        talisman.force_https = False

    @classmethod
    def tearDownClass(cls):
        """Runs once before test suite"""

    def setUp(self):
        """Runs before each test"""
        db.session.query(Account).delete()  # clean up the last tests
        db.session.commit()

        self.client = app.test_client()

    def tearDown(self):
        """Runs once after each test case"""
        db.session.remove()

    ######################################################################
    # E R R O R   H A N D L E R   T E S T   C A S E S
    ######################################################################
    def test_request_validation_error(self):
        """It should handle value errors from bad data"""
        # Just use wrong data in json
        response = self.client.post(BASE_URL, json={"name": 45252})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_bad_request(self):
        """It should handle bad requests"""
        # Just use wrong data in json
        response = self.client.post(BASE_URL, json={"name": 45252})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_not_found(self):
        """It should handle resources not found"""
        # Common causes: Mistyped URLs or pages that are moved or deleted
        # without redirection
        response = self.client.get("/accjsadasounts")  # This URL looks good to me
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_method_not_allowed(self):
        """It should not allow an illegal method call"""
        # To cause this error use a HTTP method on an endpoint
        # that doesn't support that HTTP method.
        response = self.client.delete(f"{BASE_URL}")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_mediatype_not_supported(self):
        """It should handle unsupported media"""
        # To cause this use different type than allowed by HTTP method.
        response = self.client.post(
            BASE_URL,
            json={},
            content_type="test/html"
        )
        self.assertEqual(response.status_code, status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
