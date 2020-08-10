import abc
class UserServiceInterface(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def addUser(self,id,name):
		pass
