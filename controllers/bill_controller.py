class BillController(object):
	def __init__(self,billService):
		self.billService = billService
	
	def addBill(self,id,groupId,amount,contribution,paidBy):
		return self.billService.addBill(id,groupId,amount,contribution,paidBy)

	def getUserBalance(self,userId):
		balance = 0
		for billId in self.billService.billDetails:
			bill = self.billService.billDetails.get(billId)
			if userId in bill.getContribution():
				balance = balance - bill.getContribution().get(userId)
			if userId in bill.getPaidBy():
				balance = balance + bill.getPaidBy().get(userId)
		
		return balance



