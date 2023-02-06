print("rock =1")
print("paper = 2")
print("scissor =3")
user1=int(input("enter your choice user1 "))
user2=int(input("enter your choice  user2"))
while True:
        if(user1==user2):
                print("tie")
                print("choose again")
        elif((user1==1 and user2==3)or(user1==2 and user2==1)or(user1==3 and user2==2)):
                print("user1 wins") 
                user1=int(input("enter your choice user1 "))
                user2=int(input("enter your choice user2 "))
        elif((user1==1 and user2==2)or(user1==2 and user2==3)or(user1==3 and user2==1)):
                print("user2 wins")
                user1=int(input("enter your choice user1 "))
                user2=int(input("enter your choice user2 "))
        else:
                print("invalid choice")
                user1=int(input("enter your choice user1 "))
                user2=int(input("enter your choice user2 "))
        continue    
