import math

class Polygon:
    """Base class for all polygons"""
    def __init__(self, name):
        self.name = name
    
    def area(self):
        """Calculate area of the polygon"""
        raise NotImplementedError("Subclasses must implement this method")
    
    def __str__(self):
        return f"{self.name} with area: {self.area():.2f}"

class Triangle(Polygon):
    """Triangle class inherits from Polygon"""
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height
    
    def area(self):
        """Calculate area of triangle: (base * height) / 2"""
        return (self.base * self.height) / 2

class Rectangle(Polygon):
    """Rectangle class inherits from Polygon"""
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width
    
    def area(self):
        """Calculate area of rectangle: length * width"""
        return self.length * self.width

class Square(Rectangle):
    """Square class inherits from Rectangle"""
    def __init__(self, side):
        super().__init__(side, side)
        self.name = "Square"

class Circle(Polygon):
    """Circle class inherits from Polygon"""
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        """Calculate area of circle: π * radius^2"""
        return math.pi * (self.radius ** 2)

def get_positive_number(prompt):
    """Helper function to get positive number input"""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    print("Polygon Area Calculator")
    print("1. Triangle")
    print("2. Rectangle")
    print("3. Square") 
    print("4. Circle")
    print("5. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            base = get_positive_number("Enter base of triangle: ")
            height = get_positive_number("Enter height of triangle: ")
            triangle = Triangle(base, height)
            print(triangle)
        
        elif choice == '2':
            length = get_positive_number("Enter length of rectangle: ")
            width = get_positive_number("Enter width of rectangle: ")
            rectangle = Rectangle(length, width)
            print(rectangle)
        
        elif choice == '3':
            side = get_positive_number("Enter side length of square: ")
            square = Square(side)
            print(square)
        
        elif choice == '4':
            radius = get_positive_number("Enter radius of circle: ")
            circle = Circle(radius)
            print(circle)
        
        elif choice == '5':
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1-5.")

if __name__ == "__main__":
    main()

