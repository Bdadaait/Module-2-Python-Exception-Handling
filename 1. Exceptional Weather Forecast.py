
# Task 1: Start

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit- 32) * 5/9

def main():  #Task 2: Temperature Conversion
    try:
        fahrenheit_input = input("Please enter the temperature in Fahrenheit: ")
        fahrenheit = float(fahrenheit_input)
        celsius = fahrenheit_to_celsius (fahrenheit)

    except ValueError:
        print("invalid input. Please enter a numeric value for the temperature.")

    else:     #Task 3: User Experience
        print(f"{fahrenheit} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")

    finally:  #Task 4: Finally
        print(" Thank you for using the weather forecast application.")

main()