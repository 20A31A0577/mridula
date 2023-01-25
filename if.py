#a=10
#if a%2 == 0:
#    print("even")
#else:
#       print("odd")


#a=int(input())
#if(a==1):
# print("mon")
#elif(a==2):
 #print("tue")
#if(a==3):
# print("wed")
#elif(a==4):
# print("thu")
#elif(a==5):
# print("fri")
#elif(a==6):
# print("sat")
#elif(a==7):
# print("sun")
#else:
 #   print("invaid choice")


a=int(input())
if(a>0 and a<20):
    if (a%2 == 0):
     print("weird number")
    else:
     print("normal number")
elif(a>=20 and a<30):
    print("normal number")
elif(a>=30):
    if(a%2 != 0):
     print("normal number")
    else:
     print("weird number")

