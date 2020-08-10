import sys
sys.path.append('/Users/spoylios/Desktop')
from splitwise.controllers.user_controller import UserController
from splitwise.controllers.group_controller import GroupController
from splitwise.controllers.bill_controller import BillController

from splitwise.services.bill_service import BillService
from splitwise.services.user_service import UserService
from splitwise.services.group_service import GroupService

userController = UserController(UserService())
groupController = GroupController(GroupService())
billController = BillController(BillService())


user1 = userController.addUser('user1','pawan')
user2 = userController.addUser('user2','gyan')
user3 = userController.addUser('user3','abhi')
user4 = userController.addUser('user4','nishant')
user5 = userController.addUser('user5','ds')

members = [user1,user2,user3,user4,user5]
group1 = groupController.addGroup('group1','avengers',members)

#print (group1.getMembers())
paidBy = {'user1':200,'user2':100,'user3':50,'user4':50,'user5':100}
contribution = {'user1':100,'user2':100,'user3':100,'user4':100,'user5':100}

bill1 = billController.addBill('bill1','group1',500,contribution,paidBy)

balance = billController.getUserBalance('user1')
print (balance)