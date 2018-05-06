#!usr/bin/python
#-*- coding=utf-8 -*-
setx = set(["apple","mango"])
sety = set(["mango","aplle"])
setc = setx ^ sety
print'setc=setx ^ sety ',setc,'=',setx,' ^ ',sety
x = frozenset([1,2,3,4,5])
y = frozenset([3,4,5,6,7])
print(x.isdisjoint(y)) # use isdisjoint to judge if the ser has no elements in common with the other
print(x.difference(y)) # use difference to return different elements
print(x|y) # use '|' to  generate set from x and y
sety = set(["mango","orange"])
setz = set(["mango"])
issubset =  setz <= sety
print(issubset)
issubset = (setz <= setx)
print(issubset)
