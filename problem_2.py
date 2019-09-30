"""Define a function max_of_three() that takes three numbers as arguments and returns the largest of them."""
def max_three(a,b,c):
    max_num = a
    if b> max_num:
        max_num= b
    if c> max_num:
        max_num = c
    return(max_num)

print(max_three(5,9,23))
print(max_three(15,6,9))
