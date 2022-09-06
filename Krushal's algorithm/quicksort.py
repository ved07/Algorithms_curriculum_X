import random

List = [random.randint(1, 100) for x in range(10)]

length = len(List)

print(List)

for x in range(length):
    for idx in range(x, 0, -1):
        if List[idx-1] > List[idx]:
            temp = List[idx]
            List[idx] = List[idx-1]
            List[idx - 1] = temp
print(List)