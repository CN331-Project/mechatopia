from itertools import count 
import sys 
counter = count(1) 
line = sys.argv[next(counter)].split("_")
line2 = sys.argv[next(counter)]

line.sort()

if(line2 == "ABC"):
	print(line[0],line[1],line[2])
elif(line2 == "ACB"):	
	print(line[0],line[2],line[1])
elif(line2 == "BAC"):
	print(line[1],line[0],line[2])
elif(line2 == "BCA"):
	print(line[1],line[2],line[0])
elif(line2 == "CAB"):
	print(line[2],line[0],line[1])
elif(line2 == "CBA"):
	print(line[2],line[1],line[0])



