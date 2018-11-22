import numpy as np
a = [x for x in input().split(" ")]
b = [x for x in input().split(" ")]
d_a = {}
d_b = {}
for x in a:
    x = x.split(',')
    d_a[int(x[0])]=float(x[1])

for x in b:
    x = x.split(',')
    d_b[int(x[0])]=float(x[1])

print("set A "+str(d_a))
print("set B "+str(d_b))

hamming_dist = 0.0
euclidean_dist = 0.0

for x in d_a.keys():
    if x in d_b.keys():
        hamming_dist+=(abs(d_a[x]-d_b[x]))
        euclidean_dist+=((d_a[x]-d_b[x])**2)
    else:
        hamming_dist+=d_a[x]
        euclidean_dist+=(d_a[x]**2)
        
for x in d_b.keys():
    if x not in d_a.keys():
        hamming_dist+=d_b[x]
        euclidean_dist+=(d_b[x]**2)

euclidean_dist = np.sqrt(euclidean_dist)
        
print("Hamming distance: "+str(hamming_dist))
print("Euclidean distance: "+str(euclidean_dist))
