from manim import *
config.media_width="75%"
config.verbosity="WARNING"
from random import randint

class PositionalNotation(Scene):
	def construct(self):
		count=0
		while count<100:
			int1=randint(1000,9999)
			int2=randint(1000,9999)
			if int1==int2:
				continue
			else:
				a=Tex(str(int1))
				b=Tex(str(int2))
				self.play(Create(a))
				b.next_to(a,DOWN)
				self.play(Create(b))
				self.wait(1)
				count+=1
				#print(len(a[0]))
				TopRect={i:SurroundingRectangle(a[0][i]) for i in range(len(str(int1)))}
				BottomRect={i:SurroundingRectangle(b[0][i]) for i in range(len(str(int2)))}
				if str(int1)[0]>str(int2)[0]:
					b[0][0].set_color(RED)
					self.add(TopRect[0],BottomRect[0])
					self.wait(1)
					self.add(b)
					self.wait(1)
					self.play(Indicate(a))
					self.clear()
					continue
				elif str(int1)[0]<str(int2)[0]:
					a[0][0].set_color(RED)
					self.add(TopRect[0],BottomRect[0])
					self.wait(1)
					self.add(a)
					self.wait(1)
					self.play(Indicate(b))
					self.clear()
					continue
				else:
					a[0][0].set_color(GREEN)
					b[0][0].set_color(GREEN)
					self.add(a,b,TopRect[0],BottomRect[0])
					self.wait(1)
				for i in range(1,len(str(int1))):
					if str(int1)[i]>str(int2)[i]:
						#self.remove(TopRect[i-1],BottomRect[i-1])
						self.play(ReplacementTransform(TopRect[i-1],TopRect[i]),ReplacementTransform(BottomRect[i-1],BottomRect[i]))
						b[0][i].set_color(RED)
						self.add(a)
						self.wait(1)
						self.play(Indicate(a))
						self.wait(1)
						break
					elif str(int1)[i]<str(int2)[i]:
						#self.remove(TopRect[i-1],BottomRect[i-1])
						self.play(ReplacementTransform(TopRect[i-1],TopRect[i]),ReplacementTransform(BottomRect[i-1],BottomRect[i]))
						a[0][i].set_color(RED)
						self.add(a)
						self.wait(1)
						self.play(Indicate(b))
						self.wait(1)
						break
					else:
						#self.remove(TopRect[i-1],BottomRect[i-1])
						self.play(ReplacementTransform(TopRect[i-1],TopRect[i]),ReplacementTransform(BottomRect[i-1],BottomRect[i]))
						a[0][i].set_color(GREEN)
						b[0][i].set_color(GREEN)
						self.add(a,b)
						self.wait(1)
				self.clear()
