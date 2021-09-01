from django.http import response
from django.test import TestCase,SimpleTestCase

# Create your tests here.
class SimpleTest(SimpleTestCase):
    def test_home_page_status(seft):
        response = seft.client.get("/")
        seft.assertEquals(response.status_code, 200)