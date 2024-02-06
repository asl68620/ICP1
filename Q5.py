import math
"""
The radius of a circle is 30 meters.
• Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
• Calculate the circumference of a circle and assign the value to a variable name of
_circum_of_circle_
• Take radius as user input and calculate the area
"""
# radius assignment
radius = 30.0

# Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
_area_of_circle_ = math.pi * math.pow(radius, 2)
print(f"Area with radius of 30: {_area_of_circle_}")

# Calculate the circumference of a circle and assign the value to a variable name of
# _circum_of_circle_
_circum_of_circle_ = 2 * math.pi * radius
print(f"circumference with radius of 30: {_circum_of_circle_}")

# Take radius as user input and calculate the area
radius = float(input("Enter in a radius: "))

_area_of_circle_ = math.pi * math.pow(radius,2)
print(f"The area is: {_area_of_circle_}")