
class father:
    def __init__(self,name):
        self.name = name
     
    def love (self):
        return f"i am a father  and i love my {self.name}"
    
class mother:
      def __init__(self,name,sonname):
        self.name = name
        self.sonname = sonname

      def nickname(self):
        return f"my son name is {self.sonname}"
      
class Family(father,mother):
     def __init__(self,name,sonname,age):
         father.__init__(self,name)
         mother.__init__(self,name,sonname)
         self.age= age
           
     def age(self):
        return f"my son age is {self.age}"
     
bhunti=Family("son","bhunti",18)
print(bhunti.love())
print(bhunti.nickname())
print(bhunti.age)





