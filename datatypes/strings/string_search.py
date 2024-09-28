# String Search: Finding Substrings and Pattern Matching with Regex

import re

my_string = "The rain in Spain stays mainly in the plain."

# Finding substrings with regex
matches = re.findall("ain", my_string)
print("Occurrences of 'ain':", matches)  # Output: ['ain', 'ain', 'ain']
