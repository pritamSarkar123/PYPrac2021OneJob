import re
text="The rain in Spain"
x=re.sub(r"\s","-",text)
print(x)
# The-rain-in-Spain
y=re.sub(r"\s","-",text,2) # 2<- nuber of times from begining
print(y)
# The-rain-in Spain