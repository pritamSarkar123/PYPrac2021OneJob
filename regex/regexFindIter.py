import re
text="The rain in Spain,The rain in Spain.The rain in Spain The rain in Spain"
pattern=re.compile(r"\bS\w+")
results=re.finditer(pattern,text)
for result in results:
	print(result)
print(type(results))