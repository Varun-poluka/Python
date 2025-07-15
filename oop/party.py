class PartyAnimal: # define the class
    def __init__(self): # specially names function which creates and initialises 
        self.x = 0 # x is the arrtibute and is set to 0
    def party(self): # party method in the class
        self.x = self.x + 1
        print("So far" , self.x)

an = PartyAnimal() # creates an object of the class and puts in an
#calling the method of the object
an.party()
an.party()
an.party()
