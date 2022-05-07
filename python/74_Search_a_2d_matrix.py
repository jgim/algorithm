# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix.
# This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

from typing import List
import bisect

class Solution1:
	def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
		start = 0
		end = len(matrix)
		arr_end = len(matrix[0]) - 1
		pivot = start + end // 2
		while start < end:
			if matrix[pivot][arr_end] == target:
				return 1
			elif matrix[pivot][arr_end] < target:
				start = pivot + 1
			elif matrix[pivot][arr_end] > target:
				if matrix[pivot][0] == target:
					return 1
				elif matrix[pivot][0] > target:
					end = pivot - 1
				elif matrix[pivot][0] < target:
					arr_start = 0
					arr_pivot = (arr_start + arr_len) // 2
					while (arr_start < arr_len):
						if (matrix[pivot][arr_pivot] == target):
							return 1
						elif matrix[pivot][arr_pivot] > target:
							arr_len = arr_pivot - 1
						elif matrix[pivot][arr_pivot] < target:
							arr_start = arr_pivot + 1
					return 0


solution1 = Solution1()

matrix = [list(map(int, input().split())) for _ in range(5)]
target = int(input())

result1 = solution1.searchMatrix(matrix, target)
print ("solution 1 : ", result1)


