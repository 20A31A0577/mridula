#TO PRINT A 2D ARRAY
#row=3
#col=3
#arr=[]
#for i in range(row):
#    ele=[]
#    for j in range(col):
#        ele.append((int(input('enter element '))))
#    arr.append(ele)
#    print(arr)   
#for i in range(row):
#    for j in  range(col):
#        print(arr[i][j],end=" ")
#    print()
#OUTPUT
#enter element 1
#enter element 3
#[[1, 2, 3]]
#enter element 4
#enter element 5
#enter element 6
#[[1, 2, 3], [4, 5, 6]]
#enter element 7
#enter element 8
#enter element 9
#[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#1 2 3 
#4 5 6 
#7 8 9     
    

##TO ADD 2 MATRICES
#row=3
#col=3
#arr=[[0 for j in range(3)] for i in range(3)]
#arr1=[]
#arr2=[]
#for i in range(row):
#    ele=[]
#    for j in range(col):
#        ele.append(int(input()))
#    arr1.append(ele)
#    print(arr1)
#for i in range(row):
#    for j in range(col):
#        print(arr1[i][j],end=" ")
#    print()
#for i in range(row):
#    ele=[]
#    for j in range(col):
#        ele.append(int(input()))
#    arr2.append(ele)
#    print(arr2)
#for i in range(row):
#    for j in range(col):
#        print(arr2[i][j],end=" ")
#    print()
#for i in range(row):
#    for j in range(col):                
#        arr[i][j]=arr1[i][j]+arr2[i][j]
#    print(arr)
#for i in range(row):
#    for j in range(col):
#        print(arr[i][j],end=" ")
#    print()                
#OUTPUT
#1
#2
#3
#[[1, 2, 3]]
#4
#5
#6
#[[1, 2, 3], [4, 5, 6]]
#7
#8
#9
#[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#1 2 3 
#4 5 6 
#7 8 9 
#1
#2
#3
#[[1, 2, 3]]
#4
#5
#6
#[[1, 2, 3], [4, 5, 6]]
#7
#8
#9
#[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#1 2 3 
#4 5 6 
#7 8 9 
#[[2, 4, 6], [0, 0, 0], [0, 0, 0]]
#[[2, 4, 6], [8, 10, 12], [0, 0, 0]]
#[[2, 4, 6], [8, 10, 12], [14, 16, 18]]
#2 4 6 
#8 10 12 
#14 16 18 

#first='mr.x is'
#age=38
#print(
def addition(num1,num2):
    result = num1+num2
    return result
print(addition(10,20))
    
