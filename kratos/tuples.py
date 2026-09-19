my_list = ['a', 'b', 'c', 'd', 'e']
my_tuple = ('a', 'b', 'c', 'd', 'e')
# Tuples are immutable and static:
#   Immutable: data cannot change
#   Static: length cannot change

my_list.append('f')
# my_tuple.append('f')  # Error!

my_list.pop(0)
# my_tuple.pop(0)  # Error!

my_list[-1] = '67'
# my_tuple[-1] = '67'  # Error!

for val in my_tuple:
    print(val)

first_5_prime_n = (0, 2, 3, 5, 7)
# ^can make this a tuple, as size and values never change!

first_5_prime_n = (1, 2, 3, 5, 7)
# ^re-assigns the existing tuple to a new one, so no error!

# Exercise 4-13:
# A buffet-style restaurant offers only five basic foods.
# Think of five simple foods and store them in a tuple.
# 1. Use a for loop to print each food in the restaurant.
# 2. Try to modify any food in the tuple. Make sure Python rejects the change.
# 3. Change 2 foods in the menu by re-assigning the existing tuple to a new one.
