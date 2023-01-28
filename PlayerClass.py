### Main file for Kniffel
from colorama import Fore

## KniffelPlayer is a class that stores a dict of their scoresheet, contains their name
# and contains several methods for playing and updating the scoresheet

class KniffelPlayer:
    def __init__(self, name):
        self.name = name
        self.total_score = 0
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
        print(f"\n{self.name}s Zettel. \n""Noch offen:")
        still_open = []
        for key, value in self.scoresheet.items():
            if value == None:
                still_open.append(key)
                print(key)
            else:
                continue
        return still_open

    #one turn of kniffel
    def one_turn(self):
        final_dice = []
        print(f"\n{str(self.name)} ist am Zug!")
        input("\nDrücke Enter um zu würfeln..\n")

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



        final_dice = current_dice

        return final_dice

    def add_score(self, five_dice):
        still_open = self.still_open()

        print("\nDein Ergebnis:\n" + " --- ".join([str(num) for num in five_dice]))

        field_to_score = input("\nBitte gebe an wo du das Ergebnis aufschreiben möchtest!\n")

        while field_to_score not in still_open:
            field_to_score = input(f"\n Du hast bereits {field_to_score} aufgeschrieben. Bitte wähle etwas anderes!\n")

        if field_to_score in ["1er", "2er", "3er", "4er", "5er", "6er"]:
            self.scoresheet[field_to_score] = sum([num for num in five_dice if str(num) == field_to_score[0]])
        elif field_to_score == "Dreierpasch":
            if multiple_and_fullhouse(five_dice, 3):
                self.scoresheet[field_to_score] = sum([int(num) for num in five_dice])
            else:
                print(Fore.RED + "\nErgebnis erfüllt nicht die Bedingungen. Es wird eine 0 notiert.\n" + Fore.RESET)
                self.scoresheet[field_to_score] = 0
        elif field_to_score == "Viererpasch":
            if multiple_and_fullhouse(five_dice, 4):
                self.scoresheet[field_to_score] = sum([int(num) for num in five_dice])
            else:
                print(Fore.RED + "\nErgebnis erfüllt nicht die Bedingungen. Es wird eine 0 notiert.\n" + Fore.RESET)
                self.scoresheet[field_to_score] = 0
        elif field_to_score == "Full House":
            if multiple_and_fullhouse(five_dice, "fh"):
                self.scoresheet[field_to_score] = 25
            else:
                print(Fore.RED + "\nErgebnis erfüllt nicht die Bedingungen. Es wird eine 0 notiert.\n" + Fore.RESET)
                self.scoresheet[field_to_score] = 0
        elif field_to_score == "Kleine Straße":
            #if set([1,2,3,4]) in set(five_dice) or set([2,3,4,5]) in set(five_dice) or set([3,4,5,6]) in set(five_dice):
            if all([x in five_dice for x in [1,2,3,4]]) or all([x in five_dice for x in [2,3,4,5]]) or all([x in five_dice for x in [3,4,5,6]]):
                self.scoresheet[field_to_score] = 30
            else:
                print(Fore.RED + "\nErgebnis erfüllt nicht die Bedingungen. Es wird eine 0 notiert.\n" + Fore.RESET)
                self.scoresheet[field_to_score] = 0
        elif field_to_score == "Große Straße":
            if set([1,2,3,4,5]) == set(five_dice) or set([2,3,4,5,6]) == set(five_dice):
                self.scoresheet[field_to_score] = 40
            else:
                print(Fore.RED + "\nErgebnis erfüllt nicht die Bedingungen. Es wird eine 0 notiert.\n" + Fore.RESET)
                self.scoresheet[field_to_score] = 0
        elif field_to_score == "Kniffel":
            if len(set(five_dice)) == 1:
                self.scoresheet[field_to_score] = 50
            else:
                print(Fore.RED + "\nErgebnis erfüllt nicht die Bedingungen. Es wird eine 0 notiert.\n" + Fore.RESET)
                self.scoresheet[field_to_score] = 0
        elif field_to_score == "Chance":
            self.scoresheet[field_to_score] = sum([int(num) for num in five_dice])

    def get_total_score(self):
        self.total_score = sum([val for val in self.scoresheet.values()])
        if sum([val for val in list(self.scoresheet.values())[0:6]]) >= 63:
            self.total_score += 35
        return self.total_score










def one_roll(n):
    import random
    res = [random.randint(1,6) for i in range(n)]
    print("\n" + " --- ".join([str(num) for num in res]))
    return res

def multiple_and_fullhouse(some_dice, condition):
    all_vals = {

    }

    for val in some_dice:
        if val in all_vals.keys():
            all_vals[val] += 1
        else:
            all_vals[val] = 1
    if condition == 3:
        return 3 in list(all_vals.values()) or 4 in list(all_vals.values()) or 5 in list(all_vals.values())
    elif condition == 4:
        return 4 in list(all_vals.values()) or 5 in list(all_vals.values())
    elif condition == "fh":
        return 2 in list(all_vals.values()) and 3 in list(all_vals.values())


#helper function to determine key of max value in dict (determine winner)
def keywithmaxval(d):
     """ a) create a list of the dict's keys and values;
         b) return the key with the max value"""
     v = list(d.values())
     k = list(d.keys())
     return k[v.index(max(v))]
