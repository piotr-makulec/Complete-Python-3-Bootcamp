class Account:
	def __init__(self, owner, balance):
		self.owner = owner
		self.balance = balance

	def __str__(self):
		return "Account owner:\t\t{}\nAccount balance:\t${}".format(self.owner, self.balance)

	def deposit(self, amount):
		self.balance += amount
		print("Deposit accepted")

	def withdraw(self, amount):
		if amount <= self.balance:
			self.balance -= amount
			print("Withdrawal accepted")
		else:
			print("Funds unavailable")

acct1 = Account("Jose", 100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
print(acct1)
acct1.withdraw(75)
print(acct1)
acct1.withdraw(500)
print(acct1)