"""Define a function reverse() that computes the reversal of a string. For example, reverse("I am testing") should return the string "gnitset ma I"."""


def reverse(string):
    s=""
    for i in range(len(string)):
        s += string[-i-1]
    return s
print(reverse("str"))
print(reverse("I am testing"))       
