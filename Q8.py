"""
Andrew Long Q8
Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
“The area of a circle with radius 10 is 314 meters square.”
"""

# print the template using string formating
print("%s = %d" % ("radius", 10))
print("%s = %.2f * %s ** %d" % ("Area", 3.14, "radius", 2))
print("The area of a circle with radius %d is %d meters square" % (10,314))
