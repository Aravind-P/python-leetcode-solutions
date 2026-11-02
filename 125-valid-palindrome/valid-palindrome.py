class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1=s
        n=len(s)-1
        str2=''
        str3=''
        for i in range(len(s)):
            if str1[i].isalnum():
                str3+=''.join(str1[i].lower())
                
        print("break")
        for i in range(n,-1,-1):
            if str1[i].isalnum():
                str2+=''.join(str1[i].lower())
                

        print(str2,str3)
        if str3 == str2:
            return True
        else:
            return False


