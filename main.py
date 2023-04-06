import random
print("⚔️ Character Stats Generator ⚔️")

def dice(sides):
  while True:
    result = random.randint(1, sides)
    return result

def HP(dice1, dice2):
  health1 = dice(dice1)
  health2 = dice(dice2)
  return health1 * health2

warriors = int(input("How many characters do you want? "))

for i in range(warriors):
  name = input("Name your warrior: ")
  health = HP(6, 8)
  print("Their health is: ", health, "hp")