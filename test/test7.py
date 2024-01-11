import random

class C(object):
    def __init__(self):
        self.T = 7
        self.K = 15

    def createC(self):
        list = []
        for i in range(self.T):
            a = int(self.K * 2 / 3)
            list1 = [random.randint(1, 10) for i in range(a)]
            list1.sort()
            list2 = [random.randint(1, 10) for i in range(self.K - a)]
            list2.sort(reverse=True)
            a = list1 + list2
            for j in range(1, len(a), 2):
                temp = int((a[j] + a[j - 1]) / 2)
                a[j] = temp
                a[j - 1] = temp
            a[0] = 1
            a[-1] = 2
            list.append(a)
        return list

if __name__ == "__main__":
    c = C()
    print(c.createC())