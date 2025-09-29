# Task 1: Create Justice League list
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print(f"Initial Justice League: {justice_league}")
print(f"Number of members: {len(justice_league)}\n")


# Task 2: Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print(f"After adding Batgirl and Nightwing: {justice_league}\n")


# Task 3: Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print(f"Wonder Woman as leader: {justice_league}\n")


# Task 4: Separate Aquaman and Flash by inserting Superman
justice_league.remove("Superman")                     # Remove Superman first
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index, "Superman")        # Insert before Flash
print(f"After separating Aquaman and Flash: {justice_league}\n")


# Task 5: Replace list with new team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print(f"New Justice League: {justice_league}\n")


# Task 6: Sort alphabetically
justice_league.sort()
print(f"Sorted Justice League: {justice_league}")
print(f"New Leader (0th index): {justice_league[0]}")
