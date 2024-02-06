"""
Andrew long Q6
“I am a teacher and I love to inspire and teach people”
• How many unique words have been used in the sentence? Use the split methods and set
to get the unique words.
"""

# declare the string
given_string = "I am a teacher and I love to inspire and teach people"

# Split the string
lst_words = set(given_string.split())

# Count unique words
print(f"The length of unique words: {len(lst_words)}")
