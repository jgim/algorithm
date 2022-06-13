'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''

# Definition for singly-linked list.

from typing import Optional


class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class LinkedList:
	def __init__(self, val=0):
		self.head = ListNode(val)

	def append(self, val):
		cur = self.head
		while cur.next is not None:
			cur = cur.next
		cur.next = ListNode(val)

	def print_all(self):
		cur = self.head
		while cur is not None:
			print(cur.val)
			cur = cur.next

# class Solution:
# 	def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
# 		curent1 = list1
# 		curent2 = list2
# 		while curent1.next is not None:
# 			if curent1.val >= curent2.val:
# 				ListNode(1).val = curent1.val
# 				curent1 = curent1.next
# 			else
# 				ListNode()


# 		return

list1 = LinkedList(1)
list1.append(3)
list1.append(5)

list2 = LinkedList(1)
list2.append(3)
list2.append(6)

list3 = LinkedList()
list3.append(1)
list3.append(2)

list3.print_all()

# solution.mergeTwoLists(list1, list2)

