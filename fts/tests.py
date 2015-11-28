from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from Microinsurance_Maintenance.models import Underwriter

# Create your tests here.

class InsuranceTest(StaticLiveServerTestCase):
	fixtures = ['admin_user.json']

	def setUp(self):
		self.browser=webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def get_browser_for_test(self):

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

	def test_can_add_a_new_branch_in_admin_side(self):

		self.get_browser_for_test()

		branch_link=self.browser.find_elements_by_link_text('Branches')
		self.assertEquals(len(branch_link),1)

		#self.fail('finish this test')
		branch_link[0].click()

		body=self.browser.find_element_by_tag_name('body')
		self.assertIn('0 Branches',body.text)

		new_branch=self.browser.find_element_by_link_text('Add branch')
		new_branch.click()

		body=self.browser.find_element_by_tag_name('body')
		self.assertIn('Branch name',body.text)

		branchName_field=self.browser.find_element_by_name('branch_name')
		branchName_field.send_keys('Cebuana-Cainta Branch')
		branchAdd_field=self.browser.find_element_by_name('branch_address')
		branchAdd_field.send_keys('San Andres,Cainta Rizal')
		#branchName_field.send_keys(Keys.RETURN)

		save_btn=self.browser.find_element_by_css_selector("input[value='Save']")
		save_btn.click()

		save_branch=self.browser.find_elements_by_link_text("Cebuana-Cainta Branch")
		self.assertEquals(len(save_branch),1)

		#self.fail('finish the test')		

	def test_can_save_a_new_underwriter_in_admin(self):

		self.get_browser_for_test()

		underwriter_link=self.browser.find_elements_by_link_text('Underwriters')
		self.assertEquals(len(underwriter_link),1)

		underwriter_link[0].click()

		body=self.browser.find_element_by_tag_name('body')
		self.assertIn('0 underwriter',body.text)

		new_underwriter=self.browser.find_element_by_link_text('Add underwriter')
		new_underwriter.click()

		body=self.browser.find_element_by_tag_name('body')
		self.assertIn('Underwriter name',body.text)

		underwriterName_field=self.browser.find_element_by_name('underwriter_name')
		underwriterName_field.send_keys('Prolife')
		underwriterContactNo_field=self.browser.find_element_by_name('underwriter_ContactNo')
		underwriterContactNo_field.send_keys('910-1901')
		underwriterAdd_field=self.browser.find_element_by_name('underwriter_address')
		underwriterAdd_field.send_keys('Cainta,Rizal')

		save_btn=self.browser.find_element_by_css_selector("input[value='Save']")
		save_btn.click()

		save_underwriter=self.browser.find_elements_by_link_text('Prolife')
		self.assertEquals(len(save_underwriter),1)

		#self.fail('finish the test')

	#def test_can_save_a_new_insurance_offer_in_admin(self):
		
		#self.get_browser_for_test()

		home_link=self.browser.find_element_by_link_text('Home')
		home_link.click()

		insurance_offer_link=self.browser.find_elements_by_link_text('Insurance offers')
		self.assertEquals(len(insurance_offer_link),1)
		insurance_offer_link[0].click()

		body=self.browser.find_element_by_tag_name('body')
		self.assertIn('0 insurance offers',body.text)

		new_insurance=self.browser.find_element_by_link_text('Add insurance offer')
		new_insurance.click()

		body=self.browser.find_element_by_tag_name('body')
		self.assertIn('SKU name',body.text)

		sku_field=self.browser.find_element_by_name('SKU_name')
		sku_field.send_keys('Sample Insurance')
		baseamount_field=self.browser.find_element_by_name('base_price')
		baseamount_field.send_keys(10)
		sellingamount_field=self.browser.find_element_by_name('selling_price')
		sellingamount_field.send_keys(15)
		validdays_field=self.browser.find_element_by_name('Valid_days')
		validdays_field.send_keys(30)
		agefrom_field=self.browser.find_element_by_name('Age_range_from')
		agefrom_field.send_keys(18)
		ageto_field=self.browser.find_element_by_name('Age_range_to')
		ageto_field.send_keys(75)
		limit_field=self.browser.find_element_by_name('Limit_per_person')
		limit_field.send_keys(3)
		underwriter_field=self.browser.find_element_by_name('Underwriter_name')
		underwriter_field.send_keys('Prolife')

		save_btn=self.browser.find_element_by_css_selector("input[value='Save']")
		save_btn.click()
		save_insurance=self.browser.find_elements_by_link_text("Sample Insurance")
		self.assertEquals(len(save_insurance),1)

		#self.fail('finish the test')

