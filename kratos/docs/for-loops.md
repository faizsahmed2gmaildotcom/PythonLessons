# For Loops

A **`for` loop** repeats a block of code over and over, once for each thing in
a collection (like a list) or a range of numbers. It's the main tool Python
gives you to do the same job many times without writing the same lines again.

The basic shape looks like this:

```python
for thing in a_collection:
    do_something_with(thing)
```

Everything on the line **after the colon** that is **indented** (pushed to the
right) is the *body* of the loop. Python runs the indented block once per
`thing`, then moves on to the next one. When the collection runs out, the loop
finishes.

> **Why the indentation matters:** in Python, the spaces in front of the code
> tell Python *which lines belong to the loop*. Forgetting to indent is one of
> the most common beginner mistakes — it usually shows up as an `IndentationError`.

## Looping Through Ranges

You can loop over a `range` of numbers. This is the easiest way to say "do
this N times" or "count from here to there."

```python
for number in range(1, 6):
    print(number)

# prints:
# 1
# 2
# 3
# 4
# 5
```

`range(1, 6)` counts from `1` up to (but **not** including) `6`. If you just
write `range(5)`, it starts at `0`:

```python
for number in range(5):
    print(number)

# prints:
# 0
# 1
# 2
# 3
# 4
```

You can also change the *step* to skip numbers:

```python
for number in range(1, 10, 2):
    print(number)

# prints:
# 1
# 3
# 5
# 7
# 9
```

A classic first loop: add up every number in a range.

```python
total = 0
for number in range(1, 6):
    total += number
print(total)  # 15
```

## Looping Through Lists

You can also loop over the items in a **list**. This is how you "visit" every
item and do something with it, one at a time.

```python
my_foods = ['pizza', 'falafel', 'carrot cake']

for food in my_foods:
    print(food)

# prints:
# pizza
# falafel
# carrot cake
```

Here `food` is just a *name* for "the item I'm on right now." You can call it
anything you like: `for x in my_foods:` works the same. The name only exists
while the loop is running.

You can do as much as you want with each item inside the loop:

```python
my_foods = ['pizza', 'falafel', 'carrot cake']

for food in my_foods:
    print(f"I'd love to have some {food}!")
```

### A quick note on copying vs. not copying

If you're inside a loop (or just working with lists in general), remember the
difference between *copying* a list and *reusing* the same list — you've seen
this in `list-copy.py` and `list-nocopy.py`:

```python
friend_foods = my_foods[:]  # a real copy — two separate lists
friend_foods = my_foods     # NOT a copy — both names point to the SAME list
```

If two names point to the same list, changing one changes both. Use the
`[:]` slice when you want a list you can safely change on its own.

## Bringing It All Together

`range` and lists show up together all the time. To loop over a list *by
number* (when you need to know the position), combine `range` and `len`:

```python
my_foods = ['pizza', 'falafel', 'carrot cake']

for i in range(len(my_foods)):
    print(i, my_foods[i])

# prints:
# 0 pizza
# 1 falafel
# 2 carrot cake
```

But for most jobs, just loop over the items directly (`for food in my_foods`)
— it's shorter and harder to get wrong. Only reach for the `range(len(...))`
version when you really need the number.
