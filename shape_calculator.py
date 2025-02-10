class Shape:
  pass

class ShapeCalculator:
  def calculate_area(self, shape):
    if not isinstance(shape, Shape):
      raise TypeError("Expected a Square instance.")
    return shape.process()
######################################################################
class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius
  def process(self):
    return 3.14 * self.radius ** 2
  
class Rectangle(Shape):
  def __init__(self, width, height):
    self.width = width
    self.height = height
  def process(self):
    return self.width * self.height
 
class Square(Shape):
  def __init__(self, side):
    self.side = side
  def process(self):
    return self.side ** 2

class Triangle(Shape):  
  def __init__(self, base, height):
    self.base = base
    self.height = height
  def process(self):
    return 0.5 * self.base * self.height