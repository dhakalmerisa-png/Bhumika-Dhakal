class Mammal:
    def __init__(self,name):
        self.name = name
     
    def speak (self):
        return f"i am a mamal and i say {self.name}"
    
class Pet:
      def __init__(self,name):
        self.name = name
        self.petname = petname

     def nickname(self):
        return f"my pet name is {self.petname}"
      
class Dog(Mammal,Pet):
    def __init__(self,name,petname):
        self.name =name
        self.petname=petname
jack=Dog("tommy","jack")
print(jack.speak())
print(jack.nickname())