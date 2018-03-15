from django.test import TestCase
from poll.models import Menu,Comment

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

    def test_saving_and_retrieving_menus(self):
        first_menu = Menu()
        first_menu.name = 'GangCurry'
        first_menu.type = 'Food'
        first_menu.save()

        second_menu = Menu()
        second_menu.name = 'GangSom'
        second_menu.type = 'Food'
        second_menu.save()

        thrid_menu = Menu()
        thrid_menu.name = 'KegHuay'
        thrid_menu.type = 'Drink'
        thrid_menu.save()

        fourth_menu = Menu()
        fourth_menu.name = 'NamOi'
        fourth_menu.type = 'Drink'
        fourth_menu.save()

        saved_menus = Menu.objects.all()
        self.assertEqual(saved_menus.count(), 4)

        first_saved_menu = saved_menus[0]
        second_saved_menu = saved_menus[1]
        thrid_saved_menu = saved_menus[2]
        fourth_saved_menu = saved_menus[3]
        self.assertEqual(first_saved_menu.name, 'GangCurry')
        self.assertEqual(first_saved_menu.type, 'Food')
        self.assertEqual(second_saved_menu.name, 'GangSom')
        self.assertEqual(second_saved_menu.type, 'Food')
        self.assertEqual(thrid_saved_menu.name, 'KegHuay')
        self.assertEqual(thrid_saved_menu.type, 'Drink')
        self.assertEqual(fourth_saved_menu.name, 'NamOi')
        self.assertEqual(fourth_saved_menu.type, 'Drink')
