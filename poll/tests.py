from django.test import TestCase
from poll.models import Item

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

class FillPageTest(TestCase):

    def test_uses_fill_template(self):
        response = self.client.get('/fill')
        self.assertTemplateUsed(response, 'fill.html')

    def test_can_display_a_POST_request(self):
        response = self.client.post('/fill', data={'key1': 'value1', 'key2': 'value2'})
        self.assertIn('value1', response.content.decode())
        self.assertIn('value2', response.content.decode())

class AddPageTest(TestCase):
    pass
