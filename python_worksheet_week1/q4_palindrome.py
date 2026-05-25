def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

print(is_palindrome("level"))
print(is_palindrome("Hello"))
print(is_palindrome("racecar"))
print(is_palindrome("A man a plan a canal Panama"))