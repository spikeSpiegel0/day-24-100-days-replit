import random
print("Infinity Dice 🎲")
print()
userSides = int(input("How many sides?: "))
playgame = "yes"

def rollDice(userSides):
  print("You rolled", random.randint(1,userSides))
  print()
while playgame == "yes":
  rollDice(userSides)
  playgame = input("Roll again? ")