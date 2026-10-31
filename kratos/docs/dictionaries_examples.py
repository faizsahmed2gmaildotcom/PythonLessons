enemy_dict = {
    "name": "Max Verstappen",
    "speed": "low",  # low, medium, or high
    "f1 team": "red bull",
    "grid position": 1,
    "track_progress": 30
}

if enemy_dict["speed"] == "low":
    enemy_dict["track_progress"] = enemy_dict["track_progress"] + 3
    enemy_dict["grid position"] = enemy_dict["grid position"] + 3
elif enemy_dict["speed"] == "medium":
    enemy_dict["track_progress"] = enemy_dict["track_progress"] + 10
else:
    enemy_dict["track_progress"] = enemy_dict["track_progress"] + 30
    enemy_dict["grid position"] = enemy_dict["grid position"] - 1
if enemy_dict["grid position"] == 0:
    enemy_dict["grid position"] = 1
if enemy_dict["grid position"] >= 22:
    enemy_dict["grid position"] = 22
print(enemy_dict)

# Parse enemy_dict into a full sentence:
# Bob is travelling at high speed and is in the Ferrari F1 Team. He's starting in Grid Position 1, and has currently progressed along the track by 30 units.

print(enemy_dict["name"] + " is travelling at " + enemy_dict["speed"] + " speed and is in the " + enemy_dict[
    "f1 team"].title() + " F1 Team. He's starting in Grid Position " + str(enemy_dict["grid position"]) + ", and has progressed along the track by " + str(
    enemy_dict["track_progress"]) + " units.")


# A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

# Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary,
# and store their meanings as values.

# Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.