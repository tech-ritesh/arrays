arr=[1, 2, 4, 5, 3, 7, 6]
N=8
n=len(arr)
for i in arr:
    total=sum(arr)
    s=(N)*(N+1)//2
    a=s-total
print(a)
print(s)

temp=[0]*(n+1)

for i in range(0,len(arr)):
    temp[arr[i]-1]=1

for j in range(0,n+1):
    if temp[j]==0:
        ans= j+1
print(temp)
print(ans)
priint(uihd)
