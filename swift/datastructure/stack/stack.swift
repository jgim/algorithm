public struct Stack<T> {
	private var _stack: [T] = []
	public init() {}

	public init(_ element: [T])
	{
		_stack = element
	}


	public mutating func push(_ element: T){
		_stack.append(element)
	}

	@discardableResult
	public mutating func pop() -> T?{
		_stack.popLast()
	}

	public func peek() -> T?
	{
		_stack.last
	}

	public var isEmpty: Bool
	{
		peek() == nil
	}
}

extension Stack: CustomDebugStringConvertible{
	public var debugDescription: String{
		"""
		--- top ---
		\(_stack.map{ "\($0)" }.reversed().joined(separator:"\n"))
		-----------
		"""
	}
}

extension Stack: ExpressibleByArrayLiteral {
	public init(arrayLiteral elements: T...) {
		_stack = elements
	}
}
