from selenium import webdriver
import unittest
import time

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

        # She see Aroymai in title and header
        self.assertIn('Aroymai', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Aroymai', header_text)

        ## She see food pictures with average score and number of vote
        # She select "Gang curry" picture
        select_food = self.browser.find_element_by_id('id_GangCurry')
        select_food.click()

        # She select "Keghuay" picture
        select_beverage = self.browser.find_element_by_id('id_KegHuay')
        select_beverage.click()

        # When she click Vote button, the page reload,
        vote = self.browser.find_element_by_id('id_vote')
        vote.click()
        time.sleep(3)

        # Now the new page appear
        # She see only "Gang curry" and "Keghuay" picture with vote button and text box
        table = self.browser.find_element_by_id('id_list_table')
        columns = table.find_elements_by_tag_name('td')
        ###self.assertIn('Gang curry', [column.text for column in columns])
        ###self.assertIn('Keghuay', [column.text for column in columns])
        ###self.assertNotIn('Gang som', [column.text for column in columns])

        # She type "Very delicious" in text box and select "5" at vote buttun of "Gang curry" picture
        commentfood = self.browser.find_element_by_id('id_GangCurry_comment')
        self.assertEqual(
            commentfood.get_attribute('placeholder'),
            'Enter comment'
        )
        commentfood.send_keys('Very delicious')
        scorefood = self.browser.find_element_by_id('id_GangCurry_score')
        scorefood.send_keys('5')

        # She type "Sweet too much" in text box and select "4" at vote button of "Keghuay" picture 
        commentdrinks = self.browser.find_element_by_id('id_KegHuay_comment')
        self.assertEqual(
            commentdrinks.get_attribute('placeholder'),
            'Enter comment'
        )
        commentdrinks.send_keys('Sweet too much')
        scoredrinks = self.browser.find_element_by_id('id_KegHuay_score')
        scoredrinks.send_keys('4')

        # When she click Send button, the page reload,
        send = self.browser.find_element_by_id('id_send')
        send.click()
        time.sleep(3)

        self.fail('Finish the test!')
        # Now the new page appear

        # She see "Gang curry" with text "You vote: 5 score, comment: Very delicious"

        # She see "Keghuay" picture text "You vote: 4 score, comment: Sweet too much"

        # Satisfied, she paid and walked out of the restaurant

if __name__ == '__main__':
    unittest.main(warnings='ignore')
