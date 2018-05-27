from selenium import webdriver
import unittest
import time

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def find_and_click_item(self, id):
        select_item = self.browser.find_element_by_id(id)
        select_item.click()

    def find_and_send_key(self, id, key):
        select_item = self.browser.find_element_by_id(id)
        select_item.send_keys(key)

    def check_items_in_and_notIn_table(self, item1, item2, item3, item4, table):
        self.assertIn(item1, table)
        self.assertNotIn(item2, table)
        self.assertIn(item3, table)
        self.assertNotIn(item4, table)

    def check_review_in_table(self, comment, score, name, table):
        self.assertIn(comment, table)
        self.assertIn(score, table)
        self.assertIn(name, table)

    def test_can_start_a_poll_vote_it_and_see_result(self):
        # While Pun eat "Gangcurry" and "Keghuay" at new restaurant
        # She see sign Website about food survey
        # When She finish eat food, She go to check out its homepage
        self.browser.get('http://localhost:8000')

        # She see Aroymai in title and header
        self.assertIn('Aroymai', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Aroymai', header_text)

        # She select "Gangcurry"
        self.find_and_click_item('id_Gangcurry')

        # and she select "Keghuay"
        self.find_and_click_item('id_Keghuay')

        # When she click Vote button, the page reload
        self.find_and_click_item('id_Vote')
        time.sleep(1)

        # Now the new page appear
        # She see only "Gangcurry" and "Keghuay"
        table_fillpage = self.browser.find_element_by_tag_name('table').text
        self.check_items_in_and_notIn_table('Gangcurry', 'Gangsom', 'Keghuay', 'Namoi', table_fillpage)

        # She type "Very delicious" in comment box and fill "5" at vote box of "Gangcurry"
        self.find_and_send_key('id_Gangcurry_Comment', 'Very delicious')
        self.find_and_send_key('id_Gangcurry_Score', 5)

        # She type "Sweet too much" in text box and fill "4" at vote box of "Keghuay"
        self.find_and_send_key('id_Keghuay_Comment', 'Sweet too much')
        self.find_and_send_key('id_Keghuay_Score', 4)

        # She type "Pun" in Name box
        self.find_and_send_key('id_User', 'Pun')

        # When she click Send button, the page reload,
        self.find_and_click_item('id_Send')
        time.sleep(1)

        # Now the homepage page appear again
        # She select "Gangcurry" and "Keghuay" again
        self.find_and_click_item('id_Gangcurry')
        self.find_and_click_item('id_Keghuay')

        # And this time she click Review button, the page reload
        self.find_and_click_item('id_Review')
        time.sleep(1)

        # Now the new page appear
        # She see only "Gangcurry" and "Keghuay"
        table_reviewpage = self.browser.find_element_by_tag_name('table').text
        self.check_items_in_and_notIn_table('Gangcurry', 'Gangsom', 'Keghuay', 'Namoi', table_reviewpage)

        # She see "Very delicious", "5" and her name "Pun" in "Gangcurry" review
        self.check_review_in_table('Very delicious', '5', 'Pun', table_reviewpage)

        # She see "Sweet too much", "4" and her name "Pun" in "Keghuay" review
        self.check_review_in_table('Sweet too much', '4', 'Pun', table_reviewpage)

        # Satisfied, she paid and walked out of the restaurant
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
