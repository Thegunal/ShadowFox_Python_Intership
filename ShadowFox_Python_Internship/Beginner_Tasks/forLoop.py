import random

# Task 1: Simulate rolling a six-sided die
rolls = 20
count_six = 0
count_one = 0
consecutive_six = 0
previous_roll = 0

for i in range(rolls):
    roll = random.randint(1, 6)
    print(f"Roll {i+1}: {roll}")
    
    if roll == 6:
        count_six += 1
        if previous_roll == 6:
            consecutive_six += 1
    if roll == 1:
        count_one += 1
    
    previous_roll = roll

print(f"\nTotal number of 6s rolled: {count_six}")
print(f"Total number of 1s rolled: {count_one}")
print(f"Number of times two 6s appeared consecutively: {consecutive_six}\n")


# Task 2: Jumping jacks workout
total_jacks = 100
set_size = 10
completed = 0

for i in range(0, total_jacks, set_size):
    print(f"Perform 10 jumping jacks (set {i//set_size + 1})")
    completed += set_size
    
    tired = input("Are you tired? (yes/y or no/n): ").lower()
    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").lower()
        if skip in ["yes", "y"]:
            print(f"You completed a total of {completed} jumping jacks.")
            break
    remaining = total_jacks - completed
    if remaining > 0:
        print(f"{remaining} jumping jacks remaining\n")
else:
    print("Congratulations! You completed the workout.")
