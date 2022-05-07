# Given an array of integers nums which is sorted in ascending order,
# and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.

#You must write an algorithm with O(log n) runtime complexity
from typing import List
import bisect

class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)

        while start < end:
            pivot = (start + end) // 2
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] < target:
                start = pivot + 1
            elif nums[pivot] > target:
                end = pivot
        return -1

class Solution2:
	def search(self, nums: List[int], target: int) -> int:
		index = bisect.bisect_left(nums, target)
		if index < len(nums) and nums[index] == target:
			return index
		else:
			return -1

solution1 = Solution1()
solution2 = Solution2()

nums = list(map(int, input().split()))
target = int(input())

result1 = solution1.search(nums, target)
result2 = solution2.search(nums, )
print ("solution 1 : ", result1)
print ("solution 2 : ", result2)


