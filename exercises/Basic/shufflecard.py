#!usr/bin/python
#-*- coding=utf-8 -*-
#Python Program to shuffle a deck of card using the module random and draw 5 cards 
#import moudule
import itertools,random
# make a deck of cards 
deck =  list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
#shuffle the cards 
random.shuffle(deck)
#draws five cards 
print('You got:')
for i in range(5):
    output = str(deck[i][0])+' of '+str(deck[i][1])
    print(output)
