### subject

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

#### Example:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1

#### constraints

1 <= nums.length <= 5000 5000개
-104 <= nums[i] <= 104, 209개
All values of nums are unique. 유니크
nums is an ascending array that is possibly rotated.
-104 <= target <= 104

***

### result

#### < solution_1 >

05/07/2022 16:59	Accepted	81 ms	14.4 MB	python3
05/07/2022 16:59	Accepted	56 ms	14.5 MB	python3
05/07/2022 16:59	Accepted	38 ms	14.4 MB	python3

- 이진탐색, 재귀를 사용
- low, high에 target 값이 오는 케이스도 체크, 체크를 하지 않는 solution_3과 비교해서 비교적 속도의 우위


#### < solution_2 >

05/07/2022 16:58	Accepted	48 ms	14.2 MB	python3
05/07/2022 16:58	Accepted	50 ms	14.4 MB	python3
05/07/2022 16:58	Accepted	64 ms	14.4 MB	python3

- 이진탐색, 반복문 while 사용
- 함수의 반복이 없기 때문에 공간 복잡도가 다소 우위
- 평균적인 시간 역시 재귀 대비 더 빠름


#### < solution_3 >

05/07/2022 16:57	Accepted	58 ms	14.5 MB	python3
05/07/2022 16:57	Accepted	89 ms	14.5 MB	python3
05/07/2022 16:57	Accepted	66 ms	14.4 MB	python3

- 재귀를 사용, 케이스를 단순화 시켜서 코드는 간결
- 공간과 시간을 가장 잡아먹는편

#### < total >

- 이진탐색을 사용했기 때문에 시간 복잡도는 전부 O(n)

***
