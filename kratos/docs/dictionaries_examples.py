enemy_dict = {
    "name": "Bob",
    "speed": "medium",  # low, medium, or high
    "f1 team": "ferrari",
    "grid position": 10,
    "track_progress": 0
}

if enemy_dict["f1 team"] == "ferrari":
    enemy_dict["grid position"] = 2

print(enemy_dict)

# Increase track progress by a little if speed is low

# Increase track progress by a normal amount if speed is medium

# Increase track progress by a lot if speed is high
