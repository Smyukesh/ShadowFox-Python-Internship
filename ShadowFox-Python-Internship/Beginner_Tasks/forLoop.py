import random

# Dice simulation
rolls = [random.randint(1, 6) for _ in range(20)]
print("Rolls:", rolls)
print("6s:", rolls.count(6))
print("1s:", rolls.count(1))

# Two 6s in a row
consecutive_sixes = 0
for i in range(len(rolls) - 1):
    if rolls[i] == 6 and rolls[i + 1] == 6:
        consecutive_sixes += 1
print("Two 6s in a row:", consecutive_sixes)

# Jumping jacks
completed = 0
while completed < 100:
    completed += 10
    print(f"Done {completed} jumping jacks")
    tired = input("Are you tired? (y/n): ").lower()
    if tired in ['y', 'yes']:
        skip = input("Do you want to skip remaining? (y/n): ").lower()
        if skip in ['y', 'yes']:
            break
print(f"You completed a total of {completed} jumping jacks.")
if completed == 100:
    print("Congratulations! You completed the workout.")
