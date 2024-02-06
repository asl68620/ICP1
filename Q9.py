import math

"""
Andrew Long Q9
Write a program, which reads weights (lbs.) of N students into a list and convert these weights to
kilograms in a separate list using Loop. N: No of students (Read input from user)
Ex: L1: [150, 155, 145, 148]
Output: [68.03, 70.3, 65.77, 67.13]
"""

# Enter the number of students from user
N = int(input("Number of students: "))

# Empty list
student_weights = []

# while loop to read in user weights
while N != 0:
    # read in weights, multiply to get Kgs, Round then append to empty list
    student_weights.append(round(int(input("Weight of students: ")) * 0.453592, 2))
    # iteration
    N = N - 1

# Print output
print(f"{student_weights}")
