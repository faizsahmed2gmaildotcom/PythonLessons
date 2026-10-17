# Python Fundamental Data Types

| Name       | What they store                                                                | Operators                                                                                                                                                 |
|------------|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| `int`      | Whole numbers (positive, negative, or zero)                                    | `+`, `-`, `*`, `/`, `//` (floor division), `%` (modulus), `**` (exponent), `abs()`, `divmod()`                                                            |
| `float`    | Decimal/floating-point numbers (real numbers)                                  | `+`, `-`, `*`, `/`, `//`, `%`, `**`, `abs()`, `round()`                                                                                                   |
| `bool`     | Boolean values: `True` or `False`                                              | `and`, `or`, `not`, `==`, `!=`, `<`, `>`, `<=`, `>=`                                                                                                      |
| `list`     | Ordered, mutable sequences of items                                            | `+` (concatenate), `*` (repeat), `[]` (index/slice), `in`, `not in`, `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`       |
| `tuple`    | Ordered, immutable sequences of items                                          | `+` (concatenate), `*` (repeat), `[]` (index/slice), `in`, `not in`, `count()`, `index()`                                                                 |
| `str`      | Ordered sequences of characters (text)                                         | `+` (concatenate), `*` (repeat), `[]` (index/slice), `in`, `not in`, `len()`, `upper()`, `lower()`, `strip()`, `split()`, `join()`, `replace()`, `find()` |
| `dict`     | Key-value pairs (mappings)                                                     | `[]` (key lookup/assignment), `in`, `not in`, `keys()`, `values()`, `items()`, `get()`, `update()`, `pop()`, `clear()`, `copy()`                             |
| `iterable` | Objects that can be iterated over (lists, tuples, strings, ranges, generators) | `for` loops, `in`, `not in`, `list()`, `tuple()`, `sum()`, `max()`, `min()`, `sorted()`, `enumerate()`, `zip()`                                           |

## Notes

- **Mutable** means the object can be changed after creation (lists, dicts)
- **Immutable** means the object cannot be changed after creation (strings, tuples, ints, floats, booleans)
- **Concatenate** means to combine or to merge
- The `range()` type creates immutable sequences of numbers often used in loops
- All strings are iterables, but not all iterables are strings
- Dictionary keys must be immutable (strings, ints, tuples), values can be any type
