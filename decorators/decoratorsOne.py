def checkDivByZero(operend_function):
	def innerfunction(a,b):
		if b==0:
			return operend_function(b,a)
		return operend_function(a,b)
	return innerfunction

def divOne(a,b):
	return a//b
divOneModified = checkDivByZero(divOne)

@checkDivByZero
def divTwo(a,b):
	return a//b

divThree=lambda a,b: a//b if b!=0 else b//a

print(divOneModified(5,0))
print(divTwo(5,0))
print(divThree(5,0))