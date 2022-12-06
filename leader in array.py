A=[16,17,4,3,5,2]
N=len(A)
l=[]
for i in range(N):
    while l and l[-1]<A[i]:
        l.pop()
        print(l)
    
    l.append(A[i])
    print(l)