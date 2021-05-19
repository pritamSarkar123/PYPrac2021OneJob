name_age={
	"pritam":26,
	"eshani":26,
	"rahul":27,
	"ridhika":26
}
print(name_age)
# {'pritam': 26, 'eshani': 26, 'rahul': 26, 'ridhika': 26}

# adding new items and updating values
another_name_age={
	"vusha":27,
	"rahul":28,
	"jaguli":19
}
name_age.update(another_name_age)
print(name_age)
# {'pritam': 26, 'eshani': 26, 'rahul': 28, 'ridhika': 26, 'vusha': 27, 'jaguli': 19}

d1=dict.fromkeys(range(5),0)
print(d1)
# {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}

# if key present get the value
# otherwise set the new val and get item
print(name_age.setdefault("pona",20))
print(name_age.setdefault("jaguli",90))
print(name_age)
# 20
# 19
# {'pritam': 26, 'eshani': 26, 'rahul': 28, 'ridhika': 26, 'vusha': 27, 'jaguli': 19, 'pona': 20}

# popping out the last entered item
name_age.popitem()
print(name_age)
# {'pritam': 26, 'eshani': 26, 'rahul': 28, 'ridhika': 26, 'vusha': 27, 'jaguli': 19}

# popping out particular elemet based on keys
name_age.pop('jaguli')
print(name_age)
# {'pritam': 26, 'eshani': 26, 'rahul': 28, 'ridhika': 26, 'vusha': 27}

# OR
del name_age['pritam']
print(name_age)
# {'eshani': 26, 'rahul': 28, 'ridhika': 26, 'vusha': 27}

# removing al entries in the dict
name_age.clear()
print(name_age)
# {}

# deleting the actual dictionary also
del name_age
# print(name_age) gives NameError


print("Hello eorld I am {} ".format("pritam")) 
print("Hello eorld I am {0} ".format("pritam")) # index based
print("Hello eorld I am {name} ".format(name="pritam")) # variable based