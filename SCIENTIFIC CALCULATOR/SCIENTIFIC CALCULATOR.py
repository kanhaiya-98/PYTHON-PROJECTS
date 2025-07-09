# ======================================================
#  Advanced Python Calculator
# ======================================================
# TODO 1: Import necessary modules
import sympy as sp
import math

# ======================================================
# TODO 2: Create function for Basic Arithmetic Operations
def basic_calculator():
    # Step 1: Show options to the user
    print("Basic Arithmetic Operations")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    # Step 2: Get user choice
    choice = input("Choose an operation (1-4): ")

    # Step 3: Get numbers from user
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    
    # Step 4: Perform chosen operation
    if choice == '1':
        result = a + b
    elif choice == '2':
        result = a - b
    elif choice == '3':
        result = a * b
    elif choice == '4':
        result = a / b if b != 0 else "Error: Division by zero!"
    else:
        result = "Invalid operation"
    
    # Step 5: Display result
    print(f"Result: {result}")

# ======================================================
# TODO 3: Create function for Scientific Functions
def scientific_functions():
    # Step 1: Show scientific function options
    print("Scientific Functions")
    print("1. Sine (sin)")
    print("2. Cosine (cos)")
    print("3. Tangent (tan)")
    print("4. Logarithm (log)")
    print("5. Square Root (sqrt)")

    # Step 2: Get user choice
    choice = input("Choose a function (1-5): ")

    # Step 3: Get input value
    angle_or_value = float(input("Enter the value (angle in degrees for trigonometric functions): "))

    # Step 4: Perform chosen function
    if choice == '1':
        result = math.sin(math.radians(angle_or_value))
    elif choice == '2':
        result = math.cos(math.radians(angle_or_value))
    elif choice == '3':
        result = math.tan(math.radians(angle_or_value))
    elif choice == '4':
        result = math.log(angle_or_value)  # natural log
    elif choice == '5':
        result = math.sqrt(angle_or_value)
    else:
        result = "Invalid function"
    
    # Step 5: Display result
    print(f"Result: {result}")

# ======================================================
# TODO 4: Create function to Differentiate an Expression
def differentiate_function():
    # Step 1: Define the symbol
    x = sp.symbols('x')

    # Step 2: Get function input from user
    func = input("Enter a function of x (e.g., x**2 + 3*x + 5): ")

    # Step 3: Convert input to sympy expression
    expr = sp.sympify(func)

    # Step 4: Differentiate the expression
    derivative = sp.diff(expr, x)

    # Step 5: Display result
    print(f"The derivative of {func} is: {derivative}")

# ======================================================
# TODO 5: Create function to Integrate an Expression
def integrate_function():
    # Step 1: Define the symbol
    x = sp.symbols('x')

    # Step 2: Get function input from user
    func = input("Enter a function of x to integrate (e.g., x**2 + 3*x + 5): ")

    # Step 3: Convert input to sympy expression
    expr = sp.sympify(func)

    # Step 4: Integrate the expression
    integral = sp.integrate(expr, x)

    # Step 5: Display result
    print(f"The integral of {func} is: {integral}")

# ======================================================
# TODO 6: Create function to Solve 3 Equations
def solve_equations():
    # Step 1: Define the symbols
    x, y, z = sp.symbols('x y z')

    # Step 2: Get equations from user
    eq1 = input("Enter the first equation (e.g., 2*x + 3*y + z = 1): ")
    eq2 = input("Enter the second equation (e.g., x - y + 2*z = 2): ")
    eq3 = input("Enter the third equation (e.g., 3*x + y - z = 3): ")

    # Step 3: Convert input to sympy equations
    equations = [
        sp.sympify(eq1.split('=')[0]) - sp.sympify(eq1.split('=')[1]),
        sp.sympify(eq2.split('=')[0]) - sp.sympify(eq2.split('=')[1]),
        sp.sympify(eq3.split('=')[0]) - sp.sympify(eq3.split('=')[1])
    ]

    # Step 4: Solve the system of equations
    solution = sp.solve(equations, (x, y, z))

    # Step 5: Display results
    print(f"The solution is: x = {solution[x]}, y = {solution[y]}, z = {solution[z]}")

# ======================================================
# TODO 7: Create the Main Program Loop
def main():
    while True:
        # Step 1: Show main menu
        print("\nAdvanced Calculator Options:")
        print("1. Basic Arithmetic")
        print("2. Scientific Functions")
        print("3. Differentiate a function")
        print("4. Integrate a function")
        print("5. Solve three equations")
        print("6. Exit")
        
        # Step 2: Get user choice
        choice = input("Choose an option (1-6): ")
        
        # Step 3: Call chosen function
        if choice == '1':
            basic_calculator()
        elif choice == '2':
            scientific_functions()
        elif choice == '3':
            differentiate_function()
        elif choice == '4':
            integrate_function()
        elif choice == '5':
            solve_equations()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

# ======================================================
# TODO 8: Run the Program
if __name__ == "__main__":
    main()
