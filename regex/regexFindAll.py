import re

text="The rain in Spain"
x=re.findall("ai",text)
print(x)
# ['ai', 'ai']
x=re.findall("piof",text)
print(x)
# []
