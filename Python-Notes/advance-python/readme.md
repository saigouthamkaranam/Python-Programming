# 🚀 Advance Python - Learning Notes

> Personal notes documenting my journey through Object-Oriented Programming in Python.  
> Written to solidify understanding — shared for anyone on the same path.

---

## 📚 Table of Contents

- [Chapter 2 — Object Oriented Programming](#chapter-2--object-oriented-programming)
  - [2.1 Advanced Data Types](#21-advanced-data-types)
  - [2.2 String Methods](#22-string-methods)
  - [2.3 Collections](#23-collections)
  - [2.4 Generators](#24-generators)
  - [2.5 Decorators](#25-decorators)
  - [2.6 Attribute Shadowing](#26-attribute-shadowing)
  - [2.7 Self Argument](#27-self-argument)
  - [2.8 Constructors and Init Function](#28-constructors-and-init-function)
  - [2.9 Inheritance and Composition](#29-inheritance-and-composition)
  - [2.10 Method Resolution Order (MRO)](#210-method-resolution-order-mro)
  - [2.11 The 3 Types of Methods](#211-the-3-types-of-methods-in-python)
  - [2.12 Static Methods](#212-static-methods)
  - [2.13 Class Methods](#213-class-methods)
  - [2.14 Property Decorators — Getters & Setters](#214-property-decorators--getters--setters)
- [Chapter 3 — Error Handling](#chapter-3--error-handling)
  - [3.1 Try-Except](#31-try-except)
  - [3.2 Try-Except-Else-Finally](#32-try-except-else-finally)
  - [3.3 Handling Multiple Exceptions](#33-handling-multiple-exceptions)
  - [3.4 Raising Exceptions](#34-raising-exceptions)
  - [3.5 Custom Exceptions](#35-custom-exceptions)
  - [3.6 Common Built-in Exceptions](#36-common-built-in-exceptions)
  - [3.7 File I/O](#37-file-io)
  - [3.8 File Handling using Try-Except](#38-file-handling-using-try-except)
 

---

## Chapter 2 — Object Oriented Programming

---

### 2.1 Advanced Data Types

Key modules for working with dates and times:

- `datetime` — date and time objects
- `time` — time access and conversions
- `calendar` — calendar-related utilities
- `timedelta` — duration between dates
- `arrow` — better dates and times for Python
- `dateutil` — extensions to the datetime module

---

### 2.2 String Methods

Commonly used string methods at a glance:

| Method | What it does | Example |
|---|---|---|
| `upper()` | Converts to uppercase | `'hello'.upper()` → `'HELLO'` |
| `lower()` | Converts to lowercase | `'HELLO'.lower()` → `'hello'` |
| `strip()` | Removes leading/trailing whitespace | `'  hi  '.strip()` → `'hi'` |
| `lstrip()` | Removes leading whitespace | `'  hi  '.lstrip()` → `'hi  '` |
| `rstrip()` | Removes trailing whitespace | `'  hi  '.rstrip()` → `'  hi'` |
| `replace(old, new)` | Replaces substring | `'hello'.replace('l', 'r')` → `'herro'` |
| `split(sep)` | Splits string into a list | `'a,b,c'.split(',')` → `['a','b','c']` |
| `join(iterable)` | Joins list into a string | `','.join(['a','b'])` → `'a,b'` |
| `find(sub)` | Returns index of substring, -1 if not found | `'hello'.find('l')` → `2` |
| `index(sub)` | Like find() but raises error if not found | `'hello'.index('l')` → `2` |
| `count(sub)` | Counts occurrences of substring | `'hello'.count('l')` → `2` |
| `startswith(prefix)` | Checks if string starts with prefix | `'hello'.startswith('he')` → `True` |
| `endswith(suffix)` | Checks if string ends with suffix | `'hello'.endswith('lo')` → `True` |
| `capitalize()` | Capitalizes first character | `'hello'.capitalize()` → `'Hello'` |
| `title()` | Capitalizes first letter of each word | `'hello world'.title()` → `'Hello World'` |
| `swapcase()` | Swaps upper to lower and vice versa | `'Hello'.swapcase()` → `'hELLO'` |
| `isalpha()` | Checks if all characters are letters | `'hello'.isalpha()` → `True` |
| `isdigit()` | Checks if all characters are digits | `'123'.isdigit()` → `True` |
| `isalnum()` | Checks if all chars are letters or digits | `'abc123'.isalnum()` → `True` |
| `islower()` | Checks if all characters are lowercase | `'hello'.islower()` → `True` |
| `isupper()` | Checks if all characters are uppercase | `'HELLO'.isupper()` → `True` |
| `zfill(width)` | Pads string with zeros on the left | `'42'.zfill(5)` → `'00042'` |
| `format()` | Formats string with variables | `'Hi {}'.format('John')` → `'Hi John'` |

---

### 2.3 Collections

Python's `collections` module provides specialized container datatypes beyond the built-in `list`, `dict`, `set`, and `tuple`.

📖 [Official Docs → collections](https://docs.python.org/3/library/collections.html)

---

### 2.4 Generators

A **generator function** uses `yield` instead of `return` to produce a series of values lazily — pausing and resuming execution between each yield.

```python
def fun(max):
    cnt = 1
    while cnt <= max:
        yield cnt
        cnt += 1

ctr = fun(5)
for n in ctr:
    print(n)
# Output: 1 2 3 4 5
```

#### Why use Generators?

| Reason | Explanation |
|---|---|
| 🧠 Memory Efficient | Handle large or infinite data without loading everything into memory |
| ⚡ No List Overhead | Yield items one by one, avoiding full list creation |
| 💤 Lazy Evaluation | Compute values only when needed |
| ♾️ Infinite Sequences | Ideal for unbounded data like Fibonacci series |
| 🔗 Pipeline Processing | Chain generators to process data in stages |

#### Syntax

```python
def generator_function_name(parameters):
    # Your code here
    yield expression
```

#### Simple Example

```python
def fun():
    yield 1
    yield 2
    yield 3

for val in fun():
    print(val)
# Output: 1  2  3
```

#### Real World Use Case

Generators are especially useful for processing large data files (like logs) — they handle data in small chunks without loading the entire file into memory.

---

### 2.5 Decorators

A decorator is essentially a **wrapper around your function** — it adds behavior before and/or after the function runs without modifying the function itself.

```python
def my_decorator(func):
    def wrapper():
        print("Hello")
        func()
        print("The End")
    return wrapper

@my_decorator
def greet():
    print("I am G")

greet()
# Output:
# Hello
# I am G
# The End
```

> **Preserving Metadata:** Use `@wraps` from `functools` to preserve the original function's metadata (name, docstring, etc.).

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Hello")
        func()
        print("The End")
    return wrapper
```

---

### 2.6 Attribute Shadowing

Attribute shadowing occurs when a variable in a local/inner scope has the **same name** as one in an outer scope, making the outer variable inaccessible within that scope.

```python
class Movies:
    length = 180  # class attribute

action_movies = Movies()
print(action_movies.length)   # 180

# Shadow the class attribute on the instance
action_movies.length = 210
action_movies.budget = 100

print(action_movies.length)   # 210 (instance attribute shadows class attribute)

# Delete the instance attribute
del action_movies.length
print(action_movies.length)   # 180 (falls back to class attribute ✅)

# Delete an instance-only attribute
del action_movies.budget
print(action_movies.budget)   # AttributeError! — not in the class either
```

> **Key insight:** When you `del` an instance attribute, Python falls back to the class attribute. If the class doesn't have it either, you get an `AttributeError`. That "looking back" behavior is attribute shadowing.

---

### 2.7 Self Argument

`self` is a reference to **the current instance** — it gives you access to all properties and methods defined in the class.

```python
class Movies:
    length = 180

    def describe(self):
        return self.length

# Calling directly on the class without self → Error
print(Movies.describe())          # ❌ TypeError

# Correct ways:
comedy_movies = Movies()

print(comedy_movies.describe())           # ✅ via object reference
print(Movies.describe(comedy_movies))     # ✅ via explicit object as parameter
```

---

### 2.8 Constructors and Init Function

#### What is a Constructor?

A constructor is a **special method that automatically runs when you create an object**. Its job is to initialize the object's attributes with values.

> In Python, you can't declare a variable like `int age;` (as in C). Constructors solve this by letting you declare and initialize variables at object creation time.

The constructor in Python is the `__init__` method:

```python
class Car:
    def __init__(self, type_, brand, color, price):
        self.type_ = type_
        self.brand = brand
        self.color = color
        self.price = price

car1 = Car("Sedan", "Toyota", "Red", 20000)
# The moment this runs, __init__ automatically fills in all attributes ✅
```

> ⚙️ **A constructor is a method that automatically runs when an object is created and sets up its initial values.**

---

### 2.9 Inheritance and Composition

---

#### 2.9.1 Inheritance

Inheritance means **one class automatically gets all the properties and methods of another class**.

**Real world analogy 🧬** — Think of genes in a family. A child automatically inherits traits from a parent, and can also have its own unique features.

```python
# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

# Child Class
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")

dog1 = Dog("Bruno")
dog1.eat()    # ✅ inherited from Animal
dog1.sleep()  # ✅ inherited from Animal
dog1.bark()   # ✅ Dog's own method
```

---

#### 2.9.2 Composition

Composition means **a class contains an object of another class as its attribute**.

**Real world analogy 🚗** — A Car HAS an Engine. The Car doesn't inherit from Engine — it just uses Engine as a part.

```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine with {self.horsepower}hp started!")

class Car:
    def __init__(self, name, horsepower):
        self.name = name
        self.engine = Engine(horsepower)  # Car HAS an Engine

    def start_car(self):
        print(f"{self.name} is starting...")
        self.engine.start()

car1 = Car("Toyota", 150)
car1.start_car()
# Toyota is starting...
# Engine with 150hp started!
```

---

#### 2.9.3 Key Difference

| | Inheritance | Composition |
|---|---|---|
| Relationship | **IS A** | **HAS A** |
| Example | Dog **IS A** Animal | Car **HAS A** Engine |
| How | `class Dog(Animal)` | `self.engine = Engine()` |
| Gets | All parent properties | Only what it uses |

> **Simple rule:** IS A → Inheritance &nbsp;|&nbsp; HAS A → Composition

---

#### 2.9.4 Accessing the Base Class — 3 Methods

**Method 1: Code Duplication** ❌ (avoid)

```python
class SportsCar(Car):
    def __init__(self, type_, brand, color):
        self.type_ = type_   # duplicated from Car
        self.brand = brand   # duplicated from Car
        self.color = color
```

**Method 2: Explicit Call**

```python
class SportsCar(Car):
    def __init__(self, type_, brand, color):
        Car.__init__(self, type_, brand)  # explicit parent call
        self.color = color
```

**Method 3: `super()` ✅ (preferred)**

```python
class SportsCar(Car):
    def __init__(self, type_, brand, color):
        super().__init__(type_, brand)  # clean and future-proof
        self.color = color
```

---

### 2.10 Method Resolution Order (MRO)

MRO is the **order Python follows to search for a method** when it's called.

#### Single Inheritance — Simple

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog1 = Dog()
dog1.speak()
# Search order → Dog → Animal
# Output → "Dog barks" ✅
```

#### Multiple Inheritance — Where MRO matters

```python
class A:
    def hello(self): print("Hello from A")

class B(A):
    def hello(self): print("Hello from B")

class C(A):
    def hello(self): print("Hello from C")

class D(B, C):  # inherits from BOTH B and C
    pass

d1 = D()
d1.hello()
# Search order → D → B → C → A
# Output → "Hello from B" ✅
```

Python uses the **C3 Linearization algorithm** to determine this order.

#### The Diamond Problem

```
        A
       / \
      B   C
       \ /
        D

Search order → D → B → C → A → object
```

MRO solves the diamond problem cleanly — each class is searched exactly once, left to right, bottom to top.

#### Checking MRO

```python
print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)

print(D.mro())
# [D, B, C, A, object]
```

---

### 2.11 The 3 Types of Methods in Python

```python
class Car:
    def instance_method(self):     # works with object data
        ...

    @classmethod
    def class_method(cls):         # works with class data
        ...

    @staticmethod
    def static_method():           # works independently
        ...
```

---

### 2.12 Static Methods

A static method **belongs to the class but doesn't need any object or class data** to work.

**Analogy 🚗** — Think of a calculator inside a car showroom. It lives inside the showroom but doesn't need to know anything about the cars — it just does its own job independently.

```python
class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    @staticmethod
    def convert_currency(price, rate):  # no self needed
        return price * rate

# Call WITHOUT an object
print(Car.convert_currency(20000, 83))   # 1660000 ✅

# Also works WITH an object
car1 = Car("Toyota", 20000)
print(car1.convert_currency(20000, 83))  # 1660000 ✅
```

#### When to use Static Methods?

Use them when the method:
- Does **NOT** need object data (`self`)
- Does **NOT** need class data (`cls`)
- Is just a **utility/helper function** that logically belongs in the class

#### Summary

| | Instance Method | Static Method |
|---|---|---|
| Has `self` | ✅ Yes | ❌ No |
| Needs object data | ✅ Yes | ❌ No |
| Called with object | ✅ Yes | ✅ Yes |
| Called without object | ❌ No | ✅ Yes |
| Decorator | None | `@staticmethod` |

---

### 2.13 Class Methods

A class method works with the **class itself**, not with any specific object. It uses `cls` instead of `self`.

```python
class Car:
    total_cars = 0  # class variable

    def __init__(self, brand):
        self.brand = brand
        Car.total_cars += 1

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars

car1 = Car("Toyota")
car2 = Car("BMW")
print(Car.get_total_cars())  # 2 ✅
```

> `self` → refers to the **object** (car1, car2) &nbsp;|&nbsp; `cls` → refers to the **class** (Car itself)

#### All 3 Method Types Together

```python
class Car:
    total_cars = 0

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        Car.total_cars += 1

    def show_brand(self):                        # instance method
        print(self.brand)

    @classmethod
    def get_total_cars(cls):                     # class method
        print(cls.total_cars)

    @staticmethod
    def convert_currency(price, rate):           # static method
        return price * rate

car1 = Car("Toyota", 20000)
car1.show_brand()                 # Toyota ✅
Car.get_total_cars()              # 1 ✅
Car.convert_currency(20000, 83)   # 1660000 ✅
```

#### Summary Table

| | Instance Method | Class Method | Static Method |
|---|---|---|---|
| Decorator | None | `@classmethod` | `@staticmethod` |
| First parameter | `self` | `cls` | nothing |
| Accesses | Object data | Class data | Nothing |
| Use case | Object-specific tasks | Class-level tasks | Utility functions |

#### Quick Decision Rule

| Need object data? | Need class data? | Use |
|---|---|---|
| ✅ | ❌ | Instance method |
| ❌ | ✅ | Class method |
| ❌ | ❌ | Static method |

#### Bank Analogy 🏦

| Method | Example |
|---|---|
| Instance method | "Show **MY** balance" — specific to one account |
| Class method | "How many **total accounts** exist in the bank?" |
| Static method | "Is this **amount valid**?" — just a calculation |

---

### 2.14 Property Decorators — Getters & Setters

#### The Problem Without Protection

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

acc1 = BankAccount(5000)
acc1.balance = -10000  # ❌ anyone can set an invalid balance!
```

#### Solution — Getters & Setters

- **Getter** → controls how you **read** a value
- **Setter** → controls how you **set/update** a value

#### Old Way (verbose)

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount < 0:
            print("Invalid amount!")
        else:
            self.__balance = amount

acc1 = BankAccount(5000)
acc1.set_balance(-100)     # Invalid amount!
acc1.set_balance(8000)     # ✅
print(acc1.get_balance())  # 8000
```

#### Clean Way — `@property` Decorator ✅

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    @property
    def balance(self):            # getter
        return self.__balance

    @balance.setter
    def balance(self, amount):    # setter
        if amount < 0:
            print("Invalid amount!")
        else:
            self.__balance = amount

acc1 = BankAccount(5000)
print(acc1.balance)    # 5000 ✅ — getter called automatically
acc1.balance = -100    # Invalid amount! ✅ — setter called automatically
acc1.balance = 8000    # ✅
print(acc1.balance)    # 8000 ✅
```

Looks like a **normal variable** but secretly runs validation! 🔐

#### Double Underscore `__` — Private Variables

```python
self.__balance   # strictly private
```

| Convention | Meaning |
|---|---|
| `_x` | "Please don't touch" (soft private) |
| `__x` | Strictly private — cannot be accessed directly |

```python
acc1.__balance  # ❌ AttributeError
acc1.balance    # ✅ access only through getter/setter
```

#### Summary

| | Getter | Setter |
|---|---|---|
| Decorator | `@property` | `@balance.setter` |
| Purpose | Read value | Update value |
| Looks like | Normal variable access | Normal variable assignment |

> **Simple Rule:**  
> `@property` → controls **reading** &nbsp;|&nbsp; `@x.setter` → controls **updating** &nbsp;|&nbsp; `__` → makes variable **private**

---

## Chapter 3 — Error Handling

---

### 3.1 Try-Except
 
We use `try-except` to handle a program gracefully from crashing in case of an exception or error during runtime.
 
When something goes wrong at runtime (like accessing a key that doesn't exist), Python stops the entire program right there. To get past this, we use **exception handling** with `try` and `except` blocks.
 
#### ❌ Without Exception Handling
 
```python
car_parts = {"wheels": 20, "rim": 10, "seat_covers": 10, "spray_paint": 20}
 
print(car_parts["dashcam"])
 
# Output:
# KeyError: 'dashcam'
```
 
Since `dashcam` is not a key in the dictionary, Python throws a `KeyError` and the program crashes.
 
#### ✅ With Exception Handling
 
```python
car_parts = {"wheels": 20, "rim": 10, "seat_covers": 10, "spray_paint": 20}
 
try:
    print(car_parts["dashcam"])
except KeyError:
    print("The key that you are trying to access does not exist")
 
print(car_parts["wheels"])
 
# Output:
# The key that you are trying to access does not exist
# 20
```
 
> The program **does not crash** — it handles the error gracefully and continues executing.
 
---
 
### 3.2 Try-Except-Else-Finally
 
You can extend the `try-except` block with two optional clauses:
 
- `else` → runs **only if no exception occurred**
- `finally` → **always runs**, no matter what
 
```python
def paint_car(color):
    try:
        print(f"Painting your car {color}!")
        if color == "unknown":
            raise ValueError("We don't have this color")
    except ValueError as e:
        print("Error:", e)
    else:
        print(f"Your car is painted {color}!")
    finally:
        print("Next customer please!\n")
 
paint_car("red")
paint_car("unknown")
 
# Output:
# Painting your car red!
# Your car is painted red!
# Next customer please!
#
# Painting your car unknown!
# Error: We don't have this color
# Next customer please!
```
 
#### 📋 Block Summary
 
| Block | When does it run? |
|---|---|
| `try` | Always — this is the code you want to attempt |
| `except` | Only if an exception was raised inside `try` |
| `else` | Only if NO exception was raised |
| `finally` | Always — regardless of success or failure |
 
---
 
### 3.3 Handling Multiple Exceptions
 
You can handle different types of errors differently using multiple `except` blocks.
 
```python
def process_input(value):
    try:
        result = 100 / int(value)
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except ValueError:
        print("Error: Invalid input — please enter a number!")
    except Exception as e:
        print(f"Unexpected error: {e}")
 
process_input(5)        # Result: 20.0
process_input(0)        # Error: Cannot divide by zero!
process_input("hello")  # Error: Invalid input — please enter a number!
```
 
> `Exception` acts as a **catch-all** — always put it last.
 
#### 📦 Catching Multiple Exceptions in One Block
 
```python
try:
    value = int(input("Enter a number: "))
    result = 100 / value
except (ValueError, ZeroDivisionError) as e:
    print(f"Handled error: {e}")
```
 
---
 
### 3.4 Raising Exceptions
 
You can manually trigger an exception using `raise` — useful for enforcing rules in your own code.
 
```python
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print(f"Age set to {age}")
 
set_age(25)   # Age set to 25
set_age(-5)   # ValueError: Age cannot be negative!
```
 
---
 
### 3.5 Custom Exceptions
 
You can create your own exception types by inheriting from `Exception`.
 
```python
class InsufficientFundsError(Exception):
    pass
 
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Not enough balance to withdraw!")
    return balance - amount
 
try:
    withdraw(500, 1000)
except InsufficientFundsError as e:
    print(f"Bank Error: {e}")
 
# Output:
# Bank Error: Not enough balance to withdraw!
```
 
> Custom exceptions make your error messages **descriptive and domain-specific** — much easier to debug than generic errors.
 
---
 
### 3.6 Common Built-in Exceptions
 
| Exception | When it occurs |
|---|---|
| `ValueError` | Right type, wrong value — `int("hello")` |
| `TypeError` | Wrong type entirely — `"5" + 5` |
| `KeyError` | Dict key doesn't exist — `d["missing"]` |
| `IndexError` | List index out of range — `lst[99]` |
| `ZeroDivisionError` | Dividing by zero — `10 / 0` |
| `AttributeError` | Attribute doesn't exist — `obj.unknown` |
| `FileNotFoundError` | File doesn't exist when opening |
| `ImportError` | Module can't be imported |
| `NameError` | Variable used before it's defined |
| `StopIteration` | Iterator has no more items |
| `Exception` | Base class — catches everything |
 
> **Key rules:** Handle **specific exceptions first**, then fall back to `Exception` as a last resort.
 
---
 
### 3.7 File I/O
 
File I/O (Input/Output) is how Python **reads from and writes to files** on your system. Think of it like opening a notebook, reading or writing something, and then closing it when you're done.
 
#### 📂 Opening a File — `open()`
 
```python
file = open("filename.txt", mode)
```
 
| Mode | What it does |
|---|---|
| `"r"` | Read — opens file for reading (default) |
| `"w"` | Write — creates file or overwrites existing content |
| `"a"` | Append — adds to the end without overwriting |
| `"x"` | Create — creates a new file, fails if it already exists |
| `"rb"` | Read binary — for images, PDFs, etc. |
| `"wb"` | Write binary — for images, PDFs, etc. |
 
#### 📖 Reading a File
 
```python
# Read the entire file as one string
file = open("notes.txt", "r")
content = file.read()
print(content)
file.close()
 
# Read line by line into a list
file = open("notes.txt", "r")
lines = file.readlines()
for line in lines:
    print(line.strip())
file.close()
 
# Read one line at a time
file = open("notes.txt", "r")
line = file.readline()
print(line)
file.close()
```
 
| Method | What it returns |
|---|---|
| `read()` | Entire file as a single string |
| `readlines()` | List of all lines |
| `readline()` | One line at a time |
 
#### ✍️ Writing to a File
 
```python
# Write — creates file or overwrites existing content
file = open("notes.txt", "w")
file.write("Hello, G!\n")
file.write("This is my Python notes file.\n")
file.close()
 
# Append — adds to the end without erasing existing content
file = open("notes.txt", "a")
file.write("Adding a new line at the bottom.\n")
file.close()
```
 
> ⚠️ `"w"` mode **erases all existing content** before writing. Use `"a"` if you want to keep what's already there.
 
#### ✅ The Better Way — `with` Statement (Context Manager)
 
Always prefer `with open(...)` over manually calling `open()` and `close()`. It automatically closes the file even if an error occurs.
 
```python
# Reading
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
# File is automatically closed here ✅
 
# Writing
with open("notes.txt", "w") as file:
    file.write("Clean and safe file writing!\n")
 
# Appending
with open("notes.txt", "a") as file:
    file.write("One more line added.\n")
```
 
#### 🔁 Iterating Over a File Line by Line
 
```python
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())
```
 
> Most **memory-efficient** way to read large files — reads one line at a time without loading everything into memory. Same concept as generators.
 
#### 🗑️ Other File Operations
 
```python
import os
 
os.path.exists("notes.txt")             # Check if file exists → True or False
os.remove("notes.txt")                  # Delete a file
os.rename("old_name.txt", "new.txt")    # Rename a file
os.path.getsize("notes.txt")            # Get file size in bytes
```
 
---
 
### 3.8 File Handling using Try-Except
 
Combining file operations with `try-except` makes your code **safe and crash-proof** — files might not exist, might be locked, or the disk might be full.
 
#### 🔐 Safe File Reading
 
```python
try:
    with open("notes.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file does not exist!")
except PermissionError:
    print("Error: You don't have permission to read this file!")
except Exception as e:
    print(f"Unexpected error: {e}")
```
 
#### ✍️ Safe File Writing
 
```python
try:
    with open("notes.txt", "w") as file:
        file.write("Writing safely with error handling!\n")
    print("File written successfully!")
except PermissionError:
    print("Error: Cannot write — permission denied!")
except OSError as e:
    print(f"OS Error: {e}")
```
 
#### 🔄 Real World Example — Reading a Config File
 
```python
def load_config(filepath):
    try:
        with open(filepath, "r") as file:
            config = {}
            for line in file:
                line = line.strip()
                if "=" in line:
                    key, value = line.split("=", 1)
                    config[key.strip()] = value.strip()
            return config
    except FileNotFoundError:
        print(f"Config file '{filepath}' not found. Using defaults.")
        return {}
    except Exception as e:
        print(f"Failed to load config: {e}")
        return {}
 
settings = load_config("config.txt")
print(settings)
```
 
#### 🔄 Real World Example — Writing a Log File
 
```python
def write_log(message, filepath="app.log"):
    try:
        with open(filepath, "a") as file:
            file.write(f"{message}\n")
    except PermissionError:
        print("Cannot write to log — permission denied!")
    except OSError as e:
        print(f"Log write failed: {e}")
    else:
        print(f"Log written: {message}")
    finally:
        print("Log operation complete.")
 
write_log("App started")
write_log("User logged in: G")
```
 
#### 📋 File I/O + Exception Cheat Sheet
 
| Scenario | Exception to catch |
|---|---|
| File doesn't exist | `FileNotFoundError` |
| No permission to read/write | `PermissionError` |
| Disk is full | `OSError` |
| Reading a corrupted binary file | `UnicodeDecodeError` |
| Any other file error | `OSError` / `Exception` |
 
#### 🧠 Key Takeaways
 
- Always use `with open(...)` — it handles closing automatically, even on errors
- `"r"` to read, `"w"` to write (overwrites), `"a"` to append, `"x"` to create new
- Wrap file operations in `try-except` to catch `FileNotFoundError` and `PermissionError`
- Use `finally` for cleanup logic that must always run
- For large files, iterate line by line instead of `read()` to save memory
 
---
 
<div align="center">
 
**✨ Made with 💻 + ☕ while learning Python - `By Sai Goutham Karanam` ✨**
 
</div>
