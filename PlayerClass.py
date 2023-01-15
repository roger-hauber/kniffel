### Main file for Kniffel
## KniffelPlayer is a class that stores a dict of their scoresheet, contains their name
# and contains several methods for playing and updating the scoresheet

class KniffelPlayer:
    def __init__(self, name):
        self.name = name
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
    #one turn of kniffel
    def one_turn(self):
        final_dice = []
        print(f"{str(self.name)} ist am Zug!")
        input("Drücke Enter um zu würfeln..\n")

        instruction = """\nWelche Würfel willst du behalten? \nGebe Werte zw. 1 und 5 an, wo 1 der erste Würfel ist etc.und mit Leerzeichen trennen..\n"""
        first_throw = one_roll(5)
        #print(" --- ".join([str(num) for num in res]))
        dice_selected = input(instruction)
        dice_selected = [int(die) for die in dice_selected.split()]

        dice_kept = [first_throw[i-1] for i in dice_selected]

        input(f"\nZweiter Versuch! Du würfelst mit {5-len(dice_kept)} Würfeln.. Drücke Enter!\n")

        second_throw = one_roll(5-len(dice_kept))

        dice_kept.extend(second_throw)
        current_dice = dice_kept

        print("\nAlle deine Würfel:  " +  " --- ".join([str(num) for num in current_dice]) + "\n")

        dice_selected = input(instruction)
        dice_selected = [int(die) for die in dice_selected.split()]

        dice_kept = [current_dice[i-1] for i in dice_selected]

        input(f"\nDritter Versuch! Du würfelst mit {5-len(dice_kept)} Würfeln.. Drücke Enter!\n")

        third_throw = one_roll(5-len(dice_kept))

        dice_kept.extend(third_throw)
        current_dice = dice_kept

        print("\nDein Endergebnis nach dem dritten Wurf:  \n" +  " --- ".join([str(num) for num in current_dice]))



        final_dice = [current_dice[i-1] for i in dice_selected]

        return final_dice






def one_roll(n):
    import random
    res = [random.randint(1,6) for i in range(n)]
    print(" --- ".join([str(num) for num in res]))
    return res
