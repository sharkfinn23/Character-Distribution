"""
distribution.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
import string
astring=(input("Please enter a string of text (the bigger the better): "))
print('The distribution of characters in "'+astring+'" is: ')
list=list(astring)
list1=[]
list1.extend([list.count('a'), list.count('b'), list.count('c'), list.count('d'), list.count('e'), list.count('f'), list.count('g'), list.count('h'), list.count('i'), list.count('j'), list.count('k'), list.count('l'), list.count('m'), list.count('n'), list.count('o'), list.count('p'), list.count('q'), list.count('r'), list.count('s'), list.count('t'), list.count('u'), list.count('v'), list.count('w'), list.count('x'), list.count('y'), list.count('z'),])
list2 = [x for x in range(1,27)]
list3 = list2[::-1]
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print(list2)
print(list3)
b=(zip(list1,list3,letters))
list4 = [x for x in b]
list4.sort(reverse=True)
print(list4)
print(list4[1][2])
c = 0
while c < 26:
    if list4[c][0] != 0:
        print(str(list4[c][2])*int(list4[c][0]))
    c += 1

    
