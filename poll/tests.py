from django.test import TestCase
from poll.models import Menu, Comment

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

class FillPageTest(TestCase):

    def test_uses_fill_template(self):
        response = self.client.get('/fill')
        self.assertTemplateUsed(response, 'fill.html')

    def test_can_display_a_POST_request(self):
        response = self.client.post('/fill', data={'f_food': 'value1', 'f_drink': 'value2'})
        self.assertIn('value1', response.content.decode())
        self.assertIn('value2', response.content.decode())

class AddPageTest(TestCase):
    
    def test_can_save_a_POST_request(self):
        menu = Menu.objects.create(name="Food")
        response = self.client.post('/add', data={'Food_Score': 3, 'Food_Comment': 'comment'})
        menu = Menu.objects.get(name="Food")
        self.assertEqual(menu.voted, 1)
        self.assertEqual(menu.total_score, 3)
        self.assertEqual(Comment.objects.count(), 1)
        comment = Comment.objects.first()
        self.assertEqual(comment.menu, menu)
        self.assertEqual(comment.text, 'comment')

    def test_redirects_after_POST(self):
        menu = Menu.objects.create(name="Food")
        response = self.client.post('/add', data={'Food_Score': 3, 'Food_Comment': 'comment'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/view')

class ViewPageTest(TestCase):

    def test_uses_view_template(self):
        response = self.client.get('/view')
        self.assertTemplateUsed(response, 'view.html')

class MenuAndCommentModelsTest(TestCase):

    def test_saving_and_retrieving_menu_and_comments(self):
        menu = Menu()
        menu.name = 'food'
        menu.Type = 'Food'
        menu.vote(3)
        menu.vote(4)
        menu.save()

        saved_menus = Menu.objects.all()
        self.assertEqual(saved_menus.count(), 1)

        first_saved_menu = saved_menus[0]
        self.assertEqual(first_saved_menu.name, 'food')
        self.assertEqual(first_saved_menu.Type, 'Food')
        self.assertEqual(first_saved_menu.voted, 2)
        self.assertEqual(first_saved_menu.total_score, 7)
        self.assertEqual(first_saved_menu.average, 3.5)
	
        first_comment = Comment.objects.create(menu = menu, text = "first comment")
        
        second_comment = Comment()
        second_comment.menu = menu
        second_comment.text = "second comment"
        second_comment.save()
        
        saved_comments = Comment.objects.all()
        self.assertEqual(saved_comments.count(), 2)

        first_saved_comment = saved_comments[0]
        second_saved_comment = saved_comments[1]
        self.assertEqual(first_saved_comment.menu, menu)
        self.assertEqual(first_saved_comment.text, "first comment")
        self.assertEqual(second_saved_comment.menu, menu)
        self.assertEqual(second_saved_comment.text, "second comment")
