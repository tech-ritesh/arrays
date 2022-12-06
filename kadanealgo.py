arr=[1,2,3,-2,5]
#find max contiguous sum:
N=len(arr)
s=0
s1=-1
for i in range(N):
    s=s+arr[i]
    if s1<s:
        s1=s 
    elif s < 0:
        s=0
print(s1)
#or

maxsum=arr[0]
curmax=arr[0]
curmax=max(arr[i],curmax+arr[i])
maxsum=max(curmax,maxsum)
print(maxsum)
