from django.http import response
from django.test import SimpleTestCase

class SimpleTestCase(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        # checking if the status code for each page is 200
        self.assertEqual(response.status_code,200)
    

    def test_about_page_status_code(self):
        response= self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
