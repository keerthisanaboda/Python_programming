n=int(input())
reverse=0
while n>0:
     digit=n%10
     reverse=reverse*10+digit
    n=n//10
print("Reversed number=",reverse)

#n=123  Reversed number= 123
