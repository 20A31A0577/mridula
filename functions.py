#def addition(num1,num2):
  #  result = num1+num2
 #   return result
#print(addition(10,20))
 #OUTPUT 30
def prime(num):
    count=0
    for i in range(2,num//2):
        if(num%i == 0):
            count =count+1
    if(count == 2):
        print("prime")
    else:
        print("not prime")
prime(int(input()))                 
                 

