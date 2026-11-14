user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi"
}

# <dict>.items() is a list of (<key>, <value>) tuples
for k_v in user_0.items():
    key = k_v[0]
    val = k_v[1]
    print("key: " + key + " | value: " + val)

print()
# Loop through key-value pairs: for <key>, <val> in <dict>.items()
for key, val in user_0.items():
    print("key: " + key + " | value: " + val)
