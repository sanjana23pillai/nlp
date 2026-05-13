# Q15. Regex-based Text Cleaning
# Useful regex patterns for NLP lab exam

import re

text = """
Hello, World! This is NLP Lab-2025.
My email is student123@gmail.com
Visit https://example.com now!!!
Call me at 9876543210.
There are    extra     spaces here.
"""

print("Original text:")
print(text)

# 1. Convert to lowercase
# lower() makes all letters small
text = text.lower()

# 2. Remove URLs
# http\S+ removes links starting with http or https
text = re.sub(r"http\S+", "", text)

# 3. Remove email addresses
# \S+@\S+ removes text like abc@gmail.com
text = re.sub(r"\S+@\S+", "", text)

# 4. Remove phone numbers
# \d{10} removes exactly 10 digit numbers
text = re.sub(r"\d{10}", "", text)

# 5. Remove numbers
# \d+ removes one or more digits
text = re.sub(r"\d+", "", text)

# 6. Remove punctuation and special characters
# [^\w\s] removes anything that is not a word character or space
text = re.sub(r"[^\w\s]", "", text)

# 7. Remove underscores also
# \w keeps underscores, so we remove _ separately if needed
text = re.sub(r"_", "", text)

# 8. Remove extra spaces
# \s+ means one or more spaces/newlines/tabs
text = re.sub(r"\s+", " ", text)

# 9. Remove spaces from beginning and end
# strip() removes leading and trailing spaces
text = text.strip()

print("\nCleaned text:")
print(text)


# -------------------------------------------------
# Extra handy regex examples for viva / lab exam
# -------------------------------------------------

sample = "NLP Lab 2025: Contact abc@gmail.com or call 9876543210!"

# Find all numbers
# \d+ finds one or more digits
numbers = re.findall(r"\d+", sample)
print("\nNumbers found:", numbers)

# Find all words
# \b\w+\b finds complete words
words = re.findall(r"\b\w+\b", sample)
print("Words found:", words)

# Find email
# \S+@\S+ finds email-like patterns
emails = re.findall(r"\S+@\S+", sample)
print("Emails found:", emails)

# Replace digits with #
# Useful for masking numbers
masked = re.sub(r"\d", "#", sample)
print("Masked digits:", masked)

# Split sentence using punctuation
# [.!?] splits text at full stop, exclamation mark, or question mark
sentences = re.split(r"[.!?]", "I love NLP. It is easy! Is it useful?")
print("Sentence split:", sentences)