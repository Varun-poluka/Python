class PartyAnimal:
    def __init__(self , nam):
        self.x = 0
        self.name = nam
        print(self.name , "constructed")
    def party(self):
        self.x += 1
        print(self.name , "party count" , self.x)

class FootballFan(PartyAnimal): # ingheriting partyanimal 
    def __init__(self , nam):
        super().__init__(nam) # super() is for calling superclass in this case partyanimal
        self.point = 0
    def touchdown(self):
        self.point += 7
        self.party() # using the already pre-defined method in partyanimal 
        print(self.name , "point" , self.point)

s = PartyAnimal("sally")
s.party()
j = FootballFan("john")
j.party()
j.touchdown()