class Vehicle():
    Vehicletype = ""

class Automobile(Vehicle):
    year = 0
    make = ""
    model = ""
    doors = ""
    roof = ""



#makes the class Automobile a variable 
S1 = Automobile()
S1.Vehicletype = input("Please select vehicle type: ")
S1.year = input("Please enter the year of the vehicle")
S1.make = input("Please input the make of your car: ")
S1.doors = input("Please input how many doors your car has (2 or 4): ")
S1.roof = input("Please input whether you car has a sun roof or a solid roof: ")

#Stores the the variables in a dictionary
CarStorage = {"Vehicle Type: ": S1.Vehicletype, "Year: ": S1.year, "Make: ": S1.make, "Doors: ": S1.doors, "Roof: ": S1.roof}

#prints both halves of the dictionary 
for x in CarStorage:
    print(x + str(CarStorage[x]))


# tried to do input validation but I'm not sure how it works
def intvalidate(valid):
   while True:

    try:
     valid = int(valid)
     
    except ValueError:
       print("Invalid please enter a number")
    return valid
