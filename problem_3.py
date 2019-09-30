"""Define a function that computes the length of a given list or string. (It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)"""


def length(list_str):
    c = 0
    for i in list_str:
        c+=1
    return c

print(length("swati"))
print(length(["sa","am","do","mu"]))



