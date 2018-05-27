from django.test import TestCase
from poll.models import Menu, CommentScore, User

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_display_Menu_model(self):
        Menu.objects.create(name="Gangcurry", Type="Food")
        Menu.objects.create(name="Keghuay", Type="Drink")
        response = self.client.get('/')
        self.assertIn("Gangcurry", response.content.decode())
        self.assertIn("Keghuay", response.content.decode())

class FillPageTest(TestCase):

    def test_uses_fill_template(self):
        response = self.client.get('/fill')
        self.assertTemplateUsed(response, 'fill.html')

    def test_can_display_a_GET_request(self):
        response = self.client.get('/fill', data={'Food_Gangcurry': 'Gangcurry', 'Food_Keghauy': 'Keghuay'})
        self.assertIn('Gangcurry', response.content.decode())
        self.assertIn('Keghuay', response.content.decode())

class AddPageTest(TestCase):

    def test_can_save_a_POST_request(self):
        menu = Menu.objects.create(name='Gangcurry', Type='Food')
        response = self.client.post('/add', data={'Gangcurry_comment': 'comment', 'Gangcurry_score': 3, 'User': 'Pun'})
        saved_user = User.objects.get(name = 'Pun')
        saved_commentscore = CommentScore.objects.get(menu = menu)
        self.assertEqual(saved_commentscore.menu, menu)
        self.assertEqual(saved_commentscore.user, saved_user)
        self.assertEqual(saved_commentscore.comment, 'comment')
        self.assertEqual(saved_commentscore.score, 3)

    def test_redirects_after_POST(self):
        menu = Menu.objects.create(name='Gangcurry', Type='Food')
        response = self.client.post('/add', data={'Gangcurry_comment': 'comment', 'Gangcurry_score': 3, 'User': 'Pun'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

class ReviewPageTest(TestCase):

    def test_uses_review_template(self):
        response = self.client.get('/review')
        self.assertTemplateUsed(response, 'review.html')

    def test_can_display_a_GET_request(self):
        response = self.client.get('/fill', data={'Food_Gangcurry': 'Gangcurry', 'Food_Keghauy': 'Keghuay'})
        self.assertIn('Gangcurry', response.content.decode())
        self.assertIn('Keghuay', response.content.decode())

class AboutPageTest(TestCase):

    def test_uses_about_template(self):
        response = self.client.get('/about')
        self.assertTemplateUsed(response, 'about.html')

class ModelsTest(TestCase):

    def test_saving_and_retrieving_menu_commentscores_and_user(self):
        menu = Menu.objects.create(name='Gangcurry', Type='Food')
        saved_menus = Menu.objects.all()
        self.assertEqual(saved_menus.count(), 1)
        first_saved_menu = saved_menus[0]
        self.assertEqual(first_saved_menu.name, 'Gangcurry')
        self.assertEqual(first_saved_menu.Type, 'Food')

        user = User.objects.create(name='Pun')
        saved_users = User.objects.all()
        self.assertEqual(saved_users.count(), 1)
        first_saved_user = saved_users[0]
        self.assertEqual(first_saved_user.name, 'Pun')

        first_commentscore = CommentScore.objects.create(menu = menu, user = user, comment = 'first comment', score = 1)
        second_commentscore = CommentScore.objects.create(menu = menu, user = user, comment = 'second comment', score = 2)
        saved_commentscores = CommentScore.objects.all()
        self.assertEqual(saved_commentscores.count(), 2)
        first_saved_commentscore = saved_commentscores[0]
        second_saved_commentscore = saved_commentscores[1]
        self.assertEqual(first_saved_commentscore.menu, menu)
        self.assertEqual(first_saved_commentscore.user, user)
        self.assertEqual(first_saved_commentscore.comment, 'first comment')
        self.assertEqual(first_saved_commentscore.score, 1)
        self.assertEqual(second_saved_commentscore.menu, menu)
        self.assertEqual(second_saved_commentscore.user, user)
        self.assertEqual(second_saved_commentscore.comment, 'second comment')
        self.assertEqual(second_saved_commentscore.score, 2)
