from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create your tests here.

class InsuranceTest(StaticLiveServerTestCase):
	fixtures = ['admin_user.json']

	def setUp(self):
		self.browser=webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_add_a_new_branch_in_admin_side(self):
		self.browser.get(self.live_server_url + '/admin/')

		body=self.browser.find_element_by_tag_name('body')
		self.assertIn('Django administration', body.text)

		username_field=self.browser.find_element_by_name('username')
		username_field.send_keys('admin')

		password_field=self.browser.find_element_by_name('password')
		password_field.send_keys('admin')
		password_field.send_keys(Keys.RETURN)

		#self.browser.implicitly_wait(20)
		body=self.browser.find_element_by_tag_name('body')
		self.assertIn('Site administration', body.text)

		branch_res=self.browser.find_elements_by_link_text('Branches')
		self.assertEquals(len(branch_res),1)

		#self.fail('finish this test')
		branch_res[0].click()

		body=self.browser.find_element_by_tag_name('body')
		self.assertIn('0 Branches',body.text)

		new_branch=self.browser.find_element_by_link_text('Add branch')
		new_branch.click()

		body=self.browser.find_element_by_tag_name('body')
		self.assertIn('Branch name',body.text)