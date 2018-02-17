from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_poll_vote_it_and_see_result(self):
        # While Pun eat food at new restaurant
        # She see sign Website about food poll 
        # When She finish eat food, She go to check out its homepage 
        self.browser.get('http://localhost:8000')

        # She see poll in title and header
        self.assertIn('poll', self.browser.title)
        self.fail('Finish the test!')

        # She select food and beverage pictures

        # When she click Vote button, the page reload,
        # and now the new page appear

        # She see pictures that she select with text box and score button

        # She comment text box, select score button

        # When she click Send button, the page reload,
        # and now the new page appear

        # She see picture with average score and number of votes

        # Satisfied, she paid and walked out of the restaurant

if __name__ == '__main__':
    unittest.main(warnings='ignore')
