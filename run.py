# import all classes here
from passenger_class import *
from spaceship_class import *
from expedition_class import *

# Create objects here
    # Generate six passengers
passenger1 = Passenger("Floopy", "Doop", "Cronenburg", "lskne5w7")
passenger2 = Passenger("Bird", "Person", "Giant man bird thing", "rngorihg5")
passenger3 = Passenger("Queen", "Killer", "Xenomorph", "oifhorgn8")
passenger4 = Passenger("Rick", "Sanchez", "Humanoid", "jfoww7887")
passenger5 = Passenger("Chewbaca", "Solofriend", "Wookie", "64d8aa5dw")
passenger6 = Passenger("R2", "D2", "Droid", "iuiq87d7")

    # Generate three spaceships
spaceship1 = Spaceship("Crunch", "Tardis", "Supermega fast9489")
spaceship2 = Spaceship("Kirk", "SSS Enterprise", "kos787fast")
spaceship3 = Spaceship("Solo", "Millennium Falcon", "BOOM!6579")
spaceship4 = Spaceship("Cage", "Nicolaus Excelsior", "4d5aw65d")

    # Gerneate three expeditions
    # Aggrigation can be used to insert an object inside another object.
    # In this case, a ship object inside an expidition object
expedition1 = Expedition("Alderon", spaceship3)
expedition2 = Expedition("Bettlegeus", spaceship2)
expedition3 = Expedition("Jupitor", spaceship1)


    # Keep list of  generated expoiditions ( add to empty list of expeditions)
expedition_list = []
expedition_list.append(expedition1)
expedition_list.append(expedition2)
expedition_list.append(expedition3)

        # Assign a space ship to each one
        # should be able to assign on creation of the object or
        # should be able to assign post-facto
expedition3.assign_spaceship(spaceship4)



    # Assign to each expidition, 2 passengers (append) (method)
expedition1.add_passenger_to_list(passenger1)
expedition1.add_passenger_to_list(passenger4)
# print(expedition1.expo_details())
# print(expedition1.expo_details()['Passenger List']) #List
# print(expedition1.expo_details()['Passenger List'][0]) # Passenger
# print(expedition1.expo_details()['Passenger List'][0].species) # String

expedition2.add_passenger_to_list(passenger2)
expedition2.add_passenger_to_list(passenger3)
print(expedition2.expo_details())

expedition3.add_passenger_to_list(passenger5)
expedition3.add_passenger_to_list(passenger6)

    # iterate over list of expeditions and print
for list in expedition_list:
    for expo in list.expo_details():
        print(expo, list.expo_details()[expo])

    # #iterate over expiditions
        # Iterate over list of passenger objects
            # Print out passenger details


# Create a while loop here
    # use input() to get iser imput and generated objects manually

# - AS a user i can add a pseenger to an expidiotion
# - As a user i can list all expiditions
# - As a user i can create passengers
# - As a user i can list passengers in 1 expedition