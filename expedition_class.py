# Create expeditions with:
class Expeditions():

    def __init__(self, destination, spaceship, origin = "Gazorpazorp"):
        self.origin = origin
        self.destination = destination
        self.spaceship = spaceship
        self.__passenger_list = []

# An origin (probably always Gazorpazorp),
# Should have a destination,
# A space craft assinged to it,
# A list of passengers