class ExpressionSolver:
    def __init__(self, expression):
        self.expression = expression

    def evaluate(self):
        try:
            # Use eval to evaluate the expression safely
            result = eval(self.expression)
            return result
        except Exception as e:
            return f"Error evaluating expression: {e}"

    def __str__(self):
        return f"Expression: {self.expression}"

# Example usage
if __name__ == "__main__":
    # Input expression from the user
    user_expression = input("Enter a mathematical expression (e.g., 2 + 3 * (4 - 1)): ")
    
    # Create an instance of ExpressionSolver
    solver = ExpressionSolver(user_expression)
    
    # Print the expression
    print(solver)
    
    # Evaluate and print the result
    result = solver.evaluate()
    print(f"Result: {result}")
