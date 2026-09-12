# List Functions

A **list** is an ordered collection of items that can hold anything: numbers,
words, other lists, and so on. You make one with square brackets:

```python
my_foods = ['pizza', 'falafel', 'carrot cake']
```

Here `my_foods` is the name of the list. The items inside are separated by
commas. Python keeps them in the exact order you typed them.

## List Operations

These are the most useful things you can do to a list.

### `append()` — add to the end

`append` takes one item and puts it at the **end** of the list. The list grows
by one item.

```python
my_foods.append('cannoli')
print(my_foods)  # ['pizza', 'falafel', 'carrot cake', 'cannoli']
```

Think of `append` like tacking a new card onto the end of a stack.

### `remove()` — get rid of an item by name

`remove` finds the **first** item that matches the one you give it and takes it
out. The rest of the list stays put.

```python
my_foods.remove('falafel')
print(my_foods)  # ['pizza', 'carrot cake', 'cannoli']
```

If the item isn't in the list, Python will complain (an `error`), so only call
`remove` when you're sure the item is there.

### `pop()` — take an item out and keep it

`pop` removes an item **and hands it back to you** so you can use it. This is
the big difference from `remove`:

- `remove('pizza')` — just gets rid of it.
- `pop()` — takes the item **out** and gives it to a variable.

By default `pop()` removes the **last** item. You can also ask for a specific
one by its number (its *index* — see the slicing file for how numbering works):

```python
last_food = my_foods.pop()      # grabs the last item
print(last_food)                # 'cannoli'
print(my_foods)                 # ['pizza', 'carrot cake']

first_food = my_foods.pop(0)    # grabs the first item
print(first_food)               # 'pizza'
```

Use `pop` when you need to actually use the item you're removing.

### `reverse()` vs `reversed()` — flip the order

These do the same general thing (put the list in backwards) but work differently:

- `reverse()` **changes the list itself**, in place. No new list.
- `reversed()` **makes a backwards copy to read through** and leaves the
  original untouched.

```python
my_foods = ['pizza', 'falafel', 'carrot cake']

# reverse() flips the list forever:
my_foods.reverse()
print(my_foods)  # ['carrot cake', 'falafel', 'pizza']

# reversed() just gives you a backwards view (often used with a loop):
my_foods = ['pizza', 'falafel', 'carrot cake']
for food in reversed(my_foods):
    print(food)          # prints in reverse...
print(my_foods)          # ...but the list is still in the original order
```

Rule of thumb: use `reverse()` when you want the list *to be* flipped, and
`reversed()` when you just want to *read* it backwards once.

### `len()` — how many items?

`len` (short for *length*) tells you how many items are in the list.

```python
my_foods = ['pizza', 'falafel', 'carrot cake']
print(len(my_foods))  # 3
```

You'll use `len` a lot, especially with loops, to know when you've run out of
items to go through.

## List Comprehensions

A **list comprehension** is a compact, one-line way to build a new list by
running a little piece of code for every item in an existing list.

The basic shape is:

```python
[new_item for item in old_list]
```

Read it out loud: *"for every `item` in `old_list`, make a `new_item`."*

```python
# Square every number in a list:
numbers = [1, 2, 3, 4]
squares = [n * n for n in numbers]
print(squares)  # [1, 4, 9, 16]
```

You can also add a condition at the end to only keep the items that match
(read it as *"...if it's even"*):

```python
numbers = [1, 2, 3, 4, 5, 6]
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # [2, 4, 6]
```

Comprehensions can look magic at first, but they're just a `for` loop folded
onto one line. If a comprehension ever feels too clever, rewrite it as a normal
`for` loop — it does exactly the same thing.

## Creating Ranges

A **range** is a list of numbers that counts up. It's perfect for looping a
certain number of times, or for making a numbered list quickly.

```python
print(list(range(5)))       # [0, 1, 2, 3, 4]   counts from 0 up to (but not including) 5
print(list(range(1, 6)))    # [1, 2, 3, 4, 5]   counts from 1 up to 6
print(list(range(1, 10, 2)))# [1, 3, 5, 7, 9]   counts from 1 to 10, skipping by 2
```

The three numbers in `range(start, stop, step)` mean:

- **start** — where to begin (defaults to `0`).
- **stop** — where to stop, *not included* (so `range(5)` stops at `4`).
- **step** — how much to add each time (defaults to `1`).

You'll usually use `range` inside a `for` loop rather than turning it into a
list with `list()` — you'll see exactly how in the `for` loop notes.
