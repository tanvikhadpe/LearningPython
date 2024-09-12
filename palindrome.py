def isPalindrome(s):
    # Remove spaces, punctuation and convert to lower case
    clean_string = ''.join(char.lower() for char in s if char.isalnum())

    # Check if the cleaned string is equal to its reverse
    return clean_string == clean_string[::-1]

strings = ["madam", "A man, a plan, a canal, Panama!", "hello", "12321", "Was it a car or cat I saw?"]
for string in strings:
    result = isPalindrome(string)
    print(f'"{string}" is a Palindrome: {result}')