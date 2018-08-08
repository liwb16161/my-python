#主模块
import student as stu

L = []
s1 = stu.Student("lwb",22,90)
s2 = stu.Student("tiantian",20,89)
L.append(s1)
L.append(s2)
s2.setScore(88)
for x in L:
	print(x)
