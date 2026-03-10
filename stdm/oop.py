class Person:
    name = ""
    age=0
    def __init__(self,name,age=0,salary=50000):
        self.name=name
        self.age=age
        self.salary =salary

    def sayhi(self):
            print(f"hi {self.name}")
    def increase_salary(self):
          self.salary+= self.salary*0.10
          print(f"salary={self.salary}")

    def __str__(self):
                 return f"{self.name},{self.age}"
class People:
        def __init__(self,name,age=0):
         self.name=name
         self.age=age  
         

        def __str__(self):
              return f"{self.name},{self.age}"

p1= Person("bhumika",18,10000)  
p2=Person("merisa",18)         
print(p1.name,p1.age)
print(p2.name,p2.age)
p1.sayhi()
p2.sayhi()
p1.increase_salary()
#p1=Person()
#p2=Person()
#print(type(p1))
#print(p1.name)
#print(p2.name)
