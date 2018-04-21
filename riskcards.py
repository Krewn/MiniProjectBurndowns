import random

class deck:
	def __init__(self,data):
		self.cards = data
	def draw(self):
		index = int(len(self.cards)*random.random())
		start = index
		while(self.cards[index] == 0):
			index += 1
			if(index>len(self.cards)):
				index = 0
			if(index == start):
				return((-1,random.random()*3))
		self.cards[index]-=1
		return(index,int(random.random()*3))
	def cardBack(self,i):
		if(i>-1):
			self.data[i]+=1

data = [11,5,5,2,7,4,4,4,4]		
d = deck(data)
		
class player:
	d
	def __init__(self):
		self.hand = []
	def draw(self):
		self.hand.append(d.draw())
		print(self.hand)
	def cardBack(i):
		d.cardBack(self.hand[i][0])
		print(self.hand)

tim = player()
cas = player()
kev = player()