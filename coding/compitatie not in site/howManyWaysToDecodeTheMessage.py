# https://www.youtube.com/watch?v=qli-JCrSwuk&list=PLBZBJbE_rGRVnpitdvpdY9952IsKMDuev

#


def basic(s,memo,i):
	if memo[i] != None:
		return memo[i]

	if i == len(s):
		#  means "" -> "" one message
		memo[i] = 1

	elif s[i] == "0":
		memo[i]=0
	else:
		result = basic(s,memo,i+1)
		if i+2 <= len(s) and 0<int(s[i:i+2])<=26:
			result += basic(s,memo,i+2)
		memo[i]= result

	return memo[i]

m = "1234"
memo = [None]*(len(m)+1)
print("---no of branches----- "+str(basic(m,memo,0)))
print(memo)