"""
Long Andrew question 1:
  Sort the list and find the min and max age
• Add the min age and the max age again to the list
• Find the median age (one middle item or two middle items divided by two)
• Find the average age (sum of all items divided by their number)
• Find the range of the ages (max minus min)
"""

# Following is a list of ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list
ages.sort()
print(ages)

# find min and max
print(f"The min is {ages[0]}")
print(f"The max is {ages[len(ages) - 1]}")
print(f"-" * 25)

# Find the median age (one middle item or two middle items divided by two)
print(f"The median age is {ages[len(ages) // 2]}")
print(f"-" * 25)

# Find the average age (sum of all items divided by their number)
# loop for counting total sum of all ages
total = 0
for i in range(len(ages)):
    # Add each age to the total
    total += ages[i]

# print results by dividing total by # of ages to get average
print(f"The average age is {total / len(ages)}")
print(f"-" * 25)

# Find the range of the ages (max minus min)
print(f"The range of the ages is {ages[len(ages)-1] - ages[0]}")
