"""
Long andrew Q3
• Create a tuple containing names of your sisters and your brothers (imaginary siblings are
fine)
• Join brothers and sisters tuples and assign it to siblings
• How many siblings do you have?
• Modify the siblings tuple and add the name of your father and mother and assign it to
family_members
"""

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are #fine)
brothers = ("Joey", "Dan")
sisters = ("Chey", "Pam")

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# How many siblings do you have?
print(f"I have {len(siblings)} siblings")

# Modify the siblings tuple and add the name of your father and mother and assign it to
# family_members
mom_dad = ("Greg", "leaf")
siblings = siblings + mom_dad
family_members = siblings
