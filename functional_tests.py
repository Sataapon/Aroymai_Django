from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_poll_vote_it_and_see_result(self):
        # While Pun eat "Gang curry" and "Keghuay" at new restaurant
        # She see sign Website about food poll 
        # When She finish eat food, She go to check out its homepage 
        self.browser.get('http://localhost:8000')

        # She see poll in title and header
        self.assertIn('poll', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('poll', header_text)

        ## She see food pictures with average score and number of vote
        # She select "Gang curry" picture
        select_food = self.browser.find_element_by_id('Gang curry')
        select_food.click()

        # She select "Keghuay" picture
        select_beverage = self.browser.find_element_by_id('Keghuay')
        select_beverage.click()

        # When she click Vote button, the page reload,
        submit = self.browser.find_element_by_id('Submit')
        submit.click()

        self.fail('Finish the test!')
        # and now the new page appear

        # She see only "Gang curry" and "Keghuay" picture with vote button and text box

        # She type "Very delicious" in text box and select "5" at vote buttun of "Gang curry" picture

        # She type "Sweet too much" in text box and select "4" at vote button of "Keghuay" picture 

        # When she click Send button, the page reload,
        # and now the new page appear

        # She see "Gang curry" with text "You vote: 5 score, comment: Very delicious"

        # She see "Keghuay" picture text "You vote: 4 score, comment: Sweet too much"

        # Satisfied, she paid and walked out of the restaurant

if __name__ == '__main__':
    unittest.main(warnings='ignore')
