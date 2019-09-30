"""Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise."""


def check_vowel(string):
    string = string.lower()
    if string in ["a","e","i","o","u"]:
        return True
    else:
        return False

print(check_vowel("U"))
print(check_vowel("s"))
print(check_vowel("S"))
