# Admission for anyone under age 4 is free.
# Admission for anyone between the ages of 4 and 18 is $5.
# Admission for anyone age 18 or older is $10.
# If they're a senior age 65 or older, admission is declined to due to risk of heart attack.
# Output the cost given age.

age = 50.745627564275

if age < 4:
    print("Free admission!")
# age >= 4 is definitely true here, so use elif instead of (age >= 4) and (age < 18)
elif age < 18:
    print("Admission costs $5")
# age >= 18 is definitely true here
elif age < 65:
    print("Admission costs $10")
# age >= 65 is definitely true here
else:
    print("Admission declined due to risk of heart attack!")
