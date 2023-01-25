class  userclass:
    full_name = " "
    email = " "
    __password = " "
    mobile_number = " "
    def __init__(self,name,email,password):
        self.full_name=name
        self.email=email
        self.password=__password
    def update_name(self , new_name):
        self.full_name = new_name
    """ setter method for private variable password"""    
    def get_name(self):
        return self.full_name
    def update_password(self , new_password):
        self.__password =new_password
    def update_mobile_number(self, new_number):
        self.mobile_number = new_number
    """ getter method for private variable password"""
    def get_user_pasword(self):
        return self.__password
#to validate a user   
fron registration process import userclass  
class login:
    __db = []
    def ___init__(self):
        self.print_menu()
    def print_menu(self):
        print("welcome user")
        print("1.register")
        print("2.login")
        pritn("3.exit")
    def create_use(self,email,name,password)
    new_user = userclass(name,email,password)
    self.__db.append(new_user)
    print(self.__db)
    def validate_user(self,email,password):
    print(true)
obj = login()
while True:
    option = input("enetr your choice")
    if option == '1':
        name = input("enetr your full name:")
        email= inpt("enetr email")
        password = input("enter new password")
        res=obj.create_user(name,email,password)
        if res == Ture:
            print("user created succesfully")
    elif option == '2':
        pass
    elif option == '3':
        break
