ordinals = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # <- don't do this!
ordinals = [str(i) for i in range(1, 10)]  # <- OK

for i in ordinals:
    if i == '1':
        print(i + "st")
    elif i == '2':
        print(i + "nd")
    elif i == '3':
        print(i + "rd")
    else:
        print(i + "th")
