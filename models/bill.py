class Bill(object):
	def __init__(self):
		self.id = None
		self.groupId = None
		self.amount = None
		self.contribution = {}
		self.paidBy = {}

	def setId(self,id):
		self.id = id

	def getId(self):
		return self.id

	def setGroupId(self,groupId):
		self.groupId = groupId

	def getGroupId(self):
		return self.groupId

	def setAmount(self,amount):
		self.amount = amount

	def getAmount(self):
		return self.amount

	def setContribution(self,contribution):
		self.contribution = contribution

	def getContribution(self):
		return self.contribution

	def setPaidBy(self,paidBy):
		self.paidBy = paidBy

	def getPaidBy(self):
		return self.paidBy


	
