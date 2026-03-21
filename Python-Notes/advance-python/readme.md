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
- [Chapter 3 — Error Handling](#chapter-3-error-handling)

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

> 🚧 *Coming soon...*

---

<div align="center">

**Made with 💻 + ☕ while learning Python**

</div>
