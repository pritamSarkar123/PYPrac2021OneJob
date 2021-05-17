# non strict
class DbConnect:
	__instance = None
	def __new__(cls,username="",password="",host="",port=""):
		if cls.__instance is None:
			cls.__instance = object.__new__(cls)
		cls.__instance.username=username
		cls.__instance.password=password
		cls.__instance.host=host
		cls.__instance.port=port
		return cls.__instance
	def __str__(self):
		return f" {DbConnect.__instance.username} {DbConnect.__instance.password} {DbConnect.__instance.host} {DbConnect.__instance.port}"

db1=DbConnect("Pritam","sarkar123","localhost","8080")
print(db1)
db2=DbConnect("Pritam")
print(db2)
print(db2==db1)

# Pritam sarkar123 localhost 8080
#  Pritam   
# True