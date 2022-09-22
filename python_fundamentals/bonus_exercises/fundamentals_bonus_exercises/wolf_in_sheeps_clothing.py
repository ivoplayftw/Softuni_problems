animals = input().split(", ")
number_of_wolf = animals.index('wolf') + 1
if number_of_wolf == (len(animals)):
    print("Please go away and stop eating my sheep")
elif number_of_wolf == 1:
    print(f"Oi! Sheep number {len(animals) - number_of_wolf}! You are about to be eaten by a wolf!")
else:
    print(f"Oi! Sheep number {len(animals) - number_of_wolf}! You are about to be eaten by a wolf!")
