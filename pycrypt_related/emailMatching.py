import re
emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''
def matches(text_to_search,pattern):
	pattern=re.compile(pattern)
	spans=[]
	values=[]
	matches=pattern.finditer(text_to_search)
	for match in matches:
	    spans.append(match.span())
	    values.append(match.group())
	print(spans[:6])
	print(values[:6])

matches(emails,r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
# [(1, 24), (25, 53), (54, 83)]
# ['CoreyMSchafer@gmail.com', 'corey.schafer@university.edu', 'corey-321-schafer@my-work.net']