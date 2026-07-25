P ,R,T=map(int,input().split())

A = P * (1 + R/100) ** T
CI = A - P

print("Compound interest:", CI)
#output:
#10000 2 5
#Compound interest: 1040.8080320000008
