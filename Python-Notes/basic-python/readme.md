# Python Basics — Learning Notes

> Personal notes documenting my journey through Python fundamentals.  
> Written to solidify understanding — shared for anyone on the same path.

---

## 📚 Table of Contents

- [Chapter 1 — Python Basics](#chapter-1--python-basics)
  - [1.1 History of Python](#11-history-of-python)
  - [1.2 Variables & Data Types](#12-variables--data-types)
  - [1.3 Conditionals & Loops](#13-conditionals--loops)
  - [1.4 Functions](#14-functions)
  - [1.5 Lists](#15-lists)
  - [1.6 Tuples](#16-tuples)
  - [1.7 Sets](#17-sets)
  - [1.8 Dictionaries](#18-dictionaries)

---

## Chapter 1 — Python Basics

---

### 1.1 History of Python

#### Who Created Python?

Python was created by **Guido van Rossum**, a Dutch programmer. He began working on it in the late 1980s and released the first version in **1991**.

> 🐍 **Fun fact:** Python is NOT named after the snake. Guido named it after the British comedy show **Monty Python's Flying Circus** — he wanted a name that was short, unique, and slightly mysterious.

---

#### The Timeline

| Year | Milestone |
|---|---|
| 1989 | Guido starts writing Python over Christmas break |
| 1991 | Python 0.9.0 released — first ever public version |
| 1994 | Python 1.0 released — functional programming tools added |
| 2000 | Python 2.0 released — list comprehensions, garbage collection |
| 2008 | Python 3.0 released — major redesign, broke backwards compatibility |
| 2020 | Python 2 officially retired — Python 3 is the only standard |
| Today | Python is the #1 most popular programming language in the world |

---

#### Why Was Python Created?

Guido wanted a language that was:
- **Easy to read** — code that looks almost like plain English
- **Simple to write** — less boilerplate, more productivity
- **General purpose** — usable for scripting, automation, web, data science, AI

> ⚙️ **Python's core philosophy:** *"There should be one obvious way to do it."*  
> You can read the full philosophy by typing `import this` in any Python shell.

---

#### Why is Python so Popular Today?

| Reason | Explanation |
|---|---|
| 🟢 Beginner friendly | Readable syntax, minimal setup |
| 🔬 Data Science & AI | Powers NumPy, Pandas, TensorFlow, PyTorch |
| 🌐 Web Development | Django, FastAPI, Flask |
| 🤖 Automation | Scripts, bots, scraping |
| 📦 Huge ecosystem | 400,000+ packages on PyPI |
| 🏢 Industry adoption | Used at Google, Netflix, NASA, Instagram |

---

### 1.2 Variables & Data Types

---

#### What is a Variable?

A variable is a **named container that stores a value** in memory. Think of it like a labeled box — you put something inside, and you can always find it by the label.

```
Box label : age
Box contains : 25
```

In Python:

```python
age = 25
name = "G"
is_employed = True
```

No need to declare the type — Python figures it out automatically. This is called **dynamic typing**.

---

#### Rules for Naming Variables

| Rule | Example |
|---|---|
| Must start with a letter or `_` | `name`, `_name` ✅ |
| Cannot start with a number | `1name` ❌ |
| No spaces — use underscores | `my_name` ✅ |
| Case sensitive | `Name` and `name` are different |
| Cannot use reserved keywords | `if`, `for`, `class` ❌ |

---

#### Data Types in Python

| Type | Category | Example |
|---|---|---|
| `int` | Numeric | `age = 25` |
| `float` | Numeric | `price = 9.99` |
| `complex` | Numeric | `z = 2 + 3j` |
| `str` | Text | `name = "G"` |
| `bool` | Boolean | `is_valid = True` |
| `list` | Sequence | `[1, 2, 3]` |
| `tuple` | Sequence | `(1, 2, 3)` |
| `set` | Set | `{1, 2, 3}` |
| `dict` | Mapping | `{"key": "value"}` |
| `NoneType` | None | `result = None` |

---

#### Checking the Type

```python
age = 25
print(type(age))       # <class 'int'>

name = "G"
print(type(name))      # <class 'str'>

price = 9.99
print(type(price))     # <class 'float'>
```

---

#### Type Conversion

You can convert between types explicitly:

```python
x = float(10)      # int → float     → 10.0
y = int(9.99)      # float → int     → 9  (truncates, does NOT round)
z = str(42)        # int → string    → "42"
n = int("100")     # string → int    → 100
f = float("3.14")  # string → float  → 3.14
```

> ⚠️ `int("hello")` throws a `ValueError` — only works if the string actually looks like a number.

---

#### Multiple Assignment

```python
# Same value to multiple variables
x = y = z = 0

# Different values in one line
name, age, city = "G", 25, "Fayetteville"
```

---

#### f-Strings — The Cleanest Way to Format Output

```python
name = "G"
age = 25

print(f"My name is {name} and I am {age} years old.")
# My name is G and I am 25 years old.

print(f"Next year I'll be {age + 1}")
# Next year I'll be 26
```

---

### 1.3 Conditionals & Loops

---

#### 1.3.1 Conditionals — if / elif / else

Conditionals let your program **make decisions** based on whether something is True or False.

**Real world analogy 🚦**

Think of a traffic light:
- If green → go
- Elif yellow → slow down
- Else → stop

```python
light = "green"

if light == "green":
    print("Go!")
elif light == "yellow":
    print("Slow down!")
else:
    print("Stop!")
```

---

#### Comparison Operators

| Operator | Meaning | Example |
|---|---|---|
| `==` | Equal to | `x == 5` |
| `!=` | Not equal to | `x != 5` |
| `>` | Greater than | `x > 5` |
| `<` | Less than | `x < 5` |
| `>=` | Greater than or equal | `x >= 5` |
| `<=` | Less than or equal | `x <= 5` |

---

#### Logical Operators

| Operator | Meaning | Example |
|---|---|---|
| `and` | Both must be True | `age > 18 and has_id` |
| `or` | At least one must be True | `is_admin or is_owner` |
| `not` | Reverses the condition | `not is_banned` |

---

#### Shorthand — Ternary Operator

```python
# Regular way
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

# One-liner
status = "Adult" if age >= 18 else "Minor"
```

---

#### 1.3.2 `for` Loop — When You Know How Many Times to Repeat

**Real world analogy 📋**

Think of a to-do list. You go through each item one by one until the list is done.

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
# apple
# banana
# cherry
```

---

#### `range()` with `for` loops

```python
for i in range(5):        # 0 to 4
    print(i)

for i in range(1, 6):     # 1 to 5
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8 (step of 2)
    print(i)
```

---

#### 1.3.3 `while` Loop — When You Don't Know How Many Times to Repeat

**Real world analogy 🎮**

Think of a game — keep playing while the player has lives remaining. You don't know upfront how many rounds they'll survive.

```python
lives = 3

while lives > 0:
    print(f"Lives remaining: {lives}")
    lives -= 1

# Lives remaining: 3
# Lives remaining: 2
# Lives remaining: 1
```

> ⚠️ Always make sure your `while` loop has a way to end — otherwise you'll create an **infinite loop** and your program will freeze.

---

#### Loop Control — `break`, `continue`, `pass`

| Keyword | What it does | Analogy |
|---|---|---|
| `break` | Exits the loop immediately | Emergency exit 🚪 |
| `continue` | Skips current iteration, moves to next | Skip a song ⏭️ |
| `pass` | Does nothing — placeholder | Empty room 🏠 |

```python
# break — stop when you find what you need
for num in range(10):
    if num == 5:
        break
    print(num)
# 0 1 2 3 4

# continue — skip odd numbers
for num in range(10):
    if num % 2 != 0:
        continue
    print(num)
# 0 2 4 6 8

# pass — placeholder for future code
for num in range(5):
    pass  # will fill this in later
```

---

#### Nested Loops

A loop inside a loop. The inner loop completes fully for every single iteration of the outer loop.

```python
for i in range(1, 4):       # outer loop
    for j in range(1, 4):   # inner loop
        print(f"{i} x {j} = {i*j}")
```

---

### 1.4 Functions

---

#### What is a Function?

A function is a **reusable block of code** that performs a specific task. Instead of writing the same code over and over, you define it once and call it whenever needed.

**Real world analogy 🍕**

Think of a pizza recipe. You write the recipe once, and you can make pizza as many times as you want without rewriting the steps.

```python
def make_pizza(topping):
    print(f"Making a {topping} pizza!")

make_pizza("pepperoni")   # Making a pepperoni pizza!
make_pizza("margherita")  # Making a margherita pizza!
```

---

#### Anatomy of a Function

```python
def function_name(parameters):
    # body
    return value
```

| Part | What it is |
|---|---|
| `def` | Keyword that defines a function |
| `function_name` | The name you give it |
| `parameters` | Inputs the function accepts (optional) |
| `return` | Sends a value back to the caller (optional) |

---

#### Parameters vs Arguments

```python
def greet(name):       # 'name' is the PARAMETER (placeholder)
    print(f"Hello, {name}!")

greet("G")             # "G" is the ARGUMENT (actual value)
```

> **Parameter** = variable in the function definition  
> **Argument** = actual value passed when calling the function

---

#### Default Parameters

```python
def greet(name, greeting="Hello"):   # greeting has a default value
    print(f"{greeting}, {name}!")

greet("G")                  # Hello, G!
greet("G", "What's up")     # What's up, G!
```

---

#### Return Values

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)   # 8
```

A function without `return` gives back `None` by default.

---

#### `*args` — Multiple Positional Arguments

When you don't know how many arguments will be passed:

```python
def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3))        # 6
print(add_all(10, 20, 30, 40)) # 100
```

`*args` collects all extra positional arguments into a **tuple**.

---

#### `**kwargs` — Multiple Keyword Arguments

```python
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="G", age=25, city="Fayetteville")
# name: G
# age: 25
# city: Fayetteville
```

`**kwargs` collects all extra keyword arguments into a **dict**.

---

#### Lambda Functions — One-liner Anonymous Functions

```python
# Regular function
def square(x):
    return x * x

# Lambda equivalent
square = lambda x: x * x

print(square(5))   # 25
```

Lambdas are useful when you need a quick, throwaway function — commonly used with `map()`, `filter()`, and `sorted()`.

```python
numbers = [3, 1, 4, 1, 5, 9]
sorted_nums = sorted(numbers, key=lambda x: x)
print(sorted_nums)  # [1, 1, 3, 4, 5, 9]
```

---

#### Summary Table

| Concept | Syntax | Use case |
|---|---|---|
| Basic function | `def fn(x):` | Reusable block of code |
| Default parameter | `def fn(x=10):` | Optional argument with fallback |
| Return value | `return value` | Send result back to caller |
| `*args` | `def fn(*args):` | Unknown number of positional args |
| `**kwargs` | `def fn(**kwargs):` | Unknown number of keyword args |
| Lambda | `lambda x: x*2` | Quick one-liner anonymous function |

---

### 1.5 Lists

---

#### What is a List?

A list is an **ordered, mutable collection** that can hold items of any type — including mixed types.

**Real world analogy 🛒**

Think of a shopping cart. You can add items, remove items, change items, and the order matters.

```python
shopping = ["milk", "eggs", "bread"]
```

| Property | Meaning |
|---|---|
| Ordered | Items have a fixed position (index) |
| Mutable | You can change, add, or remove items |
| Allows duplicates | Same value can appear multiple times |

---

#### Creating a List

```python
fruits = ["apple", "banana", "cherry"]
mixed  = [1, "hello", True, 3.14]     # mixed types allowed
empty  = []                            # empty list
```

---

#### Indexing & Slicing

```python
fruits = ["apple", "banana", "cherry", "mango"]

# Indexing (starts at 0)
print(fruits[0])    # apple
print(fruits[-1])   # mango  (negative = from the end)

# Slicing [start:stop:step]
print(fruits[1:3])  # ['banana', 'cherry']
print(fruits[:2])   # ['apple', 'banana']
print(fruits[::2])  # ['apple', 'cherry']  (every 2nd item)
```

---

#### Common List Methods

| Method | What it does | Example |
|---|---|---|
| `append(x)` | Adds item to the end | `fruits.append("kiwi")` |
| `insert(i, x)` | Inserts item at index | `fruits.insert(1, "kiwi")` |
| `remove(x)` | Removes first occurrence | `fruits.remove("banana")` |
| `pop(i)` | Removes & returns item at index | `fruits.pop(0)` |
| `sort()` | Sorts in place | `fruits.sort()` |
| `reverse()` | Reverses in place | `fruits.reverse()` |
| `index(x)` | Returns index of item | `fruits.index("apple")` |
| `count(x)` | Counts occurrences | `fruits.count("apple")` |
| `len()` | Returns length | `len(fruits)` |
| `clear()` | Removes all items | `fruits.clear()` |
| `copy()` | Returns a shallow copy | `fruits.copy()` |
| `extend(lst)` | Appends another list | `fruits.extend(["kiwi"])` |

---

#### List Comprehension — Pythonic One-liner

```python
# Regular way
squares = []
for i in range(1, 6):
    squares.append(i * i)

# List comprehension
squares = [i * i for i in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# With condition
evens = [i for i in range(10) if i % 2 == 0]
print(evens)    # [0, 2, 4, 6, 8]
```

---

### 1.6 Tuples

---

#### What is a Tuple?

A tuple is an **ordered, immutable collection**. Once created, you cannot change it.

**Real world analogy 📍**

Think of GPS coordinates. Latitude and longitude are fixed — you wouldn't want them to accidentally change.

```python
location = (17.3850, 78.4867)  # Hyderabad coordinates
```

| Property | Meaning |
|---|---|
| Ordered | Items have a fixed position |
| Immutable | Cannot be changed after creation |
| Allows duplicates | Same value can appear multiple times |

---

#### Creating a Tuple

```python
colors  = ("red", "green", "blue")
single  = (42,)      # ← comma is required for single-item tuple
empty   = ()         # empty tuple
mixed   = (1, "G", True)
```

> ⚠️ `(42)` is just an integer. `(42,)` is a tuple. The comma matters!

---

#### Indexing & Slicing — Same as Lists

```python
colors = ("red", "green", "blue")

print(colors[0])    # red
print(colors[-1])   # blue
print(colors[0:2])  # ('red', 'green')
```

---

#### Why use Tuples over Lists?

| Situation | Use |
|---|---|
| Data that should never change | Tuple — `(lat, lng)`, `(r, g, b)` |
| Data that needs to change | List |
| Slightly faster than list | Tuple |
| Dictionary key | Tuple ✅ (lists can't be keys) |

---

#### Tuple Unpacking

```python
coordinates = (17.38, 78.48)
lat, lng = coordinates

print(lat)  # 17.38
print(lng)  # 78.48
```

---

#### Tuple Methods

Tuples have only 2 methods (since they're immutable):

| Method | What it does |
|---|---|
| `count(x)` | Counts occurrences of x |
| `index(x)` | Returns index of first occurrence of x |

---

### 1.7 Sets

---

#### What is a Set?

A set is an **unordered collection of unique items**. Duplicates are automatically removed.

**Real world analogy 🎟️**

Think of a guest list for an event. Each person can only appear once — no duplicates allowed, and the order doesn't matter.

```python
guests = {"Alice", "Bob", "Charlie", "Alice"}
print(guests)  # {'Alice', 'Bob', 'Charlie'}  ← duplicate removed!
```

| Property | Meaning |
|---|---|
| Unordered | No index, no guaranteed order |
| Mutable | Can add or remove items |
| No duplicates | Automatically ignores duplicate values |

---

#### Creating a Set

```python
nums    = {1, 2, 3, 4}
fruits  = {"apple", "banana", "cherry"}
empty   = set()    # ← must use set(), NOT {} (that creates a dict!)
```

---

#### Common Set Methods

| Method | What it does |
|---|---|
| `add(x)` | Adds an item |
| `remove(x)` | Removes item — raises error if not found |
| `discard(x)` | Removes item — no error if not found |
| `pop()` | Removes and returns a random item |
| `clear()` | Removes all items |
| `len()` | Returns number of items |

---

#### Set Operations — The Real Power of Sets

**Real world analogy 🔵🔴**

Think of Venn diagrams from math class. Sets give you the same operations.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union — all items from both
print(A | B)         # {1, 2, 3, 4, 5, 6}

# Intersection — only items in BOTH
print(A & B)         # {3, 4}

# Difference — items in A but NOT in B
print(A - B)         # {1, 2}

# Symmetric Difference — items in either but NOT both
print(A ^ B)         # {1, 2, 5, 6}
```

---

#### When to Use Sets?

| Use case | Example |
|---|---|
| Remove duplicates from a list | `list(set(my_list))` |
| Fast membership testing | `if x in my_set` |
| Math-style set operations | union, intersection, difference |

---

### 1.8 Dictionaries

---

#### What is a Dictionary?

A dictionary is a collection of **key-value pairs**. Instead of accessing items by index, you access them by a unique key.

**Real world analogy 📖**

Think of an actual dictionary. You look up a word (key) and get its definition (value). You don't need to know the page number — just the word.

```python
person = {
    "name": "G",
    "age": 25,
    "city": "Fayetteville"
}
```

| Property | Meaning |
|---|---|
| Key-value pairs | Each item is a pair — `key: value` |
| Keys are unique | No duplicate keys |
| Ordered | Maintains insertion order (Python 3.7+) |
| Mutable | Can add, update, or remove items |

---

#### Creating a Dictionary

```python
# Literal syntax
car = {"brand": "Toyota", "year": 2022, "color": "Red"}

# Empty dict
empty = {}

# dict() constructor
person = dict(name="G", age=25)
```

---

#### Accessing Values

```python
car = {"brand": "Toyota", "year": 2022}

# Direct access — raises KeyError if key doesn't exist
print(car["brand"])         # Toyota

# Safe access — returns None (or default) if key doesn't exist
print(car.get("color"))           # None
print(car.get("color", "Black"))  # Black
```

---

#### Adding, Updating & Deleting

```python
car = {"brand": "Toyota"}

# Add new key
car["color"] = "Red"

# Update existing key
car["brand"] = "BMW"

# Delete a key
del car["color"]

# Remove and return a value
year = car.pop("year", None)  # returns None if key doesn't exist

print(car)
```

---

#### Common Dictionary Methods

| Method | What it does |
|---|---|
| `keys()` | Returns all keys |
| `values()` | Returns all values |
| `items()` | Returns all key-value pairs as tuples |
| `get(key, default)` | Safe value access |
| `pop(key)` | Removes and returns a value |
| `update(dict)` | Merges another dict in |
| `clear()` | Removes all items |
| `copy()` | Returns a shallow copy |

---

#### Iterating Over a Dictionary

```python
person = {"name": "G", "age": 25, "city": "Fayetteville"}

# Iterate over keys
for key in person:
    print(key)

# Iterate over values
for value in person.values():
    print(value)

# Iterate over key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
```

---

#### Dictionary Comprehension

```python
# Regular way
squares = {}
for i in range(1, 6):
    squares[i] = i * i

# Dictionary comprehension
squares = {i: i * i for i in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

#### Quick Comparison — List vs Tuple vs Set vs Dict

| | List | Tuple | Set | Dict |
|---|---|---|---|---|
| Syntax | `[1, 2]` | `(1, 2)` | `{1, 2}` | `{"k": "v"}` |
| Ordered | ✅ | ✅ | ❌ | ✅ (3.7+) |
| Mutable | ✅ | ❌ | ✅ | ✅ |
| Duplicates | ✅ | ✅ | ❌ | Keys: ❌ |
| Access by | Index | Index | — | Key |
| Use when | Ordered changeable data | Fixed data | Unique items | Key-value pairs |

---

<div align="center">

**Made with 💻 + ☕ while learning Python**

</div>
