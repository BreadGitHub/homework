N = input("How many numbers?:")
N = int(N)
sum = 1
if N <= 0:
    print("Nope")
    exit()
for i in range(1,N+1):
    sum *= i
print(sum)