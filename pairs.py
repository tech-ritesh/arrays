x=[2,1,6]
y=[1,5]
n=len(x)
m=len(y)
#pairs such that xpow(y)>ypow(x)
pairs=0
for i in range(n):
    for j in range(m):
        if pow(x[i],y[j])> pow(y[j],x[i]):
            pairs=pairs+1
print(pairs)