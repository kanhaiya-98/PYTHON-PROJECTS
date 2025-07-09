# ======================================================
#  Simple Unit Converter (Length & Temperature)
# ======================================================
# TODO 1: Import required modules
# Note: For this simple converter, built-ins are enough.

# ======================================================
# TODO 2: Define function to convert length units
def length_converter():
    # Step 1: Show options
    print("Length Converter")
    print("1. Meters to Kilometers")
    print("2. Kilometers to Meters")
    print("3. Meters to Miles")
    print("4. Miles to Meters")

    # Step 2: Get user choice
    choice = input("Choose a conversion (1-4): ")

    # Step 3: Get value to convert
    value = float(input("Enter the length value: "))

    # Step 4: Perform conversion
    if choice == '1':
        result = value / 1000
        print(f"{value} meters = {result} kilometers")
    elif choice == '2':
        result = value * 1000
        print(f"{value} kilometers = {result} meters")
    elif choice == '3':
        result = value * 0.000621371
        print(f"{value} meters = {result} miles")
    elif choice == '4':
        result = value / 0.000621371
        print(f"{value} miles = {result} meters")
    else:
        print("Invalid option.")

# ======================================================
# TODO 3: Define function to convert temperature units
def temperature_converter():
    # Step 1: Show options
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    # Step 2: Get user choice
    choice = input("Choose a conversion (1-4): ")

    # Step 3: Get value to convert
    value = float(input("Enter the temperature value: "))

    # Step 4: Perform conversion
    if choice == '1':
        result = (value * 9/5) + 32
        print(f"{value} °C = {result} °F")
    elif choice == '2':
        result = (value - 32) * 5/9
        print(f"{value} °F = {result} °C")
    elif choice == '3':
        result = value + 273.15
        print(f"{value} °C = {result} K")
    elif choice == '4':
        result = value - 273.15
        print(f"{value} K = {result} °C")
    else:
        print("Invalid option.")

# ======================================================
# TODO 4: Main Program Loop
def main():
    while True:
        # Step 1: Show main menu
        print("\nUnit Converter")
        print("1. Length Converter")
        print("2. Temperature Converter")
        print("3. Exit")

        # Step 2: Get user choice
        choice = input("Choose an option (1-3): ")

        # Step 3: Call selected function
        if choice == '1':
            length_converter()
        elif choice == '2':
            temperature_converter()
        elif choice == '3':
            print("Thank you for using the Unit Converter!")
            break
        else:
            print("Invalid choice. Please select again.")

# ======================================================
# TODO 5: Run the Program
if __name__ == "__main__":
    main()
