


# https://www.youtube.com/watch?v=2JSQIhPcHQg
# best explanation

def check(arr,mid,k):
	student =1
	pages =0
	for i in range(len(arr)):
		pages += arr[i]
		if pages > mid:
			pages = arr[i]
			student+=1
		if student > k:
			return False
	return True


def get_minimum_max_pages(book_pages,k):
	start = max(book_pages)
	end = sum(book_pages)
	result = -1
	while start <= end:
		mid = start + (end - start)//2
		if check(book_pages,mid,k):
			result = mid
			end = mid -1
		else:
			start = mid+1

	return result


book_pages=[10,20,30,40]
print(get_minimum_max_pages(book_pages,2))