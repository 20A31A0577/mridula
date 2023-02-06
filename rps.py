from random import randint,random
print("rock =1")
print("paper = 2")
print("scissor= 3")
user1=int(input("enter your choice user1 "))
user2=randint(1,3)
print("user2 input is",user2)
while True:
    if(user1 == user2):
        print("tie")
        print("choose again")
        user1=int(input("enter your choice user1 "))
        user2=randint(1,3)
        print(user2) 
    elif((user1==1 and user2==3)or(user1==2 and user2==1)or(user1==3 and user2==2)):
        print("user1 wins") 
        user1=int(input("enter your choice user1 "))
        user2=randint(1,3)
        print(user2)
    elif((user1==1 and user2==2)or(user1==2 and user2==3)or(user1==3 and user2==1)):
        print("user2 wins")
        user1=int(input("enter your choice user1 "))
        user2=randint(1,3)
        print(user2)
    else:
        print("invalid choice")
        user1=int(input("enter your choice user1 "))
        user2=randint(1,3)
        print(user2)
    continue    
            
        #user1=int(input("enter your choice"))
        #user2=int(input("enter your choice"))
        #break
        #user1=int(input("enter your choice"))
        #user2=randint(1,3)
        #if user1 == 1 and user2 == 2:
        #    print("user2 win")
        #elif user1 == 1 and user2 == 3:
        #    print("user1 win")
        #elif user1 == 2 and user2 == 3:
        #    print("user2 win")
        #elif user1 == 2 and user2 == 1:
        #    print("user1 win")
        #elif user1 == 3 and user2 == 2:
        #    print("user1 win")
        #elif user1 == 3 and user2 == 1:
        #    print("user2 win")
        #else:
        #    print("invalid choice")
        #continue            

