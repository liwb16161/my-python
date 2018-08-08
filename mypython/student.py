class Student:
		__slots__ = ['name','age','score']
		

		def __init__(self,name,age,score):
			self.name = name
			self.age = age
			self.score = score


		def show_info(self):
			print(self.name,self.age,self.score)


		def setScore(self,s):
			if s>100 or s<0:
				return 
			self.score=s

		def infos(self):
			print("|"+self.name.center(10) + \
					"|"+str(self.age).center(10) + \
					"|"+str(self.score).center(10))


		def __repr__(self):
			s= "|"+self.name.center(10) + \
					"|"+repr(self.age).center(10) + \
					"|"+repr(self.score).center(10) +"|"
			return s

# student1 = Student()
# student1.set_info("李文博",22,99)
# student1.show_info()