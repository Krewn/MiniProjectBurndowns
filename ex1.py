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
...             self.cards[index]-=1
...             return(index,int(random.random()*3))
...     def cardBack(self,i):
...             if(i>-1):
...                     self.data[i]+=1
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
...     def cardBack(i):
...             d.cardBack(self.hand[i][0])
...             print(self.hand)
...
>>> tim = player()
>>> cas = player()
>>> kev = player()
>>> tim.draw()
[(1, 0)]
>>> cas.draw()
[(8, 1)]
>>> kev.draw
<bound method player.draw of <__main__.player object at 0x033EB350>>
>>> kev.draw()
[(4, 0)]
>>> tim.draw()
[(1, 0), (2, 2)]
>>> cas.draw()
[(8, 1), (1, 1)]
>>> kev.draw()
[(4, 0), (2, 1)]
>>> tim.draw()
[(1, 0), (2, 2), (5, 0)]
>>> cas.draw()
[(8, 1), (1, 1), (2, 2)]
>>> kev.draw()
[(4, 0), (2, 1), (1, 1)]
>>> tim.draw()
[(1, 0), (2, 2), (5, 0), (0, 2)]
>>> class bonus:
...     def __init__(self):
...             self.reward = 4
...             self.dif = 4
...     def give(self):
...             print(self.reward)
...             self.reward+=self.dif
...             self.dif+=2
...
>>> bonbons = bonus()
>>> cas.draw()
[(8, 1), (1, 1), (2, 2), (4, 0)]
>>> kev.draw()
[(4, 0), (2, 1), (1, 1), (2, 1)]
>>> tim.draw()
[(1, 0), (2, 2), (5, 0), (0, 2), (7, 2)]
>>> cas.draw()
[(8, 1), (1, 1), (2, 2), (4, 0), (2, 1)]
>>> kev.draw()
[(4, 0), (2, 1), (1, 1), (2, 1), (3, 1)]
>>> tim.hand
[(1, 0), (2, 2), (5, 0), (0, 2), (7, 2)]
>>> tim.cardBack(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: cardBack() takes 1 positional argument but 2 were given

