#l=[1,2,3,4]
#for i in l: #printing squares of each number
 #   print(i**2 , end=" ")



#l=[1,2,3,4,5,6,7,8,9]
#key=int(input()) #printing the index of number
#for i in range(0,len(l)):
# if(key == l[i]):
 #   print(i)


#l=[ i for i in range(1,101) if i%7==0 and i%11==0]
#print(l)


#l=[1,2,3,4,5,6,7,8,9]
#for i in range(len(l)-1,-1,-1):
#    print(l[i],end=" ") # rinting numbers in reverse order

l=list(input("enter positive elements").split())
print(l)
l1=list(input("enter negative values").split())
print(l1)
l2=map(int,l)#printing sum of 2 lists
l3=map(int,l1)
a=sum(l2)
b=sum(l3)
print("a+b is",a+b)
