class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

def append(data):
	node = head
	while node.next:
		node = node.next
	node.next = ListNode(data)

listnode1 = ListNode(1)
listnode2 = ListNode(2)

print(listnode1.val) #1
print(listnode1.next) #none
print(listnode2.val) #2
print(listnode2.next) #none
1, None
2, None
#연결하기 전 next는 없음

print("\n------------------------------\n")
listnode1.next = listnode2
print(listnode1.val) #1
print(listnode1.next) #<__main__.ListNode object at 0x101e72eb0>
print(listnode2.val) #1
print(listnode2.next) #non
print("\n------------------------------\n")
# 연결 후 listnode1.next의 값이 <__main__.ListNode object at 0x101e72eb0>으로 변경
# 메모리 주소 0x101e72eb0 위치에 새로운 ListNode 객체가 생겼다는 말

listnode3 = ListNode(3)
listnode2.next = listnode3
print("\n------------------------------\n")
listnode1.next = listnode2
print(listnode1) #<__main__.ListNode object at 0x10d4abbb0>
print(listnode1.val) #1
print(listnode1.next) #<__main__.ListNode object at 0x10d4abeb0>
print(listnode2) #<__main__.ListNode object at 0x10d4abeb0>
print(listnode2.val) #2
print(listnode2.next) #<__main__.ListNode object at 0x10d4b6e80>
print(listnode3.val) #3
print(listnode3.next) #None
print("\n------------------------------\n")
#실행을 다시 하면 메모리 주소가 바뀜
#노드를 직접 출력하면 이전 node에서 next로 호출한 것과 같은 값이 나옴
#그 때 생성된 것이 아니라 생성된 객체의 주소를 확인하는 것

print("\n------------------------------\n")
print(listnode1.val) #1
print(listnode1.next.val) #2
print(listnode2.val) #2
print(listnode2.next.val) #<2
print(listnode3.val) #3
#print(listnode3.next.val) #AttributeError 'NoneType' object has no attribute 'val'
print("\n------------------------------\n")
#존재하지 않는 값을 호출할 경우 AttributeError가 발생
#next의 값을 출력하면, 다음 노드의 값이 출력

print("\n------------------------------\n")
head = listnode1
print (head) #<__main__.ListNode object at 0x10d4abbb0>
print("\n------------------------------\n")
#head를 출력하면 listnode1의 메모리 주소가 나옴

append(4)
while head:
	print(head)
	print(head.val)
	head = head.next

#값을 추가
#이것을 이용해서 linkedlist 생성 가능

