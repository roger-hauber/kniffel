### Main file for Kniffel
## KniffelPlayer is a class that stores a dict of their scoresheet, contains their name
# and contains several methods for playing and updating the scoresheet

class KniffelPlayer:
    def __init__(self, name):
        self.name = name,
        self.scoresheet = {
            "1er": None,
            "2er": None,
            "3er": None,
            "4er": None,
            "5er": None,
            "6er": None,
            "Dreierpasch": None,
            "Viererpasch": None,
            "Full House": None,
            "Kleine Straße": None,
            "Große Straße": None,
            "Kniffel": None,
            "Chance": None
        }

    #Show what is still available on scoresheet
    def still_open(self):
        print("Noch offen:")
        for key, value in self.scoresheet.items():
            if value == None:
                print(key)
            else:
                continue
