***

### Subject

Given the head of a singly linked list, reverse the list, and return the reversed list.

#### Example:


Example 1:
```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

Example 2:
```
Input: head = [1,2]
Output: [2,1]
```

Example 3:
```
Input: head = []
Output: []
```

#### constraints

```
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
```

***

### result

#### < solution >
```
05/18/2022 19:52	Accepted	39 ms	15.4 MB	python3
05/18/2022 19:52	Accepted	51 ms	15.4 MB	python3
05/18/2022 19:51	Accepted	54 ms	15.4 MB	python3
```
- linkelist를 직접 구현하여 테스트 케이스를 만들어 봄
- 스왑으로 list의 순서를 변경 후, tail(마지막 노드의 주소) 값을 리턴

***
