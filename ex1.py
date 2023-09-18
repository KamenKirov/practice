n = int(input())
stack = []
max_stack = []  # To track maximum values
min_stack = []  # To track minimum values

for _ in range(n):
    query = input().split()

    if query[0] == '1':
        num = int(query[1])
        stack.append(num)

        if not max_stack or num >= max_stack[-1]:
            max_stack.append(num)

        if not min_stack or num <= min_stack[-1]:
            min_stack.append(num)
    elif query[0] == '2':
        if stack:
            removed_num = stack.pop()

            if removed_num == max_stack[-1]:
                max_stack.pop()

            if removed_num == min_stack[-1]:
                min_stack.pop()
    elif query[0] == '3':
        if max_stack:
            print(max_stack[-1])
    elif query[0] == '4':
        if min_stack:
            print(min_stack[-1])

# Print the stack from top to bottom
stack_contents = stack[::-1]
print(', '.join(map(str, stack_contents)))
