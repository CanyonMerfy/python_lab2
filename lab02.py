import math

# Part 1
name = "Canyon"
age = 19
height = 6.5
favorite_color = "Blue"

print(name)
print(age)
print(height)
print(favorite_color)

print(name, age, height, favorite_color)
print(f"Hello: {name} my is {favorite_color}!")

print(f"Hi my name is {name}, I am {age} years old, I'm {height} feet tall, and my favorite color is {favorite_color}")

print(f"""
Name = {name}
Age = {age}
Height = {height}"
Favorite Color = {favorite_color}
""")

circle_area = math.pi * 5 ** 2
print(f"{circle_area:.1f}")

# Part 2

print(math.sqrt(age))
print(math.sin(height))
print(math.cos(height))

# Part 3
print(age + 5)
print(height - 4)
print(age * height)
print(height / 2)
print(age % 3)
print(age ** 2)


# Part 4

def temperature_conversion(fahrenheit):
    Celsius = (fahrenheit - 32) * 5/9
    print(Celsius)

f_number = input("Input a number: ")
print(temperature_conversion(int(f_number)))