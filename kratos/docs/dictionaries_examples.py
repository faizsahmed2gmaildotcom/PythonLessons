enemy_dict = {
    "name": "Bob",
    "speed": "high",  # low, medium, or high
    "f1 team": "ferrari",
    "grid position": 1,
    "track_progress": 0
}

if enemy_dict["speed"] == "low":
    enemy_dict["track_progress"] = enemy_dict["track_progress"] + 3
    enemy_dict["grid position"] = enemy_dict["grid position"] - 1
elif enemy_dict["speed"] == "medium":
    enemy_dict["track_progress"] = enemy_dict["track_progress"] + 10
else:
    enemy_dict["track_progress"] = enemy_dict["track_progress"] + 30
    enemy_dict["grid position"] = enemy_dict["grid position"] + 2
if enemy_dict["grid position"] == 0:
    enemy_dict["grid position"] = 1
print(enemy_dict)


# Parse enemy_dict into a full sentence:
# Bob is travelling at high speed and is in the Ferrari F1 Team. He's starting in Grid Position 1, and has currently progressed along the track by 30 units.
