from PIL.ImageChops import soft_light


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow=0
        fast=0
        while fast<len(nums):
            if nums[fast]!=val:
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
        return slow

nums=[1,1,2,3,4,4,4,5,6]
solution = Solution()
ans=solution.removeElement(nums,4)
for i in range(ans):
    print(nums[i])