***

### Subject

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.


#### Example:

Example 1:
```
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

Example 2:
```
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
```

Example 3:
```
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```

#### constraints

```
1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
```

***

### result

#### < solution >
```
05/11/2022 22:28	Accepted	101 ms	14.4 MB	python3
05/11/2022 22:28	Accepted	73 ms	14.4 MB	python3
05/11/2022 22:28	Accepted	80 ms	14.4 MB	python3
```
- RPN (역폴란드 표기법, 후위 표기법)
- 스택으로 해결, RPN 경우에는 먼저 pop을 한 값이 뒤에 오기 때문에 자리를 바꿔줘야함
- 기타 문제 해결 방식은 계산기 만드는 방식과 같음

***
