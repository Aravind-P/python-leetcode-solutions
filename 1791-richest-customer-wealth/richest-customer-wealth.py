class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        orig=accounts
        lis=[]
        for i in range(0,len(accounts)):
            lis.append(sum(accounts[i]))
            


        print(lis)
        return max(lis)
