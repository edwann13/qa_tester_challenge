import unittest
from sample_account import Customer

class TestSampleAccount(unittest.TestCase):
	"""Test Suite for Customer class"""

	def test_0_Withdraw(self):
		"""Test when we try to withdraw more than 
			our current balance.
			Expect the code to raise a RuntimeError
		"""
		user = createUser(0.0, "User")
		self.assertRaises(RuntimeError, user.withdraw, (1000.0))

	def test_1_Withdraw(self):
		"""Test when we try to withdraw more than 
			our current balance.
			Expect the code to raise a RuntimeError
		"""
		user = createUser(1000.0, "User")
		self.assertRaises(RuntimeError, user.withdraw, (1001.0))

	def test_2_Withdraw(self):
		""" Test that the corrent balance is returned"""
		user = createUser(170, "User")
		expected = 170 - 98.73
		result = user.withdraw(98.73)
		self.assertEqual(expected, result, "The Withdraw Balance is not correct.")

	def test_3_Withdraw(self):
		""" Test that the corrent balance is returned
			Withdraw twice
		"""
		user = createUser(57, "User")
		expected = 57 - 31.17
		expected = expected - 2.22

		user.withdraw(31.17)
		result = user.withdraw(2.22)
		self.assertEqual(expected, result, "The Withdraw Balance is not correct.")



	def test_0_Deposit(self):
		""" 
		Test deposit
		"""
		user = createUser(0.0, "User")
		expected = 100
		result = user.deposit(100)
		self.assertEqual(expected, result, "Wrong Balance returned.")

	def test_1_Deposit(self):
		""" 
		Test deposit
		"""
		user = createUser(100.0, "User")
		expected = 250.57
		result = user.deposit(150.57)
		self.assertEqual(expected, result, "Wrong Balance returned.")

	def test_2_Deposit(self):
		""" 
		Test deposit
		"""
		user = createUser(-1000.00, "User")
		expected = 0.0
		result = user.deposit(1000.00)

		self.assertEqual(expected, result, "Wrong Balance returned.")

	def test_3_Deposit(self):
		"""
		Test two deposits
		"""
		user = createUser(-1000.00, "User")
		user.deposit(1000.00)
		result = user.deposit(234.34)
		expected = 234.34

		self.assertEqual(expected, result, "Wrong Balance returned.")

		


def createUser(balance, name):
	"""Create a user with a given balance and name"""
	user = Customer(name)
	user.set_balance(balance)

	return user


if __name__ == '__main__':
    unittest.main()






