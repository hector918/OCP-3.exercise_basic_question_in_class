from abc import ABC, abstractmethod

class ShapeCalculator(ABC):
  @abstractmethod
  def process(self, **kwargs):
    pass

######################################################################
class circleCalulator(ShapeCalculator):
  def process(self, params):
    if "radius" not in params:
      raise ValueError("Parameter 'radius' not provided for circle calculation.") 
    radius = params["radius"]
    return 3.14 * radius * radius
  
class RectangleCalculator(ShapeCalculator):
  def process(self, params):
    if "width" not in params or "height" not in params:
      raise ValueError("Parameter 'width' or 'height' not provided for rectangle calculation.")
    
    width = params["width"]
    height = params["height"]
    area = width * height
    return area 
  
class squareCalculator(ShapeCalculator):
  def process(self, params):
    if "side" not in params:
      raise ValueError("Parameter 'side' not provided for square calculation.")
    side = params['side']
    return side * side