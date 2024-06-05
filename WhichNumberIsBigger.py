from manim import *
config.media_width="75%"
config.verbosity="WARNING"
from random import randint

class PositionalNotation(Scene):
	def construct(self):
		count=0
		#for 100 numbers run the code in the while loop this can be adjusted
		while count<100:
			#pick 2 numbers each in the range 1000 to 9999 (i.e.) four digit numbers, one might consider altering these ranges to require more comparisons from the algorithm
			int1=randint(1000,9999)
			int2=randint(1000,9999)
			if int1==int2:
				continue
			else:
				#make the tex objects and put int1 under int2 or  Tex a under Tex b
				a=Tex(str(int1))
				b=Tex(str(int2))
				self.play(Create(a))
				b.next_to(a,DOWN)
				self.play(Create(b))
				self.wait(1)
				count+=1
				#generate a 'list' of bounding boxes for the individual digit of each number respectively
				TopRect={i:SurroundingRectangle(a[0][i]) for i in range(len(str(int1)))}
				BottomRect={i:SurroundingRectangle(b[0][i]) for i in range(len(str(int2)))}
				#for the first digit, compare the two numbers
				if str(int1)[0]>str(int2)[0]:
					#if the first digit of int1 is greater than the first digit of int2 you can stop checking, make b (int2's) first digit red
					b[0][0].set_color(RED)
					#add the surrounding rectangles for the first digit
					self.add(TopRect[0],BottomRect[0])
					self.wait(1)
					#add the now red digit of b to the screen
					self.add(b)
					self.wait(1)
					#make all of integer1 or a's numbers flash and grow to show that it's bigger
					self.play(Indicate(a))
					#because the first digits were different we can wipe the screen and go to the next number
					self.clear()
					continue
				elif str(int1)[0]<str(int2)[0]:
					#a's first digit is smaller than the b's first digit make a's first digit red 
					a[0][0].set_color(RED)
					#add the surrunding rectangles for the first digit
					self.add(TopRect[0],BottomRect[0])
					self.wait(1)
					#add the red first digit of a to the screen
					self.add(a)
					self.wait(1)
					#make all of b's digits grow and flash to show that it is the bigger number
					self.play(Indicate(b))
					self.clear()
					#we don't need to compare the remaining pairs of digits, go to the next pair of integers
					continue
				else:
					#if neither of the first digits are the bigger of the two then they must be the equal. make both of the first digits green
					a[0][0].set_color(GREEN)
					b[0][0].set_color(GREEN)
					#add the green digits and the surrounding rectangles to the screen
					self.add(a,b,TopRect[0],BottomRect[0])
					self.wait(1)
				for i in range(1,len(str(int1))):
					if str(int1)[i]>str(int2)[i]:
						#if the current digit of b is less than the current digit of a
						#self.remove(TopRect[i-1],BottomRect[i-1])
						#move the surrounding rectangles from the previous set of digits to the current one
						self.play(ReplacementTransform(TopRect[i-1],TopRect[i]),ReplacementTransform(BottomRect[i-1],BottomRect[i]))
						b[0][i].set_color(RED)
						self.add(a)
						self.wait(1)
						self.play(Indicate(a))
						self.wait(1)
						break
					elif str(int1)[i]<str(int2)[i]:
						#if the current digit of a is less than the current digit of b
						#self.remove(TopRect[i-1],BottomRect[i-1])
						#move the surrounding rectangle from the previous set of digits to the current one
						self.play(ReplacementTransform(TopRect[i-1],TopRect[i]),ReplacementTransform(BottomRect[i-1],BottomRect[i]))
						#make the current digit of a red
						a[0][i].set_color(RED)
						#add the red a to the screen
						self.add(a)
						self.wait(1)
						#make all digits of b bigger and flashing to indicate that it is the 
						self.play(Indicate(b))
						self.wait(1)
						#because the digits were different we don't have to check the remaining digits go to the next set of integers
						break
					else:
						# if neither digit was bigger, both of the digits must be the same
						#self.remove(TopRect[i-1],BottomRect[i-1])
						self.play(ReplacementTransform(TopRect[i-1],TopRect[i]),ReplacementTransform(BottomRect[i-1],BottomRect[i]))
						a[0][i].set_color(GREEN)
						b[0][i].set_color(GREEN)
						self.add(a,b)
						self.wait(1)
				self.clear()
