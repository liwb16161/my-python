class MyNumber:
	def __init__(self,value):
		self.data=value


	def __repr__(self):
		return "MyNumber("+repr(self.data)+")"


	def  __str__(self):
		return "数值("+str(self.data)+")"

	def __add__(self,other):
		return MyNumber(self.data + other.data)

	def __sub__(self,other):
		return MyNumber(self.data - other.data)

	def __mul__(self,other):
		return MyNumber(self.data * other.data)

	def __truediv__(self,other):
		return MyNumber(self.data / other.data)

	def __floordiv__(self,other):
		return MyNumber(self.data // other.data)

	def __mod__(self,other):
		return MyNumber(self.data % other.data)

	def __pow__(self,other):
		return MyNumber(self.data ** other.data)

	def __int__(self):
		return int(self.data)

	def __iter__(self):
		



if __name__  == "__main__":
	n1 = MyNumber(100)
	n2 = MyNumber(200)
	print(repr(n1))
	print(str(n1))
	int1 = int(n1)
	print(int1)
