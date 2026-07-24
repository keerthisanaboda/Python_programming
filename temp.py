# Define a reusable function to handle the math formula
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Test the function with a specific degree input
c_temp = 30.0
f_temp = celsius_to_fahrenheit(c_temp)

print(f"{c_temp}°C is equal to {f_temp}°F")

#output: 30.0°C is equal to 86.0°F
