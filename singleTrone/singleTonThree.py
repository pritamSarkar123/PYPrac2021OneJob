class DbAccess:
	def __init__(self,name="",age="",nationality="",access="denied"):
		self.name = name;self.age = age;self.nationality = nationality
		self.access = access
	def __str__(self):
		return f"{self.name}:{self.age}:{self.nationality}:{self.access}"
	def __hash__(self):
		# parent hash will be its hash then
		# return 
		return hash((self.name, self.age, self.nationality))
	def __eq__(self, other):
		if other is None:
			return False
		if not isinstance(other,DbAccess):
			return False
		if hash(self) != hash(other):
			return False
		if self.name==other.name and self.age == other.age and self.nationality == other.nationality and self.access == other.access:
			return True
		return True
	__repr__ = __str__


class DbAccessCatalog:
	__instance = set()
	__instance_max_limit=5
	def __new__(cls,*args,**kwargs):
		if len(cls.__instance) < cls.__instance_max_limit:
			instance=DbAccess(*args,"granted",**kwargs)
			cls.__instance.add(instance)
			return instance
		return None 

	@classmethod
	def showAllInstances(cls):
		return f" {cls.__instance}"

	@classmethod
	def removeInstance(cls,obj: "DbAccess"):
		obj.access="denied"
		cls.__instance.discard(obj)

	@classmethod
	def getAccess(cls,obj):
		if obj in DbAccessCatalog._DbAccessCatalog__instance:
			print("Access Granted")
		else:
			print("Access Denied")


a=DbAccessCatalog("pritam",27,"indian")
b=DbAccessCatalog("vanu",27,"bangladesi")
c=DbAccessCatalog("eshani",27,"ghoti")
d=DbAccessCatalog("rahul",28,"gandu")
e=DbAccessCatalog("pujki",26,"sreerampur")
f=DbAccessCatalog("pona",26,"auto")

print(a,b,c,d,e,f)

DbAccessCatalog.removeInstance(b)

f=DbAccessCatalog("pona",26,"auto")

print(a,c,d,e,f,b)

# print(dir(DbAccessCatalog))

DbAccessCatalog.getAccess(a)
DbAccessCatalog.getAccess(b)
DbAccessCatalog.getAccess(c)

print(a==a)
print(a==b)
print(hash(a))
print(hash(b))

print(a)
print(b)
print(c)

print(hash("Pritam"))
print(hash("Pritam"))
