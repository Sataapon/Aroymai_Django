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
        vote = self.browser.find_element_by_id('id_Vote')
        vote.click()
        time.sleep(3)

        # Now the new page appear
        # She see only "Gang curry" and "Keghuay" picture with vote button and text box
        table_info = self.browser.find_element_by_tag_name('table').text
        self.assertIn('GangCurry', table_info)
        self.assertNotIn('GangSom', table_info)
        self.assertIn('KegHuay', table_info)
        self.assertNotIn('NamOi', table_info)

        # She type "Very delicious" in text box and select "5" at vote buttun of "Gang curry" picture
        commentfood = self.browser.find_element_by_id('id_GangCurry_Comment')
        self.assertEqual(
            commentfood.get_attribute('placeholder'),
            'Enter comment'
        )
        commentfood.send_keys('Very delicious')
        scorefood = self.browser.find_element_by_id('id_GangCurry_Score')
        scorefood.send_keys('5')

        # She type "Sweet too much" in text box and select "4" at vote button of "Keghuay" picture 
        commentdrinks = self.browser.find_element_by_id('id_KegHuay_Comment')
        self.assertEqual(
            commentdrinks.get_attribute('placeholder'),
            'Enter comment'
        )
        commentdrinks.send_keys('Sweet too much')
        scoredrinks = self.browser.find_element_by_id('id_KegHuay_Score')
        scoredrinks.send_keys('4')

        # When she click Send button, the page reload,
        send = self.browser.find_element_by_id('id_Send')
        send.click()
        time.sleep(3)

        # Now the new page appear
        # She see "Gang curry" with text "You vote: 5 points, comment: Very delicious"
        table_result = self.browser.find_element_by_tag_name('table').text
        self.assertIn('GangCurry', table_result)
        self.assertIn('Your vote: 5 points', table_result)
        self.assertIn('Your comment: Very delicious', table_result)
        # She see "Keghuay" with text "You vote: 4 points, comment: Sweet too much"
        self.assertIn('KegHuay', table_result)
        self.assertIn('Your vote: 4 points', table_result)
        self.assertIn('Your comment: Sweet too much', table_result)

        # Satisfied, she paid and walked out of the restaurant
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
