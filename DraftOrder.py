import random
import time
import sys


players = ["El Jefe", "Lucas", "Dag", "Broc and Cauli", "Sam", "Alik", "Hunter", "Hamlet", "Chase", "Byrd", "Connor", "Old Testaments"]
print("The players in this years draft are: ")
for i in range(len(players)):
    print("Team: {}".format(players[i]))

random.shuffle(players)

def _print(string):
    sys.stdout.write(string)
    sys.stdout.flush()

time.sleep(2)
print("This years draft order is as follows:")
time.sleep(1)


for i in range(len(players)):
    _print("Pick #{}".format(len(players) - i))
    time.sleep(.5)
    _print(" . ")
    time.sleep(.5)
    _print(" . ")
    time.sleep(.5)
    _print(" . ")
    time.sleep(2)
    _print(" Team {}".format(players[i]))
    print("")
    time.sleep(5)

print("Good Luck Boys")


