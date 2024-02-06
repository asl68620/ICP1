"""
Long Andrew Q4
Find the length of the set it_companies
• Add 'Twitter' to it_companies
• Insert multiple IT companies at once to the set it_companies
• Remove one of the companies from the set it_companies
• What is the difference between remove and discard
• Join A and B
• Find A intersection B
• Is A subset of B
• Are A and B disjoint sets
• Join A with B and B with A
• What is the symmetric difference between A and B
• Delete the sets completely
• Convert the ages to a set and compare the length of the list and the set.
"""
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# • Add 'Twitter' to it_companies
it_companies.add("Twitter")

# Insert multiple IT companies at once to the set it_companies
it_companies = it_companies.union({"UCM", "TRUE", "GameStop"})

# • Remove one of the companies from the set it_companies
it_companies.remove("TRUE")

# • What is the difference between remove and discard
print("The difference between remove and discard is. That remove will raise an error if the item is not in the set")

# • Join A and B
A.update(B)
print(f"The joined set is: {A}")

# • Find A intersection B
print(f"{A.intersection(B)}")

# Is A subset of B
print(f"Is A subset of B? {A.issubset(B)}")

# • Are A and B disjoint sets
print(f"Are A and B disjoint sets: {A.isdisjoint(B)}")

# • Join A with B and B with A
A.union(B)
B.union(A)

print("The union sets are: ")
print(A)
print(B)

# • What is the symmetric difference between A and B
print(f"{A.symmetric_difference(B)}")

# • Delete the sets completely
del A
del B

# • Convert the ages to a set and compare the length of the list and the set.
print(f"Length of ages before set: {len(age)}")
print(f"Length of ages after set: {len(set(age))}")

