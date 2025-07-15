class PartyAnimal: # define the class
    def __init__(self): # specially names function which creates and initialises 
        self.x = 0 # x is the arrtibute and is set to 0
    def party(self): # party method in the class
        self.x = self.x + 1
        print("So far" , self.x)

an = PartyAnimal()

print("Type:", type(an)) #gives the class name
print("Dir:", dir(an)) # gives many in which x and party are there 
print("Type:",type(an.x)) # gives the type of x
print("Type:", type(an.party)) # gives the type of party 