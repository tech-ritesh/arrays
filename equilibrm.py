arr=[1,3,5,2,2]
n=len(arr)
lsum=0
s=sum(arr)
for i in range(len(arr)):
    s=s-arr[i]
    if lsum != s:
        lsum=lsum+arr[i]

    else:
        print(i+1)
    





