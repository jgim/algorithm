'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
'''

from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
	def __init__(self, val):
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

	def get_node(self, index):
		count = 0
		node = self.head
		while count < index:
			count += 1
			node = node.next
		return node

	def add_node(self,index,val):
		new_node = ListNode(val)
		if index is 0:
			new_node.next = self.head
			self.head = new_node
			return
		node = self.get_node(index - 1)
		next_node = node.next
		node.next = new_node
		new_node.next = next_node

class Solution:
	def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		tail = None
		while head:
			node = head
			head = head.next
			node.next = tail
			tail = node
		return tail

list = LinkedList(1)
solution = Solution()

list.append(2)
list.append(3)
list.append(4)
list.append(5)

print("-")
list.print_all()
print("-")
list.head = solution.reverseList(list.head)
list.print_all()
print("-")

'''
< solution >

05/18/2022 19:52	Accepted	39 ms	15.4 MB	python3
05/18/2022 19:52	Accepted	51 ms	15.4 MB	python3
05/18/2022 19:51	Accepted	54 ms	15.4 MB	python3

linkelist를 직접 구현하여 테스트 케이스를 만들어 봄
스왑으로 list의 순서를 변경 후, tail(마지막 노드의 주소) 값을 리턴
'''
