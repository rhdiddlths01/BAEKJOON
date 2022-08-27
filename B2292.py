N = int(input())

def sum(n):
    return (3*n*(n+1) + 2)

num = 1
if N == 1:
    print(1)
else : 
    while N >= sum(num-1):
        num += 1
    print(num)
