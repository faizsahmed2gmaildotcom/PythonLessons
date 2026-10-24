enemy_dict = {
    "name": "Bob",
    "speed": "high",  # low, medium, or high
    "f1 team": "ferrari",
    "grid position": 1,
    "track_progress": 0
}


if enemy_dict["speed"]== "low":
    enemy_dict["track_progress"]=enemy_dict["track_progress"]+3
    enemy_dict["grid position"]=enemy_dict["grid position"]+2
elif enemy_dict["speed"]=="medium":
    enemy_dict["track_progress"]=enemy_dict["track_progress"]+10
else:
    enemy_dict["track_progress"]=enemy_dict["track_progress"]+30
    enemy_dict["grid position"]=enemy_dict["grid position"]-1
if enemy_dict["grid position"]==0:
    enemy_dict["grid position"]=1
print(enemy_dict)

# Increase track progress by a little if speed is low

# Increase track progress by a normal amount if speed is medium

# Increase track progress by a lot if speed is high
