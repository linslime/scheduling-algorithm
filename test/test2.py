import random


def createC(K):
    a = int(K*2/3)
    list1 = [random.randint(1,10)for i in range(a)]
    list1.sort()
    list2 = [random.randint(1,10)for i in range(K-a)]
    list2.sort(reverse=True)
    return list1 + list2
print(createC(10))