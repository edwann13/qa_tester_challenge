import unittest
from sample_account import Customer

class TestSampleAccount(unittest.TestCase):



	def test_Name(self):
		account = Customer("James")
		money = 10
		account.set_balance(10)
		self.assertEqual(money, account.withdraw(0))



if __name__ == '__main__':
    unittest.main()