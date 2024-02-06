"""
Long Andrew Q2
• Create an empty dictionary called dog
• Add name, color, breed, legs, age to the dog dictionary
• Create a student dictionary and add first_name, last_name, gender, age, marital status,
skills, country, city and address as keys for the dictionary
• Get the length of the student dictionary
• Get the value of skills and check the data type, it should be a list
• Modify the skills values by adding one or two skills
• Get the dictionary keys as a list
• Get the dictionary values as a list
"""

# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog = {
    "name": "Radar",
    "color": "Brown",
    "breed": "Poodle",
    "legs": 4,
    "age": 6,
}

# • Create a student dictionary and add first_name, last_name, gender, age,
# marital status, skills, country, city and address as keys for the dictionary
student = {
    "first_name": "Andrew",
    "last_name": "Long",
    "gender": "Male",
    "age": 20,
    "married": False,
    "Skills": ["C", "Python", "Java"],
    "country": "United States of America",
    "city": "Warrensburg",
    "address": "101 Market st."
}

# Get the length of the student dictionary
print(f"The length of student is {len(student)}")

# Get the value of skills and check the data type, it should be a list
type_of = type(student.get("Skills"))
print(f"The data type of skills in student dict is {type_of}")

# Modify the skills values by adding one or two skills
student.get("Skills").append("Spring Boot")

# • Get the dictionary keys as a list
print(f"The keys are {student.keys()}")
# • Get the dictionary values as a list
print(f"The values are {student.values()}")

