cloathes_stack = [int(x) for x in input().split()]
rack_capacity = int(input())

racks = 0

while cloathes_stack:
    racks+= 1
    current_rack_capacity = rack_capacity
    while cloathes_stack and cloathes_stack[-1] <= current_rack_capacity:
        current_rack_capacity -= cloathes_stack.pop()

print(racks)