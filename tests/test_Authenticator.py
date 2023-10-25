from authenticator import Authenticator
from user import User

user1 = User('Mike', 'Tyson', 'Danger', 'P1DG30NZ', 'petermcneely','Teacher',True)

user_list = [user1]

authenticator = Authenticator(user_list)
authenticator.users = user_list

assert authenticator.authenticate('Danger', 'P1DG30NZ') == user1
assert authenticator.authenticate('Danger', 'P1DG30N') == False

user2 = User('Evander', 'Holyfield', 'Ear', 'Yummy', 'petermcney','Teacher',False)
user_list2 = [user2]

authenticator2 = Authenticator(user_list2)
authenticator2.users = user_list2

assert authenticator.authenticate('Ear', 'Yummy') == False


