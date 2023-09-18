
class User:

    def __init__(self,Username,Password,role):
        self.username=Username
        self.Password=Password
        self.role=role
admin_user=User("Admin","admin@123","Admin")
user=User("user","user@123","user")

def authenticate():
    username=input("Enter Username  :")
    password=input("Enter Password  :")

    if username == "Admin" and password == "admin@123":
        return admin_user
   
    elif username == "user" and password == "user@123":
        return user
    else:
        print("Invalid Input")
authenticate()

def for_admin(user):
    user.role=="Admin"

def for_user(user):
    user.role=="User"