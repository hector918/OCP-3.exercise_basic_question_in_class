from shape_calculator import Circle, Rectangle, Square, Triangle


class ShapeCalculator:
    """A bad implementation that violates the Open/Closed Principle (OCP)."""

    def calculate_area(self, shape, dimensions):
        """Calculates the area based on the shape type."""

        shape_selector = {
            "circle": Circle,
            "rectangle": Rectangle,
            "square": Square
        }

        try:
            if shape in shape_selector:
                calculator = shape_selector[shape](**dimensions)
                return calculator.process()
            else:
                return "Unsupported shape."
        except Exception as e:
            return e
        
# Example usage
calculator = ShapeCalculator()
print(calculator.calculate_area("circle", {"radius": 5}))
print(calculator.calculate_area("rectangle", {"width": 4, "height": 6}))
print(calculator.calculate_area("square", {"side": 3}))
print(calculator.calculate_area("triangle", {"base": 5, "height": 10}))
