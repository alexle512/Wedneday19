word = input("Enter word to determine if it is a palindrome: ")

if word == word[::-1]:
    print("Word is a palindrome")
else:
    print("Word is not a palindrome")


