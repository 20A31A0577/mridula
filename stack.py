#stacks
#one and only one rule elements stored from top to bottom

#to remove elemnts :
 #   elements are removed from top
#class stack:
 #   def ___init__(self):
  #      self.arr = []
   # def stack_push(self,value):
    #    #to add ele
     #   self.arr.append(value)
    #def stack_pop(self,value):
       #to del ele
     #   self.arr.pop()
    #def printstack(self):
     #   print(self.arr)
class stack:
    def __init__(self):
        self.arr = []
    def stack_push(self,value):
        self.arr.append(value)
    def stack_pop(self):
        self.arr.pop()
    def printstack(self):
        print(self.arr)

s=stack()
s.stack_push(10)
s.stack_push(20)
s.stack_push(30)
print(s.arr)
s.stack_pop()
print(s.arr)
    
        
