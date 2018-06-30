class Cat():
	"""这是一个关于猫的类"""
	# def setname(self,name):
	__count__ = 0
	__slots__=["name","age"]
	owner1 = "博"
	def __init__(self,name,age):

		self.name = name
		self.age = age


	def sayhello(self):
		print("你好 喵喵喵！")


	def run(self,speed):
		print(self.name ,"正在以",speed,"的速度前进")


	@classmethod
	def owner(cls):
		print("主人是",cls.owner1)
		cls.myadd(1,3)


	def __del__(self):
		print("gg!")


	@staticmethod
	def myadd(a,b):
		return a + b


	@property
	def drink(self):
		# print(self.name,"喝了",vol,"升水")
		return self.age*5

	@drink.setter
	def dirnk(self,vol):
		self.age = vol/5


	def __repr__(self):
		s="我是"+self.name+','+"今年"+repr(self.age)+"岁"+'^_^'
		return s



class Bluecat(Cat):
	"""关于蓝猫"""
	def __init__(self,name,age,weight):
		super().__init__(name,age)
		self.weight=weight


	def sayhello(self):
		super().sayhello()
		print("我是一只小蓝猫，喵喵喵！")


if __name__=="__main__":

	# Cat1 = Cat("小灰",2)
	# Cat1.sayhello()
	# Cat1.run("110m/s")
	# Cat.owner()
	# Cat1.myadd(1,2)
	# print(Cat1.drink)
	# Cat1.dirnk=15
	# print(Cat1.age)
	bcat1 = Bluecat('xiaohui',22,"5kg")
	bcat1.sayhello()


