import re

text="The rain in Spain"
x=re.split(r"\s",text) # split using whitespace
print(x)

# ['The', 'rain', 'in', 'Spain']

text="The rain in Spain"
x=re.split(r"\s",text,1) # split using whitespace on first occurrence
print(x)
# ['The', 'rain in Spain']