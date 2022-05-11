***

### Subject

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


#### Example:


Example 1:
```
Input: s = "()"
Output: true
```

Example 2:
```
Input: s = "()[]{}"
Output: true
```

Example 3:
```
Input: s = "(]"
Output: false
```

Example 4:
```
Input: s = "([])"
Output: True
```


#### constraints

```
1 <= s.length <= 104
s consists of parentheses only '()[]{}'
```

***

### result

#### < solution_isvalid1 >
```
05/09/2022 23:27	Accepted	47 ms	17.7 MB	python3
05/09/2022 23:27	Accepted	40 ms	17.7 MB	python3
05/09/2022 23:24	Accepted	34 ms	17.7 MB	python3
```
- 재귀를 통해서 푸는 방법을 생각해봄
- 가능한 경우의 수는 5가지, 그 외의 방법은 모두 False 처리
- 재귀보다 각 경우에 따라 함수를 만들어줬기 때문에 재귀 느낌이 안남

#### < solution_isvalid2 >
```
05/09/2022 23:48	Accepted	45 ms	17.6 MB	python3
05/09/2022 23:47	Accepted	55 ms	17.7 MB	python3
05/09/2022 23:47	Accepted	46 ms	17.7 MB	python3
```
- 중복되는 함수를 묶어서 하나로 만들어 줌
- 그 과정에 들어간 변수로 인해 시간이 조금 더 지연됨

#### < solution_isvalid3 >
```
05/10/2022 01:12	Accepted	36 ms	13.9 MB	python3
05/10/2022 01:12	Accepted	36 ms	14 MB	python3
05/10/2022 01:12	Accepted	32 ms	13.9 MB	python3
```
- stack을 사용해서 문제를 해결, 괄호의 순서는 스택의 순서를 따름
- {,[,(가 오는 경우 stack에 입력
- },],)가 오는 경우 stack에 있는 값을 {,[,(과 직접 비교하여 문제를 해결
- stack을 이용해서 전체적인 속도가 증가함

#### < solution_isvalid4 >
```
05/10/2022 01:17	Accepted	34 ms	13.9 MB	python3
05/10/2022 01:17	Accepted	60 ms	14 MB	python3
05/10/2022 01:17	Accepted	49 ms	13.9 MB	python3
```
- stack + dictionary를 활용해 문제를 해결
- 값을 직접 비교하는 것에 비해서 코드는 간결해졌으나 전체적으로 시간은 더 증가함
- dictonary에서 key를 value로 변경하는 과정에서 시간이 소요되는 것으로 생각됨

***
