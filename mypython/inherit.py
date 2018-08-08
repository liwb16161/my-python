import cat 

#此示例示意单继承

class Human:
	def say(self,what):
		print("say",what)
	def walk(self,distance):
		print("go",distance)



class Student(Human):
	def study(self,subject):
		print("study",subject)

class Teacher(Student):
	def teach(self,subject):
		print("teach",subject)


h1 = Human()
h1.say("sb")
s1 = Student()
s1.study("Python")
t1 = Teacher()
t1.teach("Python")