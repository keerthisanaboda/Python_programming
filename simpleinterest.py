def fun(p, t, r):
    return (p * t * r) / 100

p, t, r = map(int,input().split())

res = fun(p, t, r)
print(res)
#output:
#1000 2 5
#100.0
