from itertools import count 
import sys 
counter = count(1) 
n = int(sys.argv[next(counter)])
list = []
for i in range(n):
	list.append(int(sys.argv[next(counter)]))

list.sort()

print(list[0])
print(list[-1])




