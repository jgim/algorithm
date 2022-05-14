'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''

from typing import List

class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		dictionary = {}
		for i, num in enumerate(nums):
			value = target - num
			if value not in dictionary:
				dictionary[num] = i
			else:
				return [dictionary[value], i]

solution = Solution()

nums = list(map(int, input().split(',')))
target = int(input())

result = solution.twoSum(nums, target)
print(result)

'''
05/14/2022 17:07	Accepted	69 ms	15.2 MB	python3
05/14/2022 17:07	Accepted	78 ms	15.2 MB	python3
05/14/2022 17:07	Accepted	89 ms	15.2 MB	python3

- dictionary를 이용해 문제를 해결
- target - num 값이 dictionary에 존재하지 않으면 인덱스 값을 추가
- 존재한다면 현재 인덱스와 num의 키값을 dicionary에서 찾아서 리턴

'''
