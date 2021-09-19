# https://www.youtube.com/watch?v=IhJgguNiYYk&list=PLi9RQVmJD2fYXgBAUfaN5MXgYPUTbzqeb&index=116
from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 0
        i = 0 
        j = 0
        index = i
        while j < len(chars):
            if chars[i] != chars[j]:
                chars[index] = chars[i]; index +=1
                count += 1
                if j - i > 1:
                    count += len(str(j-i))
                    for c in str(j-i):
                        chars[index] = c; index +=1
                i = j
            j += 1
            
        if j == len(chars):
            chars[index] = chars[i]; index +=1
            count += 1
            if j - i > 1:
                count += len(str(j-i))
                for c in str(j-i):
                    chars[index] = c; index +=1
        
        return count
    
if __name__=="__main__":
    s = Solution()
    l = ["a","a","b","b","c","c","c"]
    print(s.compress(l))
    print(l)
