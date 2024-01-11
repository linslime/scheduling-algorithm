LENGTH = 14
MAX = 8
STEP = [0,2,3,4]

def decode(list):
    ans = [0 for i in range(LENGTH)]
    now = 0
    for i in list:
        l = STEP[i]
        while l > 0:
            # print(now)
            ans[now] = 1
            now +=1
            l -= 1
        now += 1
    return ans

def dfs():
    ans = []
    list = [0]
    isNext = 1
    while len(list) > 0:
        if sum([STEP[i] for i in list]) <= MAX - 2 and sum([STEP[i] for i in list]) + len(list) < LENGTH and isNext == 1:
            list.append(0)
            isNext = 1
        elif list[-1] != len(STEP) - 1:
            list [-1] += 1
            isNext = 1
            if sum([STEP[i] for i in list]) <= MAX and sum([STEP[i] for i in list]) + len(list) - 1 <= LENGTH:
                ans.append(decode(list))
        else:
            list.pop()
            isNext = 0
    return ans


if __name__ == "__main__":
    list = dfs()
    print(list)
    print(len(list))