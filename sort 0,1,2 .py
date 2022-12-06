from selectors import EpollSelector


a=[0,1,2,0,1,2]
lo = 0
hi = len(a)-1
mid = 0
# Iterate till all the elements
# are sorted
while mid <= hi:
    # If the element is 0
    if a[mid] == 0:
        a[lo], a[mid] = a[mid], a[lo]
        lo = lo + 1
        mid = mid + 1
    # If the element is 1
    elif a[mid] == 1:
        mid = mid + 1
    # If the element is 2
    else:
        a[mid], a[hi] = a[hi], a[mid]
        hi = hi - 1
print(a)
