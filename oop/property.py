from  typing_extensions import Final,final
@final
class Student:
	def __init__(self,f_name,l_name):
		self.f_name = f_name
		self.l_name = l_name
	def __str__(self):
		return f"the Student is {self.f_name} {self.l_name}"

	@final
	@property
	def name(self):
		return f"{self.f_name} {self.l_name}"
	@final
	@name.setter
	def name(self,name):
		name=name.split(sep=" ",maxsplit=2)
		self.f_name = name[0]
		self.l_name = name[-1]
	@final
	@name.deleter
	def name(self):
		del self.f_name
		del self.l_name

	__call__=__str__
	__repr__=__str__
	__hash__=None

s = Student("Pritam","Sarkar")
print(s)
print(s())
print(repr(s))
print(str(s))

print(s.name)
s.name="Rahul Banerjee"
print(s.name)
del s.name
# print(s.name) <- gives error (AttributeError)

