arr=[2, 4, 1, 3, 5]
#two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
c=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            c=c+1
print(c)