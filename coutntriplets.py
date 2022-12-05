arr=[2,3,4]
c=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j] in arr:
            c=c+1
            
        
print(c)
    
c=0
for i in range (len(arr)):
    l=i+1
    while l<len(arr):
        if arr[i] +arr[l] in arr:
            c=c+1
        l=l+1
print(c)

