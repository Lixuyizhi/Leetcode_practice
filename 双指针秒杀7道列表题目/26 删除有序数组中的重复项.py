class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        fast = 1
        while fast < len(nums):
            if (nums[fast] != nums[slow]):
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1

nums=[1,1,2,3,4,4,4,5,6]
solution = Solution()
ans=solution.removeDuplicates(nums)
for i in range(ans):
    print(nums[i])