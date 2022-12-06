arr=[1,2,3,4,5,6,7,8,9,10]
N=len(arr)
S=15
d={}
s1=0
for i in range (N):
    s1=s1+arr[i]
    if s1==S:
        print(0,i)
        break
    if s1-S in d:
        print(d[s1-S]+1,i)
    else:
        d[s1]=i


