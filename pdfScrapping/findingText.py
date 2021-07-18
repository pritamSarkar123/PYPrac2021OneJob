import fitz
import re

def store_text():
	file_path = "3rdSem.pdf"
	# get the text and store it into a text file named "result.txt"
	with fitz.open(file_path) as pdf_obj:
		num_of_pages = pdf_obj.page_count
		with open("reult.txt","a") as f:
			for i in range(num_of_pages):
				page_obj = pdf_obj.loadPage(i)
				f.write(page_obj.getText())


def find_text():
	file_path = "3rdSem.pdf"
	patterns = ["ROLL NO","COLLEGE / INSTITUTION"]
	matches = []
	#get the text and find the 1st occurance of pattern in it using re
	with fitz.open(file_path) as pdf_obj:
		num_of_pages = pdf_obj.page_count
		for i in range(num_of_pages):
			page_obj = pdf_obj.loadPage(i)
			page_text = page_obj.getText()
			for pattern in patterns:
				matched = re.search(pattern, page_text)
				if matched:
					matches.append(matched)
	for match in matches:
		print(f"{match.span()} -> {match.group(0)}")

def find_text_2():
	file_path = "3rdSem.pdf"
	patterns = ["ROLL NO","COLLEGE / INSTITUTION"]
	matches = []
	#get the text and find the 1st occurance of pattern in it using re
	with fitz.open(file_path) as pdf_obj:
		for page in pdf_obj:
			for pattern in patterns:
				matches.extend(page.searchFor(pattern))
			# five_percent_height = (page.rect.br.y - page.rect.tl.y)
			# print(five_percent_height,page.rect.tl,page.rect.br)
		for match in matches:
			print(match,match.br.x,match.br.y,match.tl.x,match.tl.y)
	# print(matches)

# store_text()
find_text()
find_text_2()

#Rect()