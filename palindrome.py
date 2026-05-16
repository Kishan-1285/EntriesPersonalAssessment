text = input("Enter text: ")
text = text.lower()
reverse = text[::-1]
if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")