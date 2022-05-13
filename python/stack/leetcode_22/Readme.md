***

### Subject

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

#### Example:

Example 1:
```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

Example 2:
```
Input: n = 1
Output: ["()"]
```

Example 3:
```
Input: n = 2
Output: ["(())", "()()"]
```

#### constraints

```
1 <= n <= 8

stack[0], stack[1]
```

***

### result

#### < solution1 >
```
05/12/2022 23:06	Accepted	32 ms	14.1 MB	python3
05/12/2022 23:06	Accepted	54 ms	14 MB	python3
05/12/2022 23:05	Accepted	54 ms	14.3 MB	python3
```
- dfs와 재귀를 통해서 문제를 해결
- 재귀는 스택 구조를 가짐
- 다만, 진짜 스택으로도 풀 수 있겠다는 생각을 해 봄

#### < solution2 >
```
05/13/2022 18:18	Accepted	48 ms	14.2 MB	python3
05/13/2022 18:17	Accepted	58 ms	14.1 MB	python3
05/13/2022 18:17	Accepted	61 ms	14.2 MB	python3
```
- 스택을 이용해서 문제를 해결
- left, right 인자를 스택에 넣지 않았는 경우 현재 진행중인 스택에 든 값의 개수 파악을 하는데 다시 시간이 듬
- left, right 인자도 리스트로 삽입
- 결국 재귀와 유사한 구조를 가짐

***
