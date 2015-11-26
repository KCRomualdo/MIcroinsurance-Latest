from django.test import TestCase
from branch.models import Branch

# Create your tests here.

class BranchModelTest(TestCase):

	def test_can_name_the_branch(self):
		branchName=Branch(title="My first branch")
		self.assertEqual(str(branchName),branchName.title)

	def test_can_make_a_new_branch_and_save_to_db(self):
		branch=Branch()
		#branch.id_number=1
		branch.branch_name="Cebuana-Pasig Branch"

		branch.save()

		branch_totalNum=Branch.objects.all()
		self.assertEquals(len(branch_totalNum),1)
		branch_firstEntry=branch_totalNum[0]
		self.assertEquals(branch_firstEntry,branch)

		#self.assertEquals(branch_firstEntry.id_number,1)
		self.assertEquals(branch_firstEntry.branch_name,"Cebuana-Pasig Branch")

	