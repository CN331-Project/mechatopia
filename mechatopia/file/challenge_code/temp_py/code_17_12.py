from itertools import count 
import sys 
counter = count(1) 
n1 = int(sys.argv[next(counter)])
n2 = int(sys.argv[next(counter)])
n3 = int(sys.argv[next(counter)])
n = n1+n2+n3

if n >= 80:
   ans = "A"
elif n>=75:
   ans = "B+"
elif n>=70:
   ans = "B"
elif n>=65:
   ans = "C+"
elif n>=60:
   ans = "C"
elif n>=55:
   ans = "D+"
elif n>=50:
   ans = "D"
else:
   ans = "F"
print(ans)




