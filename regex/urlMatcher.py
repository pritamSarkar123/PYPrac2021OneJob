import re
urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
def matches(text_to_search,pattern):
	# group ()
	pattern=re.compile(pattern)
	spans=[]
	values=[]
	group_zero=[]
	group_one=[]
	group_two=[]
	group_three=[]
	matches=pattern.finditer(text_to_search)
	for match in matches:
	    spans.append(match.span())
	    values.append(match.group())
	    group_zero.append(match.group(0))
	    group_one.append(match.group(1))
	    group_two.append(match.group(2))
	    group_three.append(match.group(3))
	print(spans[:6])
	print(values[:6])
	print(group_zero[:6])
	print(group_one[:6])
	print(group_two[:6])
	print(group_three[:6])

matches(urls,r'https?://(www\.)?(\w+)(\.\w+)')
# [(1, 23), (24, 42), (43, 62), (63, 83)]
# ['https://www.google.com', 'http://coreyms.com', 'https://youtube.com', 'https://www.nasa.gov']
# ['https://www.google.com', 'http://coreyms.com', 'https://youtube.com', 'https://www.nasa.gov']
# ['www.', None, None, 'www.']
# ['google', 'coreyms', 'youtube', 'nasa']
# ['.com', '.com', '.com', '.gov']




#when ever match occurs substritute the matched string with group2 and group3 elements
# \2 <- group 2
# or
# we caN do
# substrituted_urls=re.sub(r"pattern",r"replacing element",finding area)
pattern=re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
substrituted_urls=pattern.sub(r'\2\3',urls)
# OR
# substrituted_urls=re.sub(r"https?://(www\.)?(\w+)(\.\w+)",r"\2\3",urls)
print(substrituted_urls)
# google.com
# coreyms.com
# youtube.com
# nasa.gov

matches = pattern.findall(urls)
print(matches)
# [('www.', 'google', '.com'), ('', 'coreyms', '.com'), ('', 'youtube', '.com'), ('www.', 'nasa', '.gov')]

text='abcd abcd abcd'
p=re.compile(r"^\w+d")
matches=p.match(text) #returns the 1st occurance
print(matches)
# <re.Match object; span=(0, 4), match='abcd'>