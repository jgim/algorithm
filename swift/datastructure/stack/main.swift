#!/usr/bin/swift

func test_stack()
{
	let array = ["A", "B", "C", "D"]
	var stack = Stack(array)

	print(stack)
	stack.push("E")
	stack.push("F")
	stack.push("G")
	stack.push("H")
	print(stack)
	stack.pop()

	if let poppedElement = stack.pop()
	{
		assert("G" == poppedElement, "this is not stack")
		print ("Popped: \(poppedElement)")
	}
	if !stack.isEmpty
	{
		print ("stack is not empty")
	}

	var stack2: Stack = [1.0, 2.0, 3.0, 4.0]
 	 print(stack2)
 	 stack2.pop()
}

test_stack()
