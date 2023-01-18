from collections import deque #adds and remove elements from both ends of the program. 
queue= deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

print(queue)
x = queue.popleft()
print(x)
print(queue)