"""
Account API Service Test Suite

Test cases can be run with the following:
  nosetests -v --with-spec --spec-color
  coverage report -m
"""
import os
import logging
from unittest import TestCase
from tests.factories import AccountFactory
from service.common import status  # HTTP Status Codes
from service.models import db, Account, init_db
from service.routes import app
from service import talisman

DATABASE_URI = os.getenv(
    "DATABASE_URI", "postgresql://postgres:postgres@localhost:5432/postgres"
)

BASE_URL = "/accounts"

# To get the Flask test client to use https with the environ_overrides attribute.
# When making an URL call, pass environ_overrides=HTTPS_ENVIRON
HTTPS_ENVIRON = {'wsgi.url_scheme': 'https'}


######################################################################
#  T E S T   C A S E S
######################################################################
class TestAccountService(TestCase):
    """Account Service Tests"""

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
    #  H E L P E R   M E T H O D S
    ######################################################################

    def _create_accounts(self, count):
        """Factory method to create accounts in bulk"""
        accounts = []
        for _ in range(count):
            account = AccountFactory()
            response = self.client.post(BASE_URL, json=account.serialize())
            self.assertEqual(
                response.status_code,
                status.HTTP_201_CREATED,
                "Could not create test Account",
            )
            new_account = response.get_json()
            account.id = new_account["id"]
            accounts.append(account)
        return accounts

    ######################################################################
    #  A C C O U N T   T E S T   C A S E S
    ######################################################################

    def test_index(self):
        """It should get 200_OK from the Home Page"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_health(self):
        """It should be healthy"""
        resp = self.client.get("/health")
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertEqual(data["status"], "OK")

    def test_security_header(self):
        """Security: The header should contain security information"""
        response = self.client.get("/", environ_overrides=HTTPS_ENVIRON)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # For more information about the options of headers:
        # See Flask Talisman documentation
        headers = {
            'X-Frame-Options': 'SAMEORIGIN',
            'X-Content-Type-Options': 'nosniff',
            'Content-Security-Policy': 'default-src \'self\'; object-src \'none\'',
            'Referrer-Policy': 'strict-origin-when-cross-origin'
        }
        for key, value in headers.items():
            self.assertEqual(response.headers.get(key), value)

    def test_cors_policies(self):
        """Security: The header should contain the CORS policies"""
        response = self.client.get("/", environ_overrides=HTTPS_ENVIRON)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.headers.get("Access-Control-Allow-Origin"), "*")

    def test_create_account(self):
        """Create: It should Create a new Account"""
        account = AccountFactory()
        response = self.client.post(
            BASE_URL,
            json=account.serialize(),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Make sure location header is set
        location = response.headers.get("Location", None)
        self.assertIsNotNone(location)

        # Check the data is correct
        new_account = response.get_json()
        self.assertEqual(new_account["name"], account.name)
        self.assertEqual(new_account["email"], account.email)
        self.assertEqual(new_account["address"], account.address)
        self.assertEqual(new_account["phone_number"], account.phone_number)
        self.assertEqual(new_account["date_joined"], str(account.date_joined))

    def test_bad_request(self):
        """Create: It should not Create an Account when sending the wrong data"""
        response = self.client.post(BASE_URL, json={"name": "not enough data"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_unsupported_media_type(self):
        """Create: It should not Create an Account when sending the wrong media type"""
        account = AccountFactory()
        response = self.client.post(
            BASE_URL,
            json=account.serialize(),
            content_type="test/html"
        )
        self.assertEqual(response.status_code, status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

    def test_read_an_account(self):
        """Read: It should Read an Account"""
        account = self._create_accounts(1)[0]
        response = self.client.get(f"{BASE_URL}/{account.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check data is correct
        read_account = response.get_json()
        self.assertEqual(read_account["id"], account.id)
        self.assertEqual(read_account["name"], account.name)
        self.assertEqual(read_account["email"], account.email)
        self.assertEqual(read_account["address"], account.address)
        self.assertEqual(read_account["phone_number"], account.phone_number)
        self.assertEqual(read_account["date_joined"], str(account.date_joined))

    def test_read_account_not_found(self):
        """Read: It should return error status when no account could be read"""
        invalid_account_id = 0
        response = self.client.get(f"{BASE_URL}/{invalid_account_id}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_an_account(self):
        """Update: It should Update an Account"""
        account = self._create_accounts(1)[0]
        updated_data = {
            "name": "Test Update Account",
            "email": "max.mustermann@gmail.com",
            "address": "Wishes Street 65",
            "phone_number": "+45 XXX",
            "date_joined": "2024-12-15"
        }
        account.deserialize(updated_data)
        response = self.client.put(f"{BASE_URL}/{account.id}", json=account.serialize())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_json = response.get_json()
        updated_account = Account().deserialize(response_json)
        # Set ID separately because deserialize()
        # doesn't deserialize ID of account
        updated_account.id = response_json["id"]
        self.assertEqual(updated_account.id, account.id)
        self.assertEqual(updated_account.name, account.name)
        self.assertEqual(updated_account.email, account.email)
        self.assertEqual(updated_account.address, account.address)
        self.assertEqual(updated_account.phone_number, account.phone_number)
        self.assertEqual(updated_account.date_joined, account.date_joined)

    def test_update_account_not_found(self):
        """Update: It should return error status when no account could be found"""
        invalid_account_id = 0
        updated_data = {}
        response = self.client.put(f"{BASE_URL}/{invalid_account_id}", json=updated_data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_account_bad_request(self):
        """Update: It should not Update an Account when sending the wrong data"""
        account = self._create_accounts(1)[0]
        response = self.client.put(
            f"{BASE_URL}/{account.id}",
            json={"name": "not enough data"}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_account_unsupported_media_type(self):
        """Update: It should not Update an Account when sending the wrong media type"""
        account = AccountFactory()
        response = self.client.put(
            f"{BASE_URL}/{account.id}",
            json=account.serialize(),
            content_type="test/html"
        )
        self.assertEqual(response.status_code, status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

    def test_delete_account(self):
        """Delete: It should Delete an Account"""
        account = self._create_accounts(1)[0]
        response = self.client.delete(
            f"{BASE_URL}/{account.id}"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Data of response as text.
        # Otherwise, it returns 'b""' and not just '""'.
        self.assertEqual(response.get_data(as_text=True), "")
        self.assertEqual(Account.find(account.id), None)
        self.assertEqual(len(Account.all()), 0)

    def test_delete_account_not_found(self):
        """Delete: It should return error status when no account could be found"""
        invalid_account_id = 0
        response = self.client.delete(f"{BASE_URL}/{invalid_account_id}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_list_all_accounts(self):
        """List: It should List all Accounts"""
        account_count = 5
        self._create_accounts(account_count)
        response = self.client.get(f"{BASE_URL}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.get_json()
        self.assertEqual(len(response_data), account_count)

    def test_list_all_accounts_no_products_found(self):
        """List: It should return success status when no account could be found"""
        """
        Note: It is deliberately programmed so that no error code (e.g. 404)
          is sent, but a success code!
          It is not an error if nothing specific was searched for
          and nothing was found in an empty database.
        """
        response = self.client.get(f"{BASE_URL}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.get_json()), 0)
        # Just to be sure
        self.assertEqual(len(Account.all()), 0)
