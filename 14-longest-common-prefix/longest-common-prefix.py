class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        str1=""
        strs.sort()
        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:
                str1 += strs[0][i]
            else:
                break
        print(str1)
        return str1


        