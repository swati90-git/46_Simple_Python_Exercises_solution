# -*- coding: cp1252 -*-

"""Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language"). That is, double every consonant and place an occurrence of "o" in between.
For example, translate("this is fun") should return the string "tothohisos isos fofunon"."""

def translate(string):
    s =""
    vowel = ["a","e","i","o","u","A","E","I","O","U"," "]
    for i in string:
        if i in vowel:
            s += i
        else:
            s += i + "o" + i
    return s
print(translate("This is fun"))
