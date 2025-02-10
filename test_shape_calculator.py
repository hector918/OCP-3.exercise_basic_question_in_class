import unittest
from shape_calculator import ShapeCalculator, Circle, Rectangle, Square, Triangle

class TestShapeCalculator(unittest.TestCase):
    def setUp(self):
        """Create a ShapeCalculator instance before each test."""
        self.calculator = ShapeCalculator()

    def test_circle_area(self):
        """Test calculating the area of a circle."""
        circle = Circle(radius=5)
        self.assertEqual(self.calculator.calculate_area(circle), 78.5)

    def test_rectangle_area(self):
        """Test calculating the area of a rectangle."""
        rectangle = Rectangle(width=4, height=6)
        self.assertEqual(self.calculator.calculate_area(rectangle), 24)

    def test_square_area(self):
        """Test calculating the area of a square."""
        square = Square(side=3)
        self.assertEqual(self.calculator.calculate_area(square), 9)

    def test_triangle_area(self):
        """Test calculating the area of a triangle."""
        triangle = Triangle(base=5, height=10)
        self.assertEqual(self.calculator.calculate_area(triangle), 25)


if __name__ == "__main__":
    unittest.main()
