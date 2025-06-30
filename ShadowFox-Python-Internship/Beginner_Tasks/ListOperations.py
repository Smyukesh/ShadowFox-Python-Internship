justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Original:", justice_league)

# 1. Count
print("Total Members:", len(justice_league))

# 2. Add new members
justice_league += ["Batgirl", "Nightwing"]
print("After Recruitment:", justice_league)

# 3. Move Wonder Woman to start
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("New Leader:", justice_league)

# 4. Insert member between Aquaman and Flash
index_flash = justice_league.index("Flash")
justice_league.insert(index_flash, "Green Lantern")  # or "Superman"
print("Separated Aquaman & Flash:", justice_league)

# 5. Replace entire list
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New Team:", justice_league)

# 6. Sort alphabetically
justice_league.sort()
print("Sorted Team:", justice_league)
print("New Leader:", justice_league[0])
