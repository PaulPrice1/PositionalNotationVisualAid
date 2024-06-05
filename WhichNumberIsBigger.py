from manim import *
config.media_width="75%"
config.verbosity="WARNING"
from random import randint

class PositionalNotation(Scene):
	def construct(self):
		count=0
		while count<10:
			int1=randint(700,1000)
			int2=randint(700,1000)
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
				for i in range(len(str(int1))):
					if str(int1)[i]>str(int2)[i]:
						b[0][i].set_color(RED)
						break
					elif str(int1)[i]<str(int2)[i]:
						a[0][i].set_color(RED)
						break
					else:
						a[0][i].set_color(GREEN)
						b[0][i].set_color(GREEN)
				self.wait(1)
				self.clear()
