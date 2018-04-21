C:\Users\Kevin>python
Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)]
 on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import random
>>>
>>> class deck:
...     def __init__(self,data):
...             self.cards = data
...     def draw(self):
...             index = int(len(self.cards)*random.random())
...             start = index
...             while(self.cards[index] == 0):
...                     index += 1
...                     if(index>len(self.cards)):
...                             index = 0
...                     if(index == start):
...                             return((-1,random.random()*3))
...             self.removeCard(index)
...             return(index,int(random.random()*3))
...     def cardBack(self,i):
...             if(i>-1):
...                     self.cards[i]+=1
...     def removeCard(self,i):
...             self.cards[i]-=1
...     def removeHand(self,h):
...             for k in h:
...                     self.removeCard(k[0])
...
>>> data = [11,5,5,2,7,4,4,4,4]
>>> d = deck(data)
>>>
... class player:
...     d
...     def __init__(self):
...             self.hand = []
...     def draw(self):
...             self.hand.append(d.draw())
...             print(self.hand)
...     def cardBack(self,i):
...             d.cardBack(self.hand[i][0])
...             del self.hand[i]
...             print(self.hand)
...     def setHand(self,s):
...             self.hand=eval(s)
...             d.removeHand(self.hand)
...
...
>>> tim = player()
>>> tim.setHand("[(1, 0), (2, 2), (5, 0), (0, 2), (7, 2)]")
>>> cas = player()
>>> cas.setHand("[(8, 1), (1, 1), (2, 2), (4, 0), (2, 1)]")
>>> kev = player()
>>> kev.setHand("[(4, 0), (2, 1), (1, 1), (2, 1), (3, 1)]")
>>> tim.cardBack(1)
[(1, 0), (5, 0), (0, 2), (7, 2)]
>>> tim.cardBack(2)
[(1, 0), (5, 0), (7, 2)]
>>> tim.cardBack(2)
[(1, 0), (5, 0)]
>>> tim.draw()
[(1, 0), (5, 0), (8, 0)]
>>> tim.draw()
[(1, 0), (5, 0), (8, 0), (7, 2)]
>>> tim.removeCard(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'player' object has no attribute 'removeCard'
>>> tim.cardBack(3)
[(1, 0), (5, 0), (8, 0)]
>>> cas.draw()
[(8, 1), (1, 1), (2, 2), (4, 0), (2, 1), (4, 0)]