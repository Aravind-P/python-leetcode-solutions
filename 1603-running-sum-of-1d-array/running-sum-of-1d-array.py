class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        orig=nums
        n=len(nums)
        ans=[]
        print(nums[0])
        ans.append(nums[0])
        for i in range(1,n):
            ans.append(ans[i-1]+nums[i])
        print(ans)
        return ans