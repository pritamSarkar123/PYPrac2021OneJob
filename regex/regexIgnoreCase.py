import re
text="The rain in Spain,The rain in Spain.The rain in spain The rain in Spain"
pattern=re.compile(r"\bS\w+",re.I)
results=re.finditer(pattern,text)
for result in results:
	print(result)
print(type(results))
# <re.Match object; span=(12, 17), match='Spain'>
# <re.Match object; span=(30, 35), match='Spain'>
# <re.Match object; span=(48, 53), match='spain'>
# <re.Match object; span=(66, 71), match='Spain'>
# <class 'callable_iterator'>