# Real dictionary: word -> definition
# Python dictionary: key -> value
# Unlike lists, you can access dictionaries using anything, not just integers!

"""
DEFINITION
dict = {
    key: value,
    ...
}

ACCESS
dict[key] = value
"""

name = "name"

enemy_dict = {
    name: "America",
    "health": 1,
    "defense": 2,
    "attack": 100,
    "Description": "This enemy is a glass canon -- high attack, low survivability."
}

enemy_list = [
    "America",
    1,
    2,
    100,
    "This enemy is a glass canon -- high attack, low survivability."
]


print(enemy_dict[name])
