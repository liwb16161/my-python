class Human:
	# tot_money = 0
	def __init__(self,name,age):
		self.name = name
		self.age = age
		self.amt = 0
		self.skill = []

	def teach(self,who,subject):
		print(self.name,"教",who.name,"学",subject)
		who.skill.append(subject)

	def makemoney(self,amt):
		print(self.name,"赚了",amt,"元！")
		self.amt += amt

	def borrow_from(self,who,amt):
		if who.amt<amt:
			raise ValueError(who.name,"钱不够",amt)
		print(self.name,"从",who.name,"借了",str(amt),"元！")
		who.amt -= amt
		self.amt += amt

h1 = Human('tom',21)

h2 = Human('tony',22)

h1.teach(h2,"python")
print(h2.skill)

h1.makemoney(1000)
print(h1.amt)

h2.borrow_from(h1,500)
print(h2.amt,h1.amt)

h1.amt=10