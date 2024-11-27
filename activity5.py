temp = int(input("Enter the temperature in farenheit: "))

celcius = (temp - 32) * 5/9
converted = (round(celcius,2))

print(f"The Conversion of {temp} degrees farenheit is {converted}")
