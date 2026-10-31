# Real dictionary: word -> definition
# Python dictionary: key -> value
# Unlike lists, you can access dictionaries using anything, not just integers!

"""
DEFINITION
dict = {
    key: value,
    ...
}

ACCESS (same as a list!)
dict[key] = value

ADDING
dict[new_key] = value

REMOVING (same as a list!)
dict.pop(key)
"""

name = "name"

enemy_dict = {
    name: "America",
    "health": 1,
    "defense": 2,
    "attack": 100,
    "description": "This enemy is a glass canon -- high attack, low survivability."
}

# Changing dict values
enemy_dict["attack"] = 5000
# Adding things to dicts (same as changing values!)
enemy_dict["speed"] = 10
# Removing things from dicts
enemy_dict.pop("attack")

print(enemy_dict)

# This is unreadable! What's all this without a dictionary?
enemy_list = [
    "America",
    1,
    2,
    100,
    "This enemy is a glass canon -- high attack, low survivability."
]

# This is far better:
enemy_dict_as_list = {
    0: "America",
    1: 1,
    2: 2,
    3: 100,
    4: "This enemy is a glass canon -- high attack, low survivability."
}

# Changing list values
enemy_list[3] = 200
print(enemy_list)
