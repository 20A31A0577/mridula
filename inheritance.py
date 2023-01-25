#single inheritance
#class a:
#    name="m"
#    age=12
#class b(a):
#    age=10
#obj=b()
#print(obj.age)
#print(obj.name)
#>>> 10
#>>> m

#multiple inheritace
#class a:
#    name="m"
#    age=36
#class b(a):
#    age=10
#class c(b):
#    degree='btech'
#class d(c):
#    number='123'
#obj=d()
#print(obj.name)
#print(obj.number)
#print(obj.degree)
#print(obj.age)
#>>>m
#>>>123
#>>>btech
#>>>10
#example program
#class hod:
#    sub="aiml"
#class tea(hod):
#    sub1="daa"
#class student(tea):
#    marks="passed"
#obj=student()
#print(obj.sub)
#print(obj.sub1)
#print(obj.marks)
#>>>aiml
#>>>daa
#>>>passed

#heirarchical inherutance
#class college:
#    name="k"
#    year="2001"
#    fee="take"
#class faculty(college):
#    fee="salary"
#class nonteaching(college):
#    fee="salary2"
#obj= nonteaching
#print(obj.name)
#print(obj.year)
#print(obj.fee)
#>>>k
#>>>2001
#>>>salary2

#multiple inheritance
#class college:
#    def t1(self):
#        print("one way")
#class youtube(college):
#    def t2(self):
#        print("second way")
#class tution(college):
#    def t3(self):
#        print("third way")
#class student(youtube,tution):
#    pass
#obj=student()
#obj.t3()
#obj.t2()
#obj.t1()
#>>>third way
#>>>second way
#>>>one way
#overriding example
#class animal:
#    def speak(self):
#        print("animals speak")
#class dog(animal):
#    def speak(self):
#        print("dog says bow bow")
#    def eat(self):
#        print("dog eats meat")
#class cat(animal):
#    def speak(self):
#        print("cat says meow")
#obj=dog()
#obj.speak()
#obj.eat()

#overloading
#def numbers(a,b,c):
#    print(a+b+c)
#def numbers(a,b,c):
#    print(a*b*c)
#numbers(10,10,10)
#OUTPUT
#1000


