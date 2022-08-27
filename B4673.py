num = [0]

def nextnum(n):
    answer = 0
    n = list(map(int, str(n)))

    for i in range(len(n)):
        answer += n[i]

    return answer

for i in range(10000):
    num.append(i+1) #num[1] = 1부터 num[1000]=1000
    
for i in range(10000):
    result = i+1
    while result<10001:
        result = nextnum(result) + result
        if result<=10000:
            num[result] = 0
       

num = [item for item in num if item != 0]

for i in range(len(num)):
    print(num[i])