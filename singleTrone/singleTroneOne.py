#strict
class DbAccess:
	__instance=None
	def __new__(cls,name="",age="",nationality="",*args,**kwargs):
		if cls.__instance is None:
			cls.__instance=object.__new__(cls,*args,**kwargs)
			cls.__instance.name=name
			cls.__instance.age=age
			cls.__instance.nationality=nationality
		return cls.__instance

	def __str__(self):
		return f" {DbAccess.__instance.name} {DbAccess.__instance.age} {DbAccess.__instance.nationality}"
	@classmethod
	def update(cls,name="",age="",nationality=""):
		if name != "":
			cls.__updateName(name)
		if nationality != "":
			cls.__updateNationality(nationality)
		if age!="":
			cls.__updateAge(age)

	@classmethod
	def __updateName(cls, name):
		cls.__instance.name = name
	@classmethod
	def __updateAge(cls,age):
		cls.__instance.age = age
	@classmethod
	def __updateNationality(cls,nationality):
		cls.__instance.nationality = nationality


db=DbAccess("Pritam Sarkar","26","indian")
print(db)
db1=DbAccess("Pritam") # No change occurs
print(db1)
db1.update("Eshani Jas","27","BG")
print(db1==db) #True
print(db1) # Eshani Jas 27 BG
print(db) # Eshani Jas 27 BG

 # we can also throw exceptionS

#  Pritam Sarkar 26 indian
#  Pritam Sarkar 26 indian
# True
#  Eshani Jas 27 BG
#  Eshani Jas 27 BG