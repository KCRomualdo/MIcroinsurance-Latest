from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create your tests here.

class InsuranceTest(LiveServerTestCase):
	fixtures = ['admin_user.json']

	def setUp(self):
		self.browser=webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_add_a_new_branch_in_admin_side(self):
		self.browser.get(self.live_server_url + '/admin/')

		body=self.browser.find_element_by_tag_name('body')
		self.assertIn('Django administration',body.text)

		f_user=self.browser.find_element_by_name('username')
		f_user.send_keys('admin')

		f_pword=self.browser.find_element_by_name('password')
		f_pword.send_keys('krista')
		f_pword.send_keys(Keys.ENTER)

		body=self.browser.find_element_by_tag_name('body')
		self.assertIn('Site administration',body.text)

		branch_res=self.browser.find_element_by_link_text('Branch')
		self.assertEquals(len(branch_res),2)

		self.fail('finish this test')