"""Donkey_kong_game"""


from random import *
import os
import threading
import time

def getchar():
	"""Returns a single character from standard input""" """Function taken from Github : https://gist.github.com/jasonrdsouza/1901709"""
	import tty, termios,sys   
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:  
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch

class Screen:

	"""2D LIST FOR BOARD"""
	def __init__(self,score):
		self.__score=score
		self.__a=[['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
				['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X',' ',' ','Q',' ',' ',' ',' ',' ',' ','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
				['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X','X','X','X','X','X','X','X','X','X','X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
				['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
				['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
				['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X',' ',' ',' ',' ',' ',' ',' ',' ','X'],
				['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
				['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
				['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
				['X',' ',' ',' ',' ',' ',' ',' ',' ','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
				['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
				['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
				['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
				['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X',' ',' ',' ',' ',' ',' ',' ',' ','X'],
				['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
				['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
				['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
				['X',' ',' ',' ',' ',' ',' ',' ',' ','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X'],
				['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
				['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
				['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
				['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X',' ',' ',' ',' ',' ',' ',' ',' ','X'],
				['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
				['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
				['X',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','X'],
				['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X']]
		for i in range(2,6):
			self.__a[i][33]='H'
		for i in range(5,9):
			self.__a[i][20]='H'
		for i in range(9,13):
			self.__a[i][35]='H'
		for i in range(13,17):
			self.__a[i][25]='H'
		for i in range(17,21):
			self.__a[i][31]='H'
		for i in range(21,25):
			self.__a[i][24]='H'
	def printscreen(self):
		
		for i  in range(0,26):
			for j in range(0,69):
				# print self.__a[i][j],
				if(self.__a[i][j]=='D'):
					print ('\033[1m'+'\033[94m' + 'D' + '\033[0m'),
				elif(self.__a[i][j]=='P'):
					print ('\033[1m'+'\033[92m' + 'P' + '\033[0m'),
				elif(self.__a[i][j]=='X'):
					print ('\033[1m'+'\033[95m' + 'X' + '\033[0m'),
				elif(self.__a[i][j]=='C'):
					print ('\033[1m'+'\033[93m' + 'C' + '\033[0m'),
				elif(self.__a[i][j]=='O'):
					print ('\033[1m'+'\033[91m' + 'O' + '\033[0m'),	
				else:	
					print self.__a[i][j],    
			print ""
 
	def printpl(self,x,y,ch):
		for i in range(2,5):
			self.__a[i][33]='H'
		for i in range(5,9):
			self.__a[i][20]='H'
		for i in range(9,13):
			self.__a[i][35]='H'
		for i in range(13,17):
			self.__a[i][25]='H'
		for i in range(17,21):
			self.__a[i][31]='H'
		for i in range(21,25):
			self.__a[i][24]='H'
		if(self.__a[x][y]=='C' and ch=='P'):
			self.collectcoin()
		self.__a[x][y]=ch

		os.system("clear")
		
		self.printscreen()
	def printplspace(self,x,y,ch):
		self.__a[x][y]=ch
		for i in range(2,5):
			self.__a[i][33]='H'
		for i in range(5,9):
			self.__a[i][20]='H'
		for i in range(9,13):
			self.__a[i][35]='H'
		for i in range(13,17):
			self.__a[i][25]='H'
		for i in range(17,21):
			self.__a[i][31]='H'
		for i in range(21,25):
			self.__a[i][24]='H'
		if(self.__a[x][y]=='C'):
			self.collectcoin()
		os.system("clear")
		
		self.printscreen()

	
	def checkwall(self,x,y):
		if(self.__a[x][y]=='X'):
			return False
		else:
			return True
	
	def checkstairs(self,x,y):
		
		if((self.__a[x][y]=='H')):
			return True
		else:
			return False
	
	def checkdot(self,x,y):
		if(self.__a[x][y]=='X' or self.__a[x][y]=='H'):
			return True
		else:
			return False
	def Iscoinpresent(self,x,y):
		if(self.__a[x][y]=='C'):
			return True
		else:
			return False

	def generatecoin(self):
		cnt=30
		i=0
		j=0
		while(cnt!=0):
			i=randint(1,24)
			j=randint(1,64)
			if(self.__a[i+1][j]=='X' and self.__a[i][j]!='H' and self.__a[i][j]!='X'):
				self.__a[i][j]='C'
				cnt=cnt-1
	
	def collectcoin(self):
	    self.__score+=5
	
	def getscore(self):
	    return self.__score

class Person:
	def __init__(self,x=0,y=0):
		self.__x=x
		self.__y=y


class Player(Person):
	def __init__(self,x,y):
		self.__x=x
		self.__y=y
	def move(self,ch,sc):
		sc.printplspace(self.__x,self.__y,' ')
		time.sleep(0.01)

		# fl=0
		if(ch=='w' or ch=='W'):
			if(sc.checkstairs(self.__x,self.__y)):
				self.__x-=1
		if(ch=='a' or ch=='A'):
			if(sc.checkdot(self.__x+1,self.__y-1)):

				if(sc.checkwall(self.__x,self.__y-1)):
					self.__y-=1
			else:
				self.__x+=4

				self.__y-=1
		if(ch=='d' or ch=='D'):
			if(sc.checkdot(self.__x+1,self.__y+1)):

				if(sc.checkwall(self.__x,self.__y+1)):
					self.__y+=1
			else:
				self.__x+=4

				self.__y+=1		
		if(ch=='s' or ch=='S'):
			if(sc.checkstairs(self.__x+1,self.__y)):
				self.__x+=1
		if(ord(ch)==32):
			sc.printpl(self.__x-1,self.__y+1,'P')
			sc.printplspace(self.__x,self.__y,' ')
			time.sleep(0.1)
			sc.printpl(self.__x-2,self.__y+2,'P')
			sc.printplspace(self.__x-1,self.__y+1,' ')
			time.sleep(0.1)
			sc.printpl(self.__x-1,self.__y+3,'P')
			sc.printplspace(self.__x-2,self.__y+2,' ')
			time.sleep(0.1)
			sc.printpl(self.__x,self.__y+4,'P')
			sc.printplspace(self.__x-1,self.__y+3,' ')
			self.__y+=4

		sc.printpl(self.__x,self.__y,'P')
		time.sleep(0.01)


	def getx(self):
		return self.__x
	def gety(self):
		return self.__y

class Donkey(Person):
	def __init__(self,x,y):
		self.__x=x
		self.__y=y
		
	def move(self,sc):
		global fl
		sc.printplspace(self.__x,self.__y,' ')
		time.sleep(0.01)

		if(fl==0):
			if(sc.Iscoinpresent(self.__x,self.__y+1)):
				self.__y+=2
			else:
				self.__y+=1
			if(self.__y>50):
				fl=1
		if(fl==1):
			if(sc.Iscoinpresent(self.__x,self.__y-1)):
				self.__y-=2
			else:
				self.__y-=1
			if(self.__y<2):
				fl=0
		sc.printpl(self.__x,self.__y,'D')
		time.sleep(0.01)
	def getx(self):
		return self.__x
	def gety(self):
		return self.__y

class Fireball:
	def __init__(self,x,y):
		self.__x=x
		self.__y=y
	def move(self,sc):
		global firemv
		sc.printplspace(self.__x,self.__y,' ')
		time.sleep(0.01)
		# firemv=randint(0,1)
		if(sc.checkdot(self.__x+1,self.__y+1)):
			if(firemv==1):
				if(sc.checkwall(self.__x,self.__y+1)):
					if(sc.Iscoinpresent(self.__x,self.__y+1)):
						self.__y+=2
					else:
						self.__y+=1
				else:
					firemv=0
					self.__y-=1
			else:
				if(sc.checkwall(self.__x,self.__y-1)):
					if(sc.Iscoinpresent(self.__x,self.__y-1)):
						self.__y-=2
					else:
						self.__y-=1
				else:
					firemv=1
					self.__y+=1

		else:
			self.__x+=4
			if(randint(0,1)==1):
				if(sc.Iscoinpresent(self.__x,self.__y+1)):
					self.__y+=2
				else:
					self.__y+=1
				firemv=1
			else:
				if(sc.Iscoinpresent(self.__x,self.__y+1)):
					self.__y-=2
				else:
					self.__y-=1
				firemv=0
		sc.printpl(self.__x,self.__y,'O')
		time.sleep(0.01)
	def getx(self):
		return self.__x
	def gety(self):
		return self.__y

		
			

lives=3        
firemv=0  
firemv=randint(0,1)
cnt=0
fl=0  
firefl=0  
score=0
def main():
	# print 
	while(1):
		global lives
		global score
		if(lives==0):
			break
		screen=Screen(score)
		screen.generatecoin()
		screen.printscreen()
		pl=Player(24,1)
		dn=Donkey(4,1)
		# dn.donkeyposition(screen)
		while(1):
			global cnt
			global firefl

			cnt+=1
			ch=getchar()
			if(ch=='q'):
				lives=0
				break
			if(cnt==10):
				fb=Fireball(dn.getx(),dn.gety())
				fb.move(screen)
				firefl=1
				cnt=-10000

			if(firefl==1):	
				fb.move(screen)
				if(fb.getx()==pl.getx() and fb.gety()==pl.gety()):
					lives-=1
					score=screen.getscore()
					score-=50
					os.system("clear")
					break
				if(dn.getx()==pl.getx() and dn.gety()==pl.gety()):
					lives-=1
					os.system("clear")
					score=screen.getscore()
					score-=50
					break
			dn.move(screen)
			if(firefl==1):	
				# fb.move(screen)
				if(fb.getx()==pl.getx() and fb.gety()==pl.gety()):
					lives-=1
					score=screen.getscore()
					score-=50
					os.system("clear")
					break
				if(dn.getx()==pl.getx() and dn.gety()==pl.gety()):
					lives-=1
					os.system("clear")
					score=screen.getscore()
					score-=50
					break
			pl.move(ch,screen)
			if(firefl==1):	
				# fb.move(screen)
				if(fb.getx()==pl.getx() and fb.gety()==pl.gety()):
					lives-=1
					score=screen.getscore()
					score-=50
					os.system("clear")
					break
				if(dn.getx()==pl.getx() and dn.gety()==pl.gety()):
					lives-=1
					os.system("clear")
					score=screen.getscore()
					score-=50
					break
			print "Your Score:"
			print screen.getscore()




	print "Game Over: Your Final Score is:",
	print screen.getscore()
if __name__ == "__main__":
	main()
