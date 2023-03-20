n=int(input())
kusti = list()
for i in range (n):
    kusti.append(int(input()))

result=list()
for i in range(len(kusti)-1):
    result.append(kusti[i-1]+kusti[i]+kusti[i+1])
result.append(kusti[0]+kusti[-1]+kusti[-2])
print(max(result))