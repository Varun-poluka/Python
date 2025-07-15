class PartyAnimal:
    def __init__(self , z): # constructor can also have parameters 
        self.name = z
        self.x = 0
    def party(self):
        self.x += 1
        print(self.name, "party count", self.x)

s = PartyAnimal("sally")
s.party()
j = PartyAnimal("john")
j.party()
s.party()
