# https://github.com/pritamSarkar123/Java2020Basic/blob/main/kmp/MyKmpTestingClass.java
text="ababcabcababababdvcd"
pattern ="ababd"

pi=[0]*len(pattern)

following = 0
leading = following + 1


while leading < len(pattern):
	if pattern[leading] == pattern[following]:
		pi[leading] = following + 1
		following += 1
	else:
		while following > 0 and pattern[leading] != pattern[following]:
			following = pi[following - 1]
		if following==0 and pattern[leading] != pattern[following]:
			pi[leading] = 0
		else:
			pi[leading] = following + 1
			following += 1
	leading += 1

pat_pointer = 0
txt_pointer = 0

while True:
	if pat_pointer == len(pattern):
		print(txt_pointer - pat_pointer)
		break
	if txt_pointer == len(text):
		print(-1)
		break
	if text[txt_pointer] == pattern[pat_pointer]:
		pat_pointer += 1
	else:
		while pat_pointer > 0 and text[txt_pointer] != pattern[pat_pointer]:
			pat_pointer = pi[pat_pointer]

		if pat_pointer!=0 or text[txt_pointer] == pattern[pat_pointer]:
			pat_pointer += 1

	txt_pointer +=1
# time O(p + t)
# space O(p)