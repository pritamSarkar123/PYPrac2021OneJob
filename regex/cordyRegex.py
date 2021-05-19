import re
text_to_search='''
s simply dummy text of the printing and type bat setting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when cat an unknown 800-555-4321 printer to Mr Golu ok a pat galley of type and Mrs. Vanu scrambled it to ma Mr. T ke a type specimen book. It has survived not only five centuries, but also the sex.com leap into electronic typesetting, remaining essentially unchanged. It was popularised 321-555-4321 in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
s simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an 900-555-4321 unknown printer Mr. Pritam took a ga mat lley of type Ms Eshani and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially Ha HaHa unchanged. It was 123.555.1234 popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more 123*555*1234 recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
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


matches(text_to_search,r'\.') 
# [(66, 67), (229, 230), (257, 258), (284, 285), (343, 344), (413, 414)]
# ['.', '.', '.', '.', '.', '.']
matches(text_to_search,r'sex\.com')
# [(340, 347)]
# ['sex.com']
matches(text_to_search,r'\bHa')
# [(1018, 1020), (1021, 1023)]
# ['Ha', 'Ha']
matches(text_to_search,r'\BHa')
# [(1023, 1025)]
# ['Ha']
matches(text_to_search,r'\d\d\d.\d\d\d.\d\d\d\d') # phone number
# [(166, 178), (434, 446), (784, 796), (1044, 1056), (1160, 1172)]
# ['800-555-4321', '321-555-4321', '900-555-4321', '123.555.1234', '123*555*1234']
matches(text_to_search,r'\d\d\d[-\.]\d\d\d[-\.]\d\d\d\d') # phone number
# [(166, 178), (434, 446), (784, 796), (1044, 1056)]
# ['800-555-4321', '321-555-4321', '900-555-4321', '123.555.1234']
with open('data.txt', 'r') as f:
	data_text=f.read()
	matches(data_text,r'\d\d\d.\d\d\d.\d\d\d\d')
	# [(12, 24), (102, 114), (191, 203), (281, 293), (378, 390), (467, 479)]
	# ['615-555-7164', '800-555-5669', '560-555-5153', '900-555-9340', '714-555-7405', '800-555-6771']
	matches(data_text,r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
	# [(12, 24), (102, 114), (191, 203), (281, 293), (378, 390), (467, 479)]
	# ['615-555-7164', '800-555-5669', '560-555-5153', '900-555-9340', '714-555-7405', '800-555-6771']
	matches(data_text,r'\b[89]00[-.]\d\d\d[-.]\d\d\d\d')
	# [(102, 114), (281, 293), (467, 479), (1093, 1105), (1443, 1455), (1794, 1806)]
	# ['800-555-5669', '900-555-9340', '800-555-6771', '900-555-3205', '800-555-6089', '800-555-7100']
	matches(data_text,r'[1-5]00[-.]\d\d\d[-.]\d\d\d\d') # starting number between 1 and 5
	# [(5836, 5848), (7961, 7973)]
	# ['400-555-1706', '300-555-7821']
	matches(data_text,r'\d{3}.\d{3}.\d{3,4}')
	# [(12, 24), (102, 114), (191, 203), (281, 293), (378, 390), (467, 479)]
	# ['615-555-7164', '800-555-5669', '560-555-5153', '900-555-9340', '714-555-7405', '800-555-6771']
# starts except b , followed by at , 3 character long word
matches(text_to_search,r"[^b]at")
# [(151, 154), (203, 206), (834, 837)]
# ['cat', 'pat', 'mat']

# starts with Mr/Ms/Mrs
# .
# \S 
# Caps then any no of words
matches(text_to_search,r'\bM(r|s|rs)\.?\s[A-Z]\w*')
# [(190, 197), (226, 235), (255, 260), (813, 823), (851, 860)]
# ['Mr Golu', 'Mrs. Vanu', 'Mr. T', 'Mr. Pritam', 'Ms Eshani']
