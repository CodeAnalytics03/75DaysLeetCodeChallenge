class Solution(object):
    def moveZeroes(self, nums):
        ip = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[ip], nums[i] = nums[i], nums[ip]
                ip += 1
        