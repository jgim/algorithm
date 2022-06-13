'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
'''

from typing import List

class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		dictionary = {}
		for str in strs:
			if str not in dictionary:
				tmp = sorted(str)
				if tmp not in dictionary:
					dictionary[tmp] += 1

solution = Solution()

strs = [n.strip("\"\"") for n in list(input().split(','))]

solution.groupAnagrams(strs)
