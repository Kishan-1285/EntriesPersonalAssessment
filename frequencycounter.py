import re
value = input("Enter the value: ")

words = re.findall(r"[A-Za-z]+", value)
word_count = {}
for word in words:
    key = word.lower()
    word_count[key] = word_count.get(key, 0) + 1

print("Word frequency:", word_count)
    
