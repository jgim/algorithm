'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

from typing import List

class Solution:
	def containsDuplicate1(self, nums: List[int]) -> bool:
		lens = len(nums)
		dictionary = {}
		for i in nums:
			if i not in dictionary:
				dictionary[i] = i
			else:
				return True
		return False

	def containsDuplicate2(self, nums: List[int]) -> bool:
		return len(nums) != len(set(nums))

	def containsDuplicate3(self, nums: List[int]) -> bool:
		nums.sort()
		for i in range(len(nums) - 1):
			if nums[i] == nums[i + 1]:
				return True
		return False


solution = Solution()

nums = list(map(int, input().split(',')))

result1 = solution.containsDuplicate1(nums)
result2 = solution.containsDuplicate2(nums)
result3 = solution.containsDuplicate3(nums)
print(result1)
print(result2)
print(result3)

'''
< solution.containsDuplicate1 >

05/13/2022 19:26	Accepted	655 ms	26 MB	python3
05/13/2022 19:26	Accepted	773 ms	25.9 MB	python3
05/13/2022 19:26	Accepted	578 ms	25.8 MB	python3

- 리스트를 돌리며 값을 python에 내장된 dicionary에 넣어줌 (해시테이블을 만들 필요가 없음)

< solution.containsDuplicate2 >

05/13/2022 19:30	Accepted	634 ms	26.1 MB	python3
05/13/2022 19:29	Accepted	675 ms	25.8 MB	python3
05/13/2022 19:29	Accepted	482 ms	26.1 MB	python3

- 파이썬에 내장된 set함수는 중복된 값을 제거해줌
- 만약 제거된 값이 있으면 길이는 기존 list보다 짧아지는 것을 활용

< solution.containsDuplicate3 >

05/13/2022 19:35	Accepted	682 ms	26.2 MB	python3
05/13/2022 19:34	Accepted	931 ms	26 MB	python3
05/13/2022 19:34	Accepted	657 ms	26.1 MB

- 정렬을 해주고 다음에 같은 값이 오게 되면 true 리턴


'''
