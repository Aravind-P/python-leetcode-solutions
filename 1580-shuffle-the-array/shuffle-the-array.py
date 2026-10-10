class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        orig=nums
        ans=[]
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
            print(ans)
        return ans  