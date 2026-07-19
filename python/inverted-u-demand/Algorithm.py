from Main1 import ModelData
from Main1 import Solution
from Main1 import NSGA2, PrintEndTime

import matplotlib.pyplot as plt
import numpy as np

data = ModelData()

sol = Solution()

nPop = 35
maxiter =100
MuteRate = .06
CrossRate = .7
nbOffSpring = 5
k = 3
N_ = int(nPop * 4 / 5) + 1

GA = NSGA2(nPop)

Solutions = GA.Initial_sol(data)
GA.Evaluate(Solutions, data)
GA.FitnessAssignment(Solutions, k)
Y = []
X = []
GA.Evaluate(Solutions, data)
for Iter in range(1, maxiter + 1):
    Pareto = GA.ParetoFrontiers(Solutions)

    LastSol = Solutions

    GA.FitnessAssignment(Solutions, k)

    F = {sol: -sol.F for sol in Solutions}

    SortedF = sorted(F, key=F.get)

    Solutions = SortedF[:nPop]

    EnvSelected = GA.EnvironmentalSelection(Solutions, N_)

    NewSolutions = GA.Variation(EnvSelected, nbOffSpring, CrossRate, MuteRate, data)

    GA.Evaluate(NewSolutions, data)

    Solutions.extend(NewSolutions)

    print("iter %s : obj1=%s  obj2=%s " % (Iter, Solutions[0].obj1, Solutions[0].obj2))

    Y.append(Solutions[0].obj1)

plt.close()
plt.clf()
plt.figure(1)
plt.xlabel('OBJ1')
plt.ylabel('OBJ2')

#sol1=Solution()
#sol1.obj1=223596
#sol1.obj2=8223596

#sol2=Solution()
#sol2.obj1=3564
#sol2.obj2=9223596

#sol3=Solution()
#sol3.obj1=923596
#sol3.obj2=10223596


#optimal=[sol1,sol2,sol3]
#LastSol.extend(optimal)
#Pareto.append([nPop+1,nPop+2,nPop+3])


for front in Pareto[:4]:
    CLR = np.random.rand(1, 3).tolist()[0]
    print(front)
    F1 = []
    F2 = []
    for ind in front:
        F1.append(LastSol[ind].obj1)
        F2.append(LastSol[ind].obj2 )
    X = []
    Y = []
    while len(F1) > 0:
        maxF1 = -1e7
        maxF2 = -1e7
        point_ind = 0
        for ind in range(len(F1)):
            if F1[ind] >= maxF1 and F2[ind] >= maxF2:
                point_x = F1[ind]
                point_y = F2[ind]
                maxF1 = F1[ind]
                maxF2 = F2[ind]
                point_ind = ind
        F1.pop(point_ind)
        F2.pop(point_ind)
        X.append(point_x)
        Y.append(point_y)

    plt.plot(X, Y, '.-', color=CLR, markersize=10)

print('======== Obj1 =========')
print(Solutions[0].obj1)
print('======== Obj2 =========')
print(Solutions[0].obj2)
plt.show()

Solutions[0].X
Solutions[0].Yn






