***

### Subject

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.


#### Example:

Input
```
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
```

Output
```
[null,null,null,null,-3,null,0,-2]
```

Explanation
```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

#### constraints

```
-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin
```

***

### result

#### < solution Minstack1>
```
05/11/2022 15:43	Accepted	55 ms	18 MB	python3
05/10/2022 03:25	Accepted	80 ms	18.1 MB	python3
05/10/2022 03:25	Accepted	76 ms	18 MB	python3
```
입력 값이 쌓이는 스택(stack), 최소값이 쌓이는 스택(min_stack) 2개를 만들었음
push -> min_stack의 top에 있는 값보다 입력되는 값이 더 작으면 min_stack에 val 값을 입력

#### < solution Minstack2>
```
05/11/2022 21:14	Accepted	58 ms	18.4 MB	python3
05/11/2022 21:14	Accepted	111 ms	18.3 MB	python3
05/11/2022 21:14	Accepted	127 ms	18.5 MB	python3
```
이중 리스트를 만들어서 값을 넣어줌, 코드는 짧아졌으나 전체적으로 시간과 메모리를 더 많이 사용함

***
