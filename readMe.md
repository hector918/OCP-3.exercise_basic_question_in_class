Problem
You have been given a poorly designed program that calculates the area of different shapes. However, it violates the Open/Closed Principle (OCP) because every time a new shape is added, the calculate_area() function must be modified.

Your task is to identify the problem and refactor the code to follow OCP.

Instructions
1️. Look at the given bad code.

It has a function calculate_area() that checks the shape type using if-elif statements.
This violates OCP because adding a new shape requires modifying the function.
2️. Identify the issue.

What happens if we want to add a new shape (e.g., Triangle or Hexagon)?
Why is this bad for scalability?
3️. Refactor the code following OCP.

Convert the logic into an OCP-compliant design.
Use inheritance and polymorphism to remove the need for if-elif checks.
Make sure new shapes can be added without modifying existing code.
4️. Test your solution.

Ensure that new shapes can be added easily.
Run the program to verify your refactored solution.

running test:

python -m unittest test_shape_calculator.py
