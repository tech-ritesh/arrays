arr1=[1 ,3, 5 ,7]
arr2=[0, 2 ,6 ,8 ,9]
c=[]
n=len(arr1)
m=len(arr2)

i=0
j=0
while i<n and j<m:
    if arr1[i] < arr2[j]:
        c.append(arr1[i])
        i=i+1
    else:
        c.append(arr2[j])
        j=j+1
while i<n:
    c.append(arr1[i])
    i=i+1
while j<m:
    c.append(arr2[j])
    j=j+1
for i in range(n):
    arr1[i]=c[i]
for i in range(m):
    arr2[i]=c[i+n]
print(c)
print(arr1)
print(arr2)
print(aarr4)



