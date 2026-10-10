cars = ['audi', 'bmw', 'subaru', 'toyota']

# Equality
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Inequality
if cars[0] != 'bmw':
    print("BMW isn't first!")

# Comparisons
age = 5

if age < 20:
    print('child')
elif age > 20:
    print('unc')
else:
    print('tuff')

# Check if an item's in a list: <item> in <list>
if 'subaru' in cars:
    print("foo")

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you're not banned.")
