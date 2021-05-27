class User:
	def log(self):
		print(self)

class Teacher(User):
	def __init__(self,name):
		self.name = name
	def __str__(self):
		return self.name
	def log(self):
		print(f"inside teacher class {self.name}")

class Student(User):
	def __init__(self,name):
		self.name = name
	def __str__(self):
		return self.name

l=[Teacher("Pritam"),Student("Rahul"),User()]

l[0].log()
l[1].log()
l[2].log()

# inside teacher class Pritam
# Rahul
# <__main__.User object at 0x000001CB9AD2BA88>