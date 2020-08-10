from splitwise.services.group_service_interface import GroupServiceInterface
from splitwise.models.group import Group

class GroupService(GroupServiceInterface):
	groupDetails = {}
	def addGroup(self,id,name,members):
		group = Group()
		group.setId(id)
		group.setName(name)
		group.setMembers(members)
		
		self.__class__.groupDetails[id] = group
		return group


