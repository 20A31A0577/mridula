from user import Userclass  
class login:
    __db = []
    def ___init__(self):
        self.print_menu()
    def print_menu(self):
        print("welcome user")
        print("1.register")
        print("2.login")
        print("3.exit")
    def create_user(self,name,email,password):
        new_user = Userclass(name,email,password)
        self.__db.append(new_user)
        print(self.__db)
        return True
    def validate_user(self,email,password):
        temp=self.__db.copy()
        for user_obj in temp:
            if email == user_obj.email:
                if password == user_obj.get_user_password():
                    return True
                else:
                    return False
obj = login()
while True:
    option = input("enter your choice")
    if option == '1':
        name = input("enter your full name:")
        email= input("enter email")
        password = input("enter new password")
        res=obj.create_user(name,email,password)
        if res == True:
            print("user created succesfully")
    elif option == '2':
        email = input("enter email")
        password= input("enter password")
        if obj.validate_user(email,password):
            print("login success")
        else:
            print("login failed")
    elif option == '3':
        break
    else:
        print("invalid input")
