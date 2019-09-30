# Spaceships should have a:
class Spaceship():
    def __init__(self, captain, name, signature):
        self.captiain = captain
        self.__name = name
        self.__intergalatic_warp_drive_signature = signature

    def identify(self):
        return self.__intergalatic_warp_drive_signature

    def identify_by_name(self):
        return self.__name

    def change_name(self, name):
        self.__name = name
        # change name



# Captain
# Name
# Intergalatic _warp_drive_signature