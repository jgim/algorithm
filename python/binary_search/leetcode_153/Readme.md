### Subject

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.


#### Example:

```Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.```

Example 2:
```Input: nums = [4,5,6,7, 8 ,0,1,2,3]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.```

Example 3:
```Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.```


#### constraints

```n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.```

***

### result

#### < solution_findMin1 >
```
05/08/2022 02:34	Accepted	37 ms	14.2 MB	python3
05/08/2022 02:33	Accepted	45 ms	14.2 MB	python3
05/08/2022 02:33	Accepted	52 ms	14.1 MB	python3
```

- 반복문을 사용한 이진탐색
- 처음부터 정렬된 경우, 또는 값이 하나만 존재하는 경우에는 반복문 이전에 처리를 해줬음
- 반복문 도중 하나만 남을 경우, 그 값을 리턴
- nums[low] < nums[high] 경우는 정렬이 되어 있는 경우라서 nums[low]
- mid값 앞에 최대값이 존재하는 경우, 최소값이 mid가 탈락되는 문제를 nums[mid - 1]의 값을 체크하는 것으로 해결
- rotate가 일어난 경우 최소값은 정렬되지 않은 쪽에 존재하기 때문에 그 영역을 반복문으로 돌림

#### < solution_findMin2 >
```
05/08/2022 03:48	Accepted	43 ms	14.2 MB	python3
05/08/2022 03:47	Accepted	55 ms	14.1 MB	python3
05/08/2022 03:47	Accepted	78 ms	14.3 MB	python3
```
- low < high 반복문 조건으로 하나가 오는 경우 체크 가능
- mid앞 값이 최대값이 올 경우 생길 수 있는 문제는 반복문을 돌릴 때 mid 값을 포함시키는 것으로 해결
- 조건을 생략한 대신 전체적인 성능이 기존 코드에 비해서 떨어지는 경향이 있음

#### < solution_findMin3 >
```
05/08/2022 03:33	Accepted	45 ms	14.1 MB	python3
05/08/2022 03:33	Accepted	56 ms	14.1 MB	python3
05/08/2022 03:32	Accepted	91 ms	14.3 MB	python3
```
- 정렬된 케이스도 이진탐색, 숫자가 클 때는 유의미하지만 제약조건처럼 범위가 작을 때는 큰 차이가 없음

#### < solution_findMin4 >
```
05/08/2022 04:11	Accepted	38 ms	14.5 MB	python3
05/08/2022 04:11	Accepted	70 ms	14.4 MB	python3
05/08/2022 04:11	Accepted	50 ms	14.3 MB	python3
```
- findMin3의 코드를 재귀로 풀이
- 반복문보다 메모리 사용량이 늘어남
- 시간적으로는 기존 반복문보다 짧아짐, 대체로 findMin1과 비슷한 걸로 봐서는 반복문 조건 체크 할 때 if보다 시간 소모가 더 클 수도 있다는 생각이 듬 -> 확인 필요
- 메모리 문제를 고려하지 않는다면, 재귀와 반복문의 차이는 없는 듯함
