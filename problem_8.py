"""Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome("radar") should return True."""

#1st method
def is_palindrome(string):
    s = ""
    for i in range(len(string)):
        s += string[-i-1]
    if s == string:
        return True
    else:
        return False

print(is_palindrome("radar"))
print(is_palindrome("abcba"))
print(is_palindrome("Was it a car or a cat I saw"))


# 2nd method
def is_palindrome(string):
    ab = ''
    length = len(string)
    for i in range(length):
        ab += string[length-1]
        length -= 1
    if string == ab:
        return True
    else:
        return False


print(is_palindrome("radar"))
print(is_palindrome("Was it a car or a cat I saw"))

