from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic1=defaultdict(int)
        for i in range(len(s)):
            dic1[s[i]]+=1
        print(dic1)
        values=dic1.items()
        for k,v in values:
            print(k,v)
            if v==1:
                return s.index(k)
        return -1
                
           






        