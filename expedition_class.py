# Create expeditions with:
class Expedition():

    def __init__(self, destination, spaceship = '', origin = "Gazorpazorp"):
        self.__origin = origin
        self.__destination = destination
        self.__spaceship = spaceship
        self.__passenger_list = []

        # Keep list of  generated expoiditions ( add to empty list of expeditions)
        # Assign a space ship to each one
        # should be able to assign on creation of the object or
        # should be able to assign post-facto

    # Assigning variables always goes from left to right. == is not the same as =
    # self.__spaceship = new_spaceship is not the same as new_spaceship = self.__spaceship
    def assign_spaceship(self, new_spaceship):
        self.__spaceship = new_spaceship

        # Get the passenger list, then append passengers to it
    def add_passenger_to_list(self, passenger):
        if self.__passenger_list.append(passenger):
            return True
        else:
            return False

        # We want to send a dictionary with
        # Origin, Destination, Ship, passengers
    def expo_details(self):
            expo_details = {
                "Origin": self.__origin,
                "Destination": self.__destination,
                "Ship": self.__spaceship,
                "Passenger List": self.__passenger_list
            }
            return expo_details
    # You can also use the bellow method to iterate over all the expeditions
    # Use a getter method and call it with your expidition index in the for loop of expedition_list
    def get_origin(self):
        return self.__origin

    def get_destination(self):
        return self.__destination

    def get_ship(self):
        return self.__spaceship

    def get_passenger_list(self):
        return self.__passenger_list

    # Generally wouldnt use the bellow statement as it contains a print in the ethod which is bad practice
    def print_list_passengers(self):
        for passenger in self.get_passenger_list():
            print('Name: ' + passenger.f_name, 'Species: ' + passenger.species, 'IDR: ' + passenger.dna_reg )

# An origin (probably always Gazorpazorp),
# Should have a destination,
# A space craft assinged to it,
# A list of passengers