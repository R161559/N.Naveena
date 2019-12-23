#finding factorial of the elements in an array and storing it in an another array
import numpy as np
a=np.asarray([1,2,3,4,5,6,7])
l=len(a)
n=0
while(n<l):
	fact=1
	i=1
	while(i<=a[n]):
		fact=fact*i
		i=i+1
	a[n]=fact
	n=n+1
print a
#finding factorial using function
a=np.asarray([1,2,3,4,5,6,7])
l=len(a)
for i in range (0,l):
	b=np.math.factorial(a[i])
	a[i]=b
print a

