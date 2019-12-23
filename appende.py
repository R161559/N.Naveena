#appending array by taking even as condition
import numpy as np
a=np.asarray([1,2,3,4,5,6,7,8])
b=([0])
l=len(a)
for i in range(0,l):
	if(a[i]%2==0):
		b=np.append(b,a[i])
print b
#appending array by taking primenumber as condition
a=([1,2,3,4,5,6,7,8,9])
b=([0])
l=len(a)
n=0
while(n<l):
	i=1
	count=0
	while(i<a[n]):
		if(a[n]%i==0):
			count=count+1
		i=i+1
	if(count==1):
		b=np.append(b,a[n])

	n=n+1
print b
	

