"""Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers.
For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24."""



def sum_num(list_num):
    s = 0
    for i in list_num:
        s+=i
    return s

def multiply(list_num):
    a = 1
    for i in list_num:
        a *= i
    return a

l1 = [2,3,4,5]
print(sum_num(l1))
print(multiply(l1))
