# Search the string to see if it starts with "The" and ends with "Spain":
import re

text="The rain in Spain"
x=re.search("^The.*Spain$",text)
print(x)
print(type(x))
# <re.Match object; span=(0, 17), match='The rain in Spain'>
# <class 're.Match'>
if x:
	print(f"from {x.start()} to {x.end()}")
else:
	print("Not found")


text="The rain in Spain"
x=re.search("ai",text) # returns first match
print(x)
# <re.Match object; span=(5, 7), match='ai'>

text="The rain in Spain"
# any word starts with "\bS\w+" , 1st occurance
x=re.search(r"\bS\w+",text)
print(x,x.span())
print(x.string)
print(x.group())
print(x.groups())
# <re.Match object; span=(12, 17), match='Spain'> (12, 17)
# The rain in Spain
# Spain
# ()

text="The rain in Spain"
pattern=re.compile(r"\bS\w+")
x=re.search(pattern,text)
print(x)
x=pattern.search(text)
print(x)
# <re.Match object; span=(12, 17), match='Spain'>
# <re.Match object; span=(12, 17), match='Spain'>