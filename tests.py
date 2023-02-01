import PlayerClass
import colorama
from colorama import Fore
# Write a test that checks the get_total_score method
def total_score_test(sample_scoresheet):
    test_player = PlayerClass.KniffelPlayer("test_player")

    test_player.scoresheet = sample_scoresheet

    return test_player.get_total_score()

#scoresheet that achieves bonus and should result in 243 points
scoresheet_with_bonus = {
            "1er": 3,
            "2er": 6,
            "3er": 9,
            "4er": 12,
            "5er": 15,
            "6er": 18,
            "Dreierpasch": 20,
            "Viererpasch": 20,
            "Full House": 25,
            "Kleine Straße": 0,
            "Große Straße": 0,
            "Kniffel": 50,
            "Chance": 20
        }

#without bonus (target == 202)
scoresheet_no_bonus = {
            "1er": 3,
            "2er": 6,
            "3er": 9,
            "4er": 12,
            "5er": 15,
            "6er": 12,
            "Dreierpasch": 20,
            "Viererpasch": 20,
            "Full House": 25,
            "Kleine Straße": 0,
            "Große Straße": 0,
            "Kniffel": 50,
            "Chance": 20
        }

#testing with Bonus (target == 243)
test_total_bonus = total_score_test(scoresheet_with_bonus)

if test_total_bonus == 233:
    print(Fore.GREEN + "Test passed for scoresheet with bonus!")
else:
    print(Fore.RED + f"Test failed! {test_total_bonus} != 243")

#testing without bonus (target 202)
test_total_no_bonus = total_score_test(scoresheet_no_bonus)

if test_total_no_bonus == 192:
    print(Fore.GREEN + "Test passed for scoresheet without bonus")
else:
    print(Fore.RED + f"Test failed! {test_total_no_bonus} != 202")
print(Fore.RESET)

### Testing add score method
dummy_player = PlayerClass.KniffelPlayer("dummy")

## 1er
dummy_player.add_score(["1", "1", "2", "3", "3"])

print(dummy_player.scoresheet)

dummy_player.add_score(["3", "3", "4", "5", "5"])

print(dummy_player.scoresheet)


## some random changes
