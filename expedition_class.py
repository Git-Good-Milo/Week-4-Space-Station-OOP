# Create expeditions with:
class Expedition():

    def __init__(self, destination, spaceship = '', origin = "Gazorpazorp"):
        self.__origin = origin
        self.__destination = destination
        self.__spaceship = spaceship
        self.__passenger_list = []

    def assign_spaceship(self, new_spaceship):
        self.__spaceship = new_spaceship

        # We want to send a dictionary with
        # Origin, Destination, Ship, passengers
    def expo_details(self):
        expo_details = {
            "Origin": self.__origin,
            "Destination": self.__destination,
            "Ship": self.__spaceship,
            "Passenger List": self.__passenger_list
        }
        return



# An origin (probably always Gazorpazorp),
# Should have a destination,
# A space craft assinged to it,
# A list of passengers