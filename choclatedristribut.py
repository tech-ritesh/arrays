A=[3, 4, 1, 9, 56, 7, 9, 12]
M=5
N=len(A)
A.sort()
mindif = A[N-1]-A[0]
for i in range(len(A)-M+1):
    mindif = min (mindif,A[i+M-1]-A[i])
print( mindif)
    