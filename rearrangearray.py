arr=[1,2,3,4,5,6]
n=len(arr)


i=0
j=n-1
for x in range(0,n,2):
    arr[x]=arr[j]
    if (x+1 <= n-1):
        arr[x+1]=arr[i]
        j-=1
        i+=1
print(arr)