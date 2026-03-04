'''
**Problem 1 — Shape Area Calculator**
```
Create the following classes:
- Shape → has method area() → returns 0
- Rectangle(Shape) → overrides area() → length * width
- Circle(Shape) → overrides area() → π * r²
- Square(Rectangle) → overrides area() → side²

Create objects of each and call area().
Print MRO of Square.
'''

class Shape():
    length = 0
    width = 0
    def Area():
        pass

class Rectangle(Shape):

    def Area(length,width):
        return length * width
    
class Circle(Shape):

    def Area(radius):
        return 3.14 * radius * radius

class Square(Rectangle):

    def Area(side):
        return side * side

print(Rectangle.Area(4,5))
print(Circle.Area(4))
print(Square.Area(5))
