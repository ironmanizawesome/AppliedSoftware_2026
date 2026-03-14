def f2c(temp_f):
    return (temp_f - 32) * 5/9

temp_f = float(input("Enter a temperature in Fahrenheit: "))
print(f"Temperature in Celsius: {f2c(temp_f):.2f}")