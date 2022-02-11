from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        tptr = n - 1

        for i in range(n - 1, -1, -1):
            if nums[i] == 2:
                nums[tptr], nums[i] = nums[i], nums[tptr]
                tptr -= 1


        zptr = 0
        for i in range(0, tptr + 1):
            if nums[i] == 0:
                nums[zptr], nums[i] = nums[i], nums[zptr]
                zptr += 1

nums=[2,0,2,1,1,0]

s=Solution()

s.sortColors(nums)

print(nums)