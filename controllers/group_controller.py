class GroupController(object):
	def __init__(self,groupService):
		self.groupService = groupService
	def addGroup(self,id,name,members):
		return self.groupService.addGroup(id,name,members)