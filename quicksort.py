__author__ = 'Robert'

def quicksort (ar, n, s, e):

    aa = list(range(0,n))

    p = ar[e]
    aal = 0
    aar = -1
    l = 0
    r = 0
    y = e

    for i in range(s,e):
        if (ar[i] < p):
            if (aar != -1):
                x = aa[aal]
                aal += 1
                ar[x], ar[i] = ar[i], ar[x]
                if ar[i] > p:
                    aar += 1
                    aa[aar] = i

            l += 1
        else:
            aar += 1
            aa[aar] = i
            r += 1

    if (aal <= aar):
        x = aa[aal]
        aal += 1
        ar[x], ar[e] = ar[e], ar[x]
        y = x

    [print(i,end=' ') for i in ar]
    print()

    if (l > 1):
        ar = quicksort(ar, n, s, y-1)
    if (r > 1):
        ar = quicksort(ar, n, y+1, e)

    return(ar)

n = int(input())
ar = input().split()
ar = [int(num) for num in ar]
ar = quicksort(ar, n, 0, n-1)
