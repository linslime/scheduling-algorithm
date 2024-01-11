import random
import gurobipy
import numpy as np

class Solver(object):
    def __init__(self,T,I,J,K):
        self.T = T
        self.I = I
        self.J = J
        self.K = K
        self.MAX = 8
        self.STEP = [0,2,3,4]
        self.A, self.B, self.C, self.D = self.createDate()

    def decode(self,list):
        ans = [0 for i in range(self.K)]
        now = 0
        for i in list:
            l = self.STEP[i]
            while l > 0:
                # print(now)
                ans[now] = 1
                now += 1
                l -= 1
            now += 1
        return ans

    def createA(self):
        ans = []
        list = [0]
        isNext = 1
        while len(list) > 0:
            if sum([self.STEP[i] for i in list]) <= self.MAX - 2 and sum([self.STEP[i] for i in list]) + len(list) < self.K and isNext == 1:
                list.append(0)
                isNext = 1
            elif list[-1] != len(self.STEP) - 1:
                list[-1] += 1
                isNext = 1
                if sum([self.STEP[i] for i in list]) <= self.MAX and sum([self.STEP[i] for i in list]) + len(list) - 1 <= self.K:
                    ans.append(self.decode(list))
            else:
                list.pop()
                isNext = 0
        self.J = len(ans)
        return ans

    def createB(self):
        return [[[1 for j in range(self.J)] for i in range(self.I)] for t in range(self.T)]

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

    def createDate(self):
        return self.createA(), self.createB(), self.createC(), 40

    def solver(self):
        A, B, C, D = self.A,self.B,self.C,self.D
        # 模型建立
        MODEL = gurobipy.Model()

        # 定义变量
        x = MODEL.addVars(self.T, self.I, self.J, vtype=gurobipy.GRB.BINARY, name="x")

        # 更新模型
        MODEL.update()

        # 目标函数
        # MODEL.setObjective(sum([sum([f[j] * p[i, j] for j in J]) for i in I]), gurobipy.GRB.MINIMIZE)
        MODEL.setObjective(gurobipy.quicksum(gurobipy.quicksum(gurobipy.quicksum(gurobipy.quicksum(x[t, i, j] * A[j][k] for j in range(self.J)) for k in range(self.K)) for t in range(self.T)) for i in range(self.I)) - gurobipy.quicksum(C[t][k] for t in range(self.T) for k in range(self.K)),gurobipy.GRB.MINIMIZE)

        MODEL.addConstrs(gurobipy.quicksum(gurobipy.quicksum(gurobipy.quicksum(x[t, i, j] * A[j][k] for j in range(self.J)) for k in range(self.K)) for t in range(self.T)) <= D for i in range(self.I))
        # MODEL.addConstrs(gurobipy.quicksum(gurobipy.quicksum(gurobipy.quicksum(x[t, i, j] * A[j][k] for j in range(self.J)) for k in range(self.K)) for t in range(self.T)) >= 25 for i in range(self.I))
        MODEL.addConstrs(gurobipy.quicksum(x[t, i, j] * A[j][k] for j in range(self.J) for i in range(self.I)) >= C[t][k] for t in range(self.T) for k in range(self.K))
        MODEL.addConstrs(gurobipy.quicksum(x[t, i, j] for j in range(self.J)) <= 1 for t in range(self.T) for i in range(self.I))
        MODEL.addConstrs(x[t, i, j] <= B[t][i][j] for t in range(self.T) for i in range(self.I) for j in range(self.J))

        MODEL.Params.LogToConsole = False  # 显示求解过程
        MODEL.Params.MIPGap = 0.0001  # 百分比界差
        # MODEL.Params.TimeLimit = 10  # 限制求解时间为 100s
        MODEL.optimize()
        y = np.zeros((self.T, self.I, self.K))
        for t in range(self.T):
            for i in range(self.I):
                for k in range(self.K):
                    y[t][i][k] = sum(x[t, i, j].x * A[j][k] for j in range(self.J))
        return y

if __name__ == "__main__":
    solver = Solver(7,16,0,12)
    y = solver.createC()
    print(y)