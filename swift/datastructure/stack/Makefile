NAME = stack

SWIFT = swiftc

SRCS =	main.swift \
		stack.swift

$(NAME) :
	$(SWIFT) $(SRCS) -o $(NAME)

all : $(NAME)

clean	:
	rm -rf $(NAME)

re		: clean all

.PHONY: all clean re
