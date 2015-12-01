from django.test import TestCase
from Microinsurance_Maintenance.models import Branch,InsuranceOffer,Underwriter,UserType,User

# Create your tests here.

class BranchModelTest(TestCase):

	def test_can_make_a_new_branch_and_save_to_db(self):
		branch=Branch()
		#branch.id_number=1
		branch.branch_name="Cebuana-Rizal Branch"
		branch.branch_address="Cainta,Rizal"

		branch.save()

		branch_totalNum=Branch.objects.all()
		self.assertEquals(len(branch_totalNum),1)
		branch_firstEntry=branch_totalNum[0]
		self.assertEquals(branch_firstEntry,branch)

		#self.assertEquals(branch_firstEntry.id_number,1)
		self.assertEquals(branch_firstEntry.branch_name,"Cebuana-Rizal Branch")
		self.assertEquals(branch_firstEntry.branch_address,"Cainta,Rizal")

class UnderwriterModelTest(TestCase):

	def test_can_make_a_new_underwriter_and_save_to_db(self):
		under_writer=Underwriter()
		under_writer.underwriter_name="Prolife"
		under_writer.underwriter_ContactNo="674-8192"
		under_writer.underwriter_address="Cainta,Rizal"

		under_writer.save()

		under_writer_total=Underwriter.objects.all()
		self.assertEquals(len(under_writer_total),1)
		under_writer_firstEntry=under_writer_total[0]
		self.assertEquals(under_writer_firstEntry,under_writer)

		self.assertEquals(under_writer_firstEntry.underwriter_name,"Prolife")
		self.assertEquals(under_writer_firstEntry.underwriter_ContactNo,"674-8192")
		self.assertEquals(under_writer_firstEntry.underwriter_address,"Cainta,Rizal")


class InsuranceModelTest(TestCase):

	def test_can_make_a_new_insurance_offer_and_save_to_db(self):

		insuranceOff=InsuranceOffer()
		insuranceOff.SKU_name="Car insurance"
		insuranceOff.base_price=25
		insuranceOff.selling_price=30
		insuranceOff.Valid_days=30
		insuranceOff.Age_range_from=18
		insuranceOff.Age_range_to=75
		insuranceOff.Limit_per_person=3
		insuranceOff.Underwriter_name=Underwriter.objects.create(underwriter_name='Prolife')

		insuranceOff.save()

		all_insurance_in_db=InsuranceOffer.objects.all()
		self.assertEquals(len(all_insurance_in_db),1)
		only_insurance_in_db=all_insurance_in_db[0]
		self.assertEquals(only_insurance_in_db,insuranceOff)

		self.assertEquals(only_insurance_in_db.SKU_name,'Car insurance')
		self.assertEquals(only_insurance_in_db.base_price,25)
		self.assertEquals(only_insurance_in_db.selling_price,30)
		self.assertEquals(only_insurance_in_db.Valid_days,30)
		self.assertTrue(only_insurance_in_db.Age_range_from,18)
		self.assertTrue(only_insurance_in_db.Age_range_to,75)
		self.assertEquals(only_insurance_in_db.Limit_per_person,3)
		self.assertEquals(Underwriter.objects.filter(underwriter_name='Prolife').count(),1)

class UserTypeModelTest(TestCase):

	def test_can_make_a_new_type_and_save_to_db(self):

		userType=UserType()
		userType.userTypeName="Branch Manager"

		userType.save()

		all_types_in_db=UserType.objects.all()
		self.assertEquals(len(all_types_in_db),1)
		only_type_in_db=all_types_in_db[0]
		self.assertEquals(only_type_in_db,userType)

		self.assertEquals(only_type_in_db.userTypeName,'Branch Manager')

class UserModelTest(TestCase):

	def test_can_make_a_new_personel_and_save_to_db(self):

		user=User()
		user.firstName="Ana"
		user.midName=""
		user.lastName="Batumbakal"
		user.contactNo="09182091018"
		user.emailAdd="admin@example.com"
		user.user_branch=Branch.objects.create(branch_name='Pasig Branch')
		user.user_ptype=UserType.objects.create(userTypeName='Branch Manager')
		user.user_uname="anaba"
		user.user_pword="anaba"

		user.save()

		all_user_in_db=User.objects.all()
		self.assertEquals(len(all_user_in_db),1)
		only_user_in_db=all_user_in_db[0]
		self.assertEquals(only_user_in_db,user)

		self.assertEquals(only_user_in_db.firstName,'Ana')
		self.assertEquals(only_user_in_db.midName,'')
		self.assertEquals(only_user_in_db.lastName,'Batumbakal')
		self.assertEquals(only_user_in_db.contactNo,'09182091018')
		self.assertEquals(only_user_in_db.emailAdd,'admin@example.com')
		self.assertEquals(Branch.objects.filter(branch_name='Pasig Branch').count(),1)
		self.assertEquals(UserType.objects.filter(userTypeName='Branch Manager').count(),1)
		self.assertEquals(only_user_in_db.user_uname,'anaba')
		self.assertEquals(only_user_in_db.user_pword,'anaba')

#class PromoModelTest(TestCase):

#	def test_can_make_a_new_promo_and_save_to_db(self):

