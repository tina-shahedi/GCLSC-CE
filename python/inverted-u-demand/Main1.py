class ModelData:

    def __init__(self):
        ###  Sets
        import numpy as np
        from scipy.stats import norm

        self.J = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]  # index for distribution center
        self.I = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]  # index for customer point
        self.C = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]  # index for collection center

        J = self.J
        I = self.I
        C = self.C
        ### Model Parameters
        self.Hn = 10  # holding cost new tire in year
        self.Hr = 10  # holding cost new tire in year
        self.Hu = 10  # holding cost new tire in year

        self.Prwn = 20  # purchase cost raw material new
        self.Prwr = 10  # purchase cost raw material retread

        self.Pcn = 40  # production cost new tire
        self.Pcr = 20  # production cost retread tire

        self.XX = 360  # number of day in year
        self.Beta = .1  # factor related to transportation cost
        self.teta = .1  # factor related to holding cost

        self.alpha = 0.2  # percent of retreadable returned tire
        self.Gamma = 0.1  # fixed value for cannibalization effect in linear model
        self.Landa = 0.01  # coeficient of nirmalized the price
        self.mn = {i: np.random.randint(20, 30) for i in I}  # market potenciel scale of new tire in customer point i
        self.mr = {i: 0.85 * self.mn[i] for i in I}  # market potenciel scale of retread tire in customer point i
        self.svu = {i: np.random.randint(10, 15) for i in I}  # salvage value of used tire
        self.Fd = {j: np.random.randint(200, 300) for j in J}  # fixed constructing cost distribution center j
        self.An = {j: np.random.uniform(1, 2) for j in J}  # fixed ordering cost new tire in distribution center j
        self.Ar = {j: np.random.uniform(1, 2) for j in J}  # fixed ordering cost retread tire in distribution center j
        self.Pain = {j: 3 * self.Hn for j in J}  # backorder cost new in distribution center j
        self.Pair = {j: 3 * self.Hr for j in J}  # backorder cost retread in distribution center j
        self.Tvcn = {j: np.random.uniform(1, 2) for j in
                     J}  # Transportation variable cost of new tire from m-rem to dis ceneter j
        self.Tvcr = {j: np.random.uniform(1, 2) for j in
                     J}  # Transportation variable cost of retread tire from m-rem to dis ceneter j
        self.Tfcn = {j: np.random.uniform(1, 2) for j in
                     J}  # Transportation fixed cost of new tire from m-rem to dis ceneter j
        self.Tfcr = {j: np.random.uniform(1, 2) for j in
                     J}  # Transportation fixed cost of retread tire from m-rem to dis ceneter j

        self.Tdcn = {(i, j): np.random.uniform(1, 2) for i in I for j in
                     J}  # Transportation cost of new tire between customer i & dis center j

        self.Tdcr = {(i, j): np.random.uniform(1, 2) for i in I for j in
                     J}  # Transportation cost of retread tire between customer i & dis center j

        self.Trcu = {(i, c): np.random.uniform(1, 2) for i in I for c in
                     C}  # transportation cost used tire from customer point i to collection center c

        self.Trmu = {c: np.random.uniform(.1, 1) for i in I for c in
                     C}  # transportation cost used tire from c to m-rem

        self.Tru = {c: np.random.uniform(.1, 1) for i in I for c in
                    C}  # transportation cost used tire from c to recycle center
        self.Ln = {j: np.random.uniform(5, 10) for j in
                   J}  # lead time for new tire in dis center j

        self.Lr = {j: np.random.uniform(5, 10) for j in
                   J}  # lead time for retread tire in dis center j

        self.Sigman1 = {i: 0.01 for i in I}  # standard deviation of nue i  for new tire
        self.Sigmar1 = {i: 0.01 for i in I}  # standard deviation of nue i  for retread tire
        self.Sigman2 = {i: 0.01 for i in I}  # standard deviation of epsilon i  for new tire
        self.Sigmar2 = {i: 0.01 for i in I}  # standard deviation of epsilon i  for retread tire
        self.tn = {j: np.random.uniform(5, 10) for j in
                   J}  # inventory review interval in dis center j for new tire
        self.tr = {j: np.random.uniform(5, 10) for j in
                   J}  # inventory review interval in dis center j for retread tire

        self.Tu = {c: 7 for c in C}  # inventory review interval in collection center c for used tire
        self.Fc = {c: np.random.uniform(100, 300) for c in C}  # fixed cost of constructing collection center c

        self.Bu = {(i, c): np.random.uniform(10, 20) for i in I for c in
                   C}  # quantity of returned used tire from customer point i to collection cenetr c
        self.Rs = {(i, c): np.random.uniform(10, 20) for i in I for c in
                   C}  # Selling price used tire returned from customer point i by collection center c to m-rem center
        self.Rp = {(i, c): np.random.uniform(10, 20) for i in I for c in
                   C}  # Selling price used tire returned from customer point i by collection center c to recycle center
        self.eI = {j: np.random.uniform(1, 3) for j in
                   J}  # environmental Impact transporting to dis center j
        self.eIs = {j: np.random.uniform(10, 20) for j in
                    J}  # environmental Impact establish dis center j
        self.eId = {(i, j): np.random.uniform(1, 3) for i in I for j in
                    J}  # environmental Impact transporting from dis center j to customer point i
        self.eIc = {(i, c): np.random.uniform(3, 5) for i in I for c in
                    C}  # environmental Impact transporting from customer point i to collection center c

        self.eIm = {c: np.random.uniform(1, 2) for c in
                    C}  # environmental Impact transporting from collection center c to m-rem center
        self.eIr = {c: np.random.uniform(1, 2) for c in
                    C}  # environmental Impact transporting from collection center c to recycle center
        self.eIe = {c: np.random.uniform(2, 3) for c in C}  # environmental Impact establish collection center c
        teta = self.teta
        Hn = self.Hn
        tn = self.tn
        tr = self.tr
        Pain = self.Pain
        Pair = self.Pair
        XX = self.XX
        Hr = self.Hr
        self.sln = {j: 1 - ((teta * Hn * tn[j]) / (Pain[j] * XX)) for j in J}  # service level new tire
        self.slr = {j: 1 - ((teta * Hr * tr[j]) / (Pair[j] * XX)) for j in J}  # service level retread tire
        sln = self.sln
        slr = self.slr
        self.Ztn = {j: norm.ppf(sln[j], 0, 1) for j in
                    J}  # Value of the accumulated standard normal distribution such that P(Z<Ztn(j))=sln(j)
        self.Ztr = {j: norm.ppf(slr[j], 0, 1) for j in
                    J}  # Value of the accumulated standard normal distribution such that P(Z<Ztr(j))=slr(j)
        Ztn = self.Ztn
        Ztr = self.Ztr
        self.phiZtn = {j: norm.cdf(Ztn[j], 0, 1) for j in
                       J}  # standard normal cumulative distribution function
        self.phiZtr = {j: norm.cdf(Ztr[j], 0, 1) for j in
                       J}  # standard normal cumulative distribution function

        self.eM = {j: np.random.uniform(5, 7) for j in
                   J}  # #distance between manufacturing-remanufac & distribution center j
        self.eD = {(i, j): np.random.uniform(1, 5) for i in I for j in J
                   }  # #distance between distribution center j & customer point i
        self.eS = {(i, c): np.random.uniform(3, 5) for i in I for c in C
                   }  # #distance between customer point i & collection center c
        self.eC = {c: np.random.uniform(1, 5) for c in C
                   }  # #distance between collection center c & manufacturing-remanufac
        self.eR = {c: np.random.uniform(2, 3) for c in C
                   }  # #distance between collection center c & Recycling center

        self.pd = {i: 0.2 for i in I}
        self.TainU = {i: -0.0391 + 6.3151 * (self.pd[i]) - 21.4636 * ((self.pd[i]) ** 2) + 24.9582 * (
                (self.pd[i]) ** 3) - 9.7866 * ((self.pd[i]) ** 4) for i in I}


class Solution():
    def __init__(self):
        # TODO: obj1 is min and the other is max
        self.obj1 = 1e5
        self.obj2 = -1e5
        self.X = {}
        self.Tpl = {}
        self.Yn = {}
        self.Yr = {}
        self.Tpu = {}
        self.pr = {}
        self.pn = {}
        self.vu = {}
        self.C1 = {}
        self.C2 = {}

    def copy(self):
        newSol = Solution()
        newSol.obj1 = self.obj1
        newSol.obj2 = self.obj2
        newSol.X = {ind: self.X[ind] for ind in self.X.keys()}
        newSol.Tpl = {ind: self.Tpl[ind] for ind in self.Tpl.keys()}
        newSol.Yn = {ind: self.Yn[ind] for ind in self.Yn.keys()}
        newSol.Yr = {ind: self.Yr[ind] for ind in self.Yr.keys()}
        newSol.Tpu = {ind: self.Tpu[ind] for ind in self.Tpu.keys()}
        newSol.pr = {ind: self.pr[ind] for ind in self.pr.keys()}
        newSol.pn = {ind: self.pn[ind] for ind in self.pn.keys()}
        newSol.vu = {ind: self.vu[ind] for ind in self.vu.keys()}
        newSol.C1 = {ind: self.C1[ind] for ind in self.C1.keys()}
        newSol.C2 = {ind: self.C2[ind] for ind in self.C2.keys()}
        return newSol


class NSGA2():
    def __init__(self, npop):
        self.npop = npop

    def Initial_sol(self, data):
        # TODO: constr79
        import numpy as np
        Solutions = []
        J = data.J
        C = data.C
        I = data.I
        Tvcr = data.Tvcr
        Tfcr = data.Tfcr
        Prwr = data.Prwr
        Landa = data.Landa
        pd = data.pd
        Rp = data.Rp
        Trcu = data.Trcu
        svu = data.svu
        tn = data.tn
        Ln = data.Ln
        Sigman2 = data.Sigman2
        Sigman1 = data.Sigman1
        mn = data.mn
        tr = data.tr
        Lr = data.Lr
        Sigmar2 = data.Sigmar2
        Sigmar1 = data.Sigmar1
        mr = data.mr
        TainU = data.TainU

        Pcr = data.Pcr
        nPop = self.npop
        for pop in range(nPop):
            sol = Solution()
            # binary variables
            num_openJ = np.random.randint(1, len(J))
            openJ = np.random.choice(J, num_openJ)
            sol.X = {j: 1 if j in openJ else 0 for j in J}

            num_openC = np.random.randint(1, len(C))
            openC = np.random.choice(C, num_openC)
            sol.Tpl = {c: 1 if c in openC else 0 for c in C}

            assign_n_ij = {i: np.random.choice(openJ, 1) for i in I}
            sol.Yn = {(i, j): 1 if j in assign_n_ij[i] else 0 for i in I for j in J}

            assign_r_ij = {i: np.random.choice(openJ, 1) for i in I}
            sol.Yr = {(i, j): 1 if j in assign_r_ij[i] else 0 for i in I for j in J}

            assign_ic = {i: np.random.choice(openC, 1) for i in I}
            sol.Tpu = {(i, c): 1 if c in assign_ic[i] else 0 for i in I for c in C}

            # positive variables
            sol.pn = {i: max(np.random.uniform((Tvcr[j] + Tfcr[j] + Prwr + Pcr) * sol.Yr[i, j], 1 / Landa) for j in J)
                      for i in I}

            sol.pr = {i: sol.pn[i] - pd[i] * sol.pn[i] for i in I}

            sol.vu = {(i, c): np.random.uniform(svu[i], min(sol.pr[i], Rp[i, c] - Trcu[i, c])) for i in I for c in C}

            sol.C1 = {j: np.sqrt(sum((tn[j] + Ln[j]) * (Sigman1[i] ** 2) * sol.Yn[i, j] * (mn[i] ** 2) * (
                    (1 - (Landa * sol.pn[i])) ** 2) * ((1 - TainU[i]) ** 2) for i in I) + sum((tn[j] + Ln[j]) * (
                    Sigman2[i] ** 2) * sol.Yn[i, j] for i in I)) for j in J}

            sol.C2 = {j: np.sqrt(sum((tr[j] + Lr[j]) * (Sigmar1[i] ** 2) * sol.Yr[i, j] * (mr[i] ** 2) * (
                    (1 - (Landa * sol.pr[i])) ** 2) for i in I) + sum(
                (tr[j] + Lr[j]) * (Sigmar1[i] ** 2) * sol.Yr[i, j] * (
                        mn[i] ** 2) * ((1 - (Landa * sol.pn[i])) ** 2) * (TainU[i] ** 2) for i in I) + sum(
                (tr[j] + Lr[j]) * (
                        Sigmar1[i] ** 2) * sol.Yr[i, j] * 2 * mr[i] * mn[i] * (1 - (Landa * sol.pn[i])) * (1 - (
                        Landa * sol.pr[i])) * TainU[i] for i in I) + sum(
                (tr[j] + Lr[j]) * (Sigmar2[i] ** 2) * sol.Yr[i, j] for i in I)) for j in J}

            Solutions.append(sol)

        return Solutions

    def Evaluate(self, Solutions, data):

        I = data.I
        J = data.J
        C = data.C
        Pcn = data.Pcn
        Prwr = data.Prwr
        XX = data.XX
        mn = data.mn
        Landa = data.Landa
        Gamma = data.Gamma
        Beta = data.Beta
        Tdcn = data.Tdcn
        An = data.An
        tn = data.tn
        Tfcn = data.Tfcn
        Tvcn = data.Tvcn
        teta = data.teta
        Hn = data.Hn
        Pain = data.Pain
        phiZtn = data.phiZtn
        Pcr = data.Pcr
        mr = data.mr
        Tdcr = data.Tdcr
        Ar = data.Ar
        tr = data.tr
        Tfcr = data.Tfcr
        Tvcr = data.Tvcr
        Hr = data.Hr
        Pair = data.Pair
        phiZtr = data.phiZtr
        Fd = data.Fd
        Rs = data.Rs
        alpha = data.alpha
        Bu = data.Bu
        Rp = data.Rp
        Fc = data.Fc
        Hu = data.Hu
        Tu = data.Tu
        Trcu = data.Trcu
        Trmu = data.Trmu
        Tru = data.Tru
        eI = data.eI
        eId = data.eId
        eIs = data.eIs
        eIc = data.eIc
        eIe = data.eIe
        eIm = data.eIm
        eIr = data.eIr
        eM = data.eM
        eS = data.eS
        eC = data.eC
        eD = data.eD
        eR = data.eR
        Prwn = data.Prwn
        TainU = data.TainU

        for sol in Solutions:
            Yn = sol.Yn
            Yr = sol.Yr
            X = sol.X
            vu = sol.vu
            pr = sol.pr
            pn = sol.pn
            C1 = sol.C1
            C2 = sol.C2
            Tpu = sol.Tpu
            Tpl = sol.Tpl

            obj1 =abs (
                    sum((pn[i] - Pcn - Prwn) * XX * mn[i] * (1 - (Landa * pn[i])) * (1 - TainU[i]) for i in I) -
                    sum(
                        Beta * XX * Tdcn[i, j] * eD[i, j] * Yn[i, j] * mn[i] * (1 - (Landa * pn[i])) * (1 - TainU[i])
                        for i in I for j in J) -
                    sum(An[j] * (XX / tn[j]) * X[j] for j in J) - sum(Beta * Tfcn[j] * (XX / tn[j]) * X[j] for j in J) -
                    sum(
                        Beta * XX * Tvcn[j] * eM[j] * Yn[i, j] * mn[i] * (1 - (Landa * pn[i])) * (1 - TainU[i]) for j in
                        J for i in I) -
                    sum(0.5 * teta * Hn * tn[j] * Yn[i, j] * mn[i] * (1 - (Landa * pn[i])) * (1 - TainU[i]) for j in J
                        for i in I) -
                    sum(((Pain[j] * XX) / tn[j]) * phiZtn[j] * C1[j] for j in J) +
                    sum((pr[i] - Pcr - Prwr) * XX * mr[i] * (1 - (Landa * pr[i])) for i in I) +
                    sum((pr[i] - Pcr - Prwr) * XX * mn[i] * (1 - (Landa * pn[i])) * TainU[i] for i in I) -
                    sum(Beta * XX * Tdcr[i, j] * eD[i, j] * Yr[i, j] * mr[i] * (1 - (Landa * pr[i])) for j in J for i in
                        I) -
                    sum(
                        Beta * XX * Tdcr[i, j] * eD[i, j] * Yr[i, j] * mn[i] * (1 - (Landa * pn[i])) * TainU[i] for j in
                        J for i in I) -
                    sum(Ar[j] * (XX / tr[j]) * X[j] for j in J) - sum(Beta * Tfcr[j] * (XX / tr[j]) * X[j] for j in J) -
                    sum(Beta * XX * Tvcr[j] * eM[j] * Yr[i, j] * mr[i] * (1 - (Landa * pr[i])) for j in J for i in I) -
                    sum(Beta * XX * Tvcr[j] * eM[j] * Yr[i, j] * mn[i] * (1 - (Landa * pn[i])) * TainU[i] for j in J for
                        i in I) -
                    sum(0.5 * teta * Hr * tr[j] * Yr[i, j] * mr[i] * (1 - (Landa * pr[i])) for j in J for i in I) -
                    sum(0.5 * teta * Hr * tr[j] * Yr[i, j] * mn[i] * (1 - (Landa * pn[i])) * TainU[i] for j in J for i
                        in I) -
                    sum(((Pair[j] * XX) / tr[j]) * phiZtr[j] * C2[j] for j in J) -
                    sum(Fd[j] * X[j] for j in J) + sum(
                Rs[i, c] * alpha * Bu[i, c] * Tpu[i, c] * XX for c in C for i in I) +
                    sum(Rp[i, c] * (1 - alpha) * Bu[i, c] * Tpu[i, c] * XX for c in C for i in I) -
                    sum(vu[i, c] * Bu[i, c] * XX * Tpu[i, c] for c in C for i in I) -
                    sum(Fc[c] * Tpl[c] for c in C) - sum(
                0.5 * teta * Hu * Bu[i, c] * Tpu[i, c] * Tu[c] for c in C for i in I) -
                    sum(Beta * Trcu[i, c] * eS[i, c] * Bu[i, c] * XX * Tpu[i, c] for c in C for i in I) -
                    sum(Beta * Trmu[c] * eC[c] * alpha * Bu[i, c] * Tpl[c] * XX for c in C for i in I) -
                    sum(Beta * Tru[c] * eR[c] * (1 - alpha) * Bu[i, c] * Tpl[c] * XX for c in C for i in I)
            )

            obj2 = (
                    sum(eI[j] * eM[j] * XX * Yn[i, j] * mn[i] * (1 - (Landa * pn[i])) * (1 - TainU[i]) for j in J for i
                        in I) +
                    sum(eI[j] * eM[j] * XX * Yr[i, j] * mr[i] * (1 - (Landa * pr[i])) for j in J for i in I) +
                    sum(eI[j] * eM[j] * XX * Yr[i, j] * mr[i] * (1 - (Landa * pn[i])) * TainU[i] for j in J for i in
                        I) +
                    sum(eId[i, j] * eD[i, j] * XX * Yn[i, j] * mn[i] * (1 - (Landa * pn[i])) * (1 - TainU[i]) for j in J
                        for i in I) +
                    sum(eId[i, j] * eD[i, j] * XX * Yr[i, j] * mr[i] * (1 - (Landa * pr[i])) for j in J for i in I) +
                    sum(eId[i, j] * eD[i, j] * XX * Yr[i, j] * mn[i] * (1 - (Landa * pn[i])) * TainU[i] for j in J for i
                        in I) +
                    sum(eIs[j] * X[j] for j in J) + sum(eIe[c] * Tpl[c] for c in C) +
                    sum(eIc[i, c] * eS[i, c] * Bu[i, c] * XX * Tpu[i, c] for c in C for i in I) +
                    sum(eIm[c] * eC[c] * alpha * Bu[i, c] * Tpl[c] * XX for c in C for i in I) +
                    sum(eIr[c] * eR[c] * (1 - alpha) * Bu[i, c] * Tpl[c] * XX for c in C for i in I)
            )
            sol.obj1 = obj1
            sol.obj2 = obj2

    def Mutation(self, Solutions, MuteRate, data):
        import numpy as np
        J = data.J
        C = data.C
        I = data.I
        Tvcr = data.Tvcr
        Tfcr = data.Tfcr
        Prwr = data.Prwr
        Landa = data.Landa
        Tvcn = data.Tvcn
        Tfcn = data.Tfcn
        Prwn = data.Prwn
        Pcn = data.Pcn
        Rp = data.Rp
        Trcu = data.Trcu
        svu = data.svu
        tn = data.tn
        Ln = data.Ln
        Sigman2 = data.Sigman2
        Sigman1 = data.Sigman1
        mn = data.mn
        tr = data.tr
        Lr = data.Lr
        Sigmar2 = data.Sigmar2
        Sigmar1 = data.Sigmar1
        mr = data.mr
        pd = data.pd
        Pcr = data.Pcr
        TainU = data.TainU

        MuteSolutions = []
        for sol in Solutions:
            offspring = sol.copy()

            # binary variables
            offspring.X = {ind: 1 - offspring.X[ind] if np.random.rand() < MuteRate else sol.X[ind] for ind in
                           J}
            offspring.Tpl = {ind: 1 - offspring.Tpl[ind] if np.random.rand() < MuteRate else sol.Tpl[ind] for ind
                             in C}

            openJ = [j for j in J if offspring.X[j] > 0]
            if not openJ:
                num_openJ = np.random.randint(1, len(J))
                openJ = np.random.choice(J, num_openJ)

            assign_n_ij = {i: np.random.choice(openJ, 1) for i in I}
            offspring.Yn = {(i, j): 1 if j in assign_n_ij[i] else 0 for i in I for j in J}

            assign_r_ij = {i: np.random.choice(openJ, 1) for i in I}
            offspring.Yr = {(i, j): 1 if j in assign_r_ij[i] else 0 for i in I for j in J}

            openC = [c for c in C if offspring.Tpl[c] > 0]
            if not openC:
                num_openC = np.random.randint(1, len(C))
                openC = np.random.choice(C, num_openC)
            assign_ic = {i: np.random.choice(openC, 1) for i in I}
            offspring.Tpu = {(i, c): 1 if c in assign_ic[i] else 0 for i in I for c in C}

            # positive variables
            offspring.pn = {i: max(np.random.uniform((Tvcr[j] + Tfcr[j] + Prwr + Pcr) * offspring.Yr[i, j], 1 / Landa)
                                   for j in J) if np.random.rand() < MuteRate else sol.pn[i]
                            for i in I}

            offspring.pr = {i: offspring.pn[i] - pd[i] * offspring.pn[i] for i in I}

            offspring.vu = {(i, c): np.random.uniform(svu[i], min(offspring.pr[i], Rp[i, c] - Trcu[i, c])) for i in I
                            for c in C}

            offspring.C1 = {j: np.sqrt(sum((tn[j] + Ln[j]) * (Sigman1[i] ** 2) * offspring.Yn[i, j] * (mn[i] ** 2) * (
                    (1 - (Landa * offspring.pn[i])) ** 2) * ((1 - TainU[i]) ** 2) for i in I) + sum((tn[j] + Ln[j]) * (
                    Sigman2[i] ** 2) * offspring.Yn[i, j] for i in I)) for j in J}

            offspring.C2 = {j: np.sqrt(sum((tr[j] + Lr[j]) * (Sigmar1[i] ** 2) * offspring.Yr[i, j] * (mr[i] ** 2) * (
                    (1 - (Landa * offspring.pr[i])) ** 2) for i in I) + sum(
                (tr[j] + Lr[j]) * (Sigmar1[i] ** 2) * offspring.Yr[i, j] * (
                        mn[i] ** 2) * ((1 - (Landa * offspring.pn[i])) ** 2) * (TainU[i] ** 2) for i in I) + sum(
                (tr[j] + Lr[j]) * (
                        Sigmar1[i] ** 2) * offspring.Yr[i, j] * 2 * mr[i] * mn[i] * (1 - (Landa * offspring.pn[i])) * (
                        1 - (
                        Landa * offspring.pr[i])) * TainU[i] for i in I) + sum(
                (tr[j] + Lr[j]) * (Sigmar2[i] ** 2) * offspring.Yr[i, j] for i in I)) for j in J}

        MuteSolutions.append(offspring)

        return MuteSolutions

    def CrossOver(self, Solutions, nbOffSpring, CrossRate, data):
        import numpy as np
        J = data.J
        C = data.C
        I = data.I
        Tvcr = data.Tvcr
        Tfcr = data.Tfcr
        Prwr = data.Prwr
        Landa = data.Landa
        Tvcn = data.Tvcn
        Tfcn = data.Tfcn
        Prwn = data.Prwn
        Pcn = data.Pcn
        Rp = data.Rp
        Trcu = data.Trcu
        svu = data.svu
        tn = data.tn
        Ln = data.Ln
        Sigman2 = data.Sigman2
        Sigman1 = data.Sigman1
        mn = data.mn
        tr = data.tr
        Lr = data.Lr
        Sigmar2 = data.Sigmar2
        Sigmar1 = data.Sigmar1
        mr = data.mr
        TainU = data.TainU
        pd = data.pd
        Pcr = data.Pcr
        TotalOffspring = []
        for n in range(nbOffSpring):
            parent1 = np.random.choice(Solutions, 1, replace=False).tolist()[0]
            parent2 = np.random.choice(Solutions, 1, replace=False).tolist()[0]

            offspring1 = Solution()
            offspring2 = Solution()

            if np.random.rand() < CrossRate:
                RandInt = np.random.randint(len(J))
                first_part = [j for j in range(RandInt)]
            else:
                first_part = [j for j in J]
            offspring1.X = {j: parent1.X[j] if j in first_part else parent2.X[j] for j in J}
            offspring2.X = {j: parent2.X[j] if j in first_part else parent1.X[j] for j in J}

            if np.random.rand() < CrossRate:
                RandInt = np.random.randint(len(J))
                first_part = [j for j in range(RandInt)]
            else:
                first_part = [j for j in J]
            offspring1.Tpl = {c: parent1.Tpl[c] if c in first_part else parent2.Tpl[c] for c in C}
            offspring2.Tpl = {c: parent2.Tpl[c] if c in first_part else parent1.Tpl[c] for c in C}
            # offspring1 
            openJ = [j for j in J if offspring1.X[j] > 0]
            if not openJ:
                num_openJ = np.random.randint(1, len(J))
                openJ = np.random.choice(J, num_openJ)
            assign_n_ij = {i: np.random.choice(openJ, 1) for i in I}
            offspring1.Yn = {(i, j): 1 if j in assign_n_ij[i] else 0 for i in I for j in J}

            assign_r_ij = {i: np.random.choice(openJ, 1) for i in I}
            offspring1.Yr = {(i, j): 1 if j in assign_r_ij[i] else 0 for i in I for j in J}

            openC = [c for c in C if offspring1.Tpl[c] > 0]
            if not openC:
                num_openC = np.random.randint(1, len(C))
                openC = np.random.choice(C, num_openC)
            assign_ic = {i: np.random.choice(openC, 1) for i in I}
            offspring1.Tpu = {(i, c): 1 if c in assign_ic[i] else 0 for i in I for c in C}

            # offspring2
            openJ = [j for j in J if offspring2.X[j] > 0]
            if not openJ:
                num_openJ = np.random.randint(1, len(J))
                openJ = np.random.choice(J, num_openJ)
            assign_n_ij = {i: np.random.choice(openJ, 1) for i in I}
            offspring2.Yn = {(i, j): 1 if j in assign_n_ij[i] else 0 for i in I for j in J}

            assign_r_ij = {i: np.random.choice(openJ, 1) for i in I}
            offspring2.Yr = {(i, j): 1 if j in assign_r_ij[i] else 0 for i in I for j in J}

            openC = [c for c in C if offspring2.Tpl[c] > 0]
            if not openC:
                num_openC = np.random.randint(1, len(C))
                openC = np.random.choice(C, num_openC)
            assign_ic = {i: np.random.choice(openC, 1) for i in I}
            offspring2.Tpu = {(i, c): 1 if c in assign_ic[i] else 0 for i in I for c in C}

            # positive variables offspring1 
            offspring1.pn = {i: max(np.random.uniform((Tvcr[j] + Tfcr[j] + Prwr + Pcr) * offspring1.Yr[i, j], 1 / Landa)
                                    for j in J) if np.random.rand() < CrossRate else parent1.pn[i]
                             for i in I}

            offspring1.pr = {i: offspring1.pn[i] - pd[i] * offspring1.pn[i] for i in I}

            offspring1.vu = {(i, c): np.random.uniform(svu[i], min(offspring1.pr[i], Rp[i, c] - Trcu[i, c])) for i in I
                             for c in C}

            offspring1.C1 = {j: np.sqrt(sum((tn[j] + Ln[j]) * (Sigman1[i] ** 2) * offspring1.Yn[i, j] * (mn[i] ** 2) * (
                    (1 - (Landa * offspring1.pn[i])) ** 2) * ((1 - TainU[i]) ** 2) for i in I) + sum((tn[j] + Ln[j]) * (
                    Sigman2[i] ** 2) * offspring1.Yn[i, j] for i in I)) for j in J}

            offspring1.C2 = {j: np.sqrt(sum((tr[j] + Lr[j]) * (Sigmar1[i] ** 2) * offspring1.Yr[i, j] * (mr[i] ** 2) * (
                    (1 - (Landa * offspring1.pr[i])) ** 2) for i in I) + sum(
                (tr[j] + Lr[j]) * (Sigmar1[i] ** 2) * offspring1.Yr[i, j] * (
                        mn[i] ** 2) * ((1 - (Landa * offspring1.pn[i])) ** 2) * (TainU[i] ** 2) for i in I) + sum(
                (tr[j] + Lr[j]) * (
                        Sigmar1[i] ** 2) * offspring1.Yr[i, j] * 2 * mr[i] * mn[i] * (
                        1 - (Landa * offspring1.pn[i])) * (
                        1 - (
                        Landa * offspring1.pr[i])) * TainU[i] for i in I) + sum(
                (tr[j] + Lr[j]) * (Sigmar2[i] ** 2) * offspring1.Yr[i, j] for i in I)) for j in J}
            # positive variables offspring2
            offspring2.pn = {i: max(np.random.uniform((Tvcr[j] + Tfcr[j] + Prwr + Pcr) * offspring2.Yr[i, j], 1 / Landa)
                                    for j in J) if np.random.rand() < CrossRate else parent2.pn[i]
                             for i in I}

            offspring2.pr = {i: offspring2.pn[i] - pd[i] * offspring2.pn[i] for i in I}

            offspring2.vu = {(i, c): np.random.uniform(svu[i], min(offspring2.pr[i], Rp[i, c] - Trcu[i, c])) for i in I
                             for c in C}

            offspring2.C1 = {j: np.sqrt(sum((tn[j] + Ln[j]) * (Sigman1[i] ** 2) * offspring2.Yn[i, j] * (mn[i] ** 2) * (
                    (1 - (Landa * offspring2.pn[i])) ** 2) * ((1 - TainU[i]) ** 2) for i in I) + sum((tn[j] + Ln[j]) * (
                    Sigman2[i] ** 2) * offspring2.Yn[i, j] for i in I)) for j in J}

            offspring2.C2 = {j: np.sqrt(sum((tr[j] + Lr[j]) * (Sigmar1[i] ** 2) * offspring2.Yr[i, j] * (mr[i] ** 2) * (
                    (1 - (Landa * offspring2.pr[i])) ** 2) for i in I) + sum(
                (tr[j] + Lr[j]) * (Sigmar1[i] ** 2) * offspring2.Yr[i, j] * (
                        mn[i] ** 2) * ((1 - (Landa * offspring2.pn[i])) ** 2) * (TainU[i] ** 2) for i in I) + sum(
                (tr[j] + Lr[j]) * (
                        Sigmar1[i] ** 2) * offspring2.Yr[i, j] * 2 * mr[i] * mn[i] * (
                        1 - (Landa * offspring2.pn[i])) * (
                        1 - (
                        Landa * offspring2.pr[i])) * TainU[i] for i in I) + sum(
                (tr[j] + Lr[j]) * (Sigmar2[i] ** 2) * offspring2.Yr[i, j] for i in I)) for j in J}
            TotalOffspring.append(offspring1)
            TotalOffspring.append(offspring2)

        return TotalOffspring

    def ParetoFrontiers(self, Sols):

        nPop = len(Sols)
        SolList = [i for i in range(nPop)]
        AllParetos = []

        while (len(SolList) > 0):
            Pareto = []
            Dominate = {(i, j): 0 for i in SolList for j in SolList}

            for i1 in range(len(SolList) - 1):
                for j1 in range(i1 + 1, len(SolList)):
                    i = SolList[i1]
                    j = SolList[j1]
                    if Sols[i].obj1 > Sols[j].obj1 and Sols[i].obj2 < Sols[j].obj2:
                        Dominate[i, j] = 1
                    if Sols[j].obj1 > Sols[i].obj1 and Sols[j].obj2 < Sols[i].obj2:
                        Dominate[j, i] = 1

            SumDom = {j: sum(Dominate[i, j] for i in SolList) for j in SolList}
            for j in SumDom.keys():
                if SumDom[j] < 1:
                    Pareto.append(j)
                    SolList.remove(j)
            AllParetos.append(Pareto)

        return AllParetos

    def FitnessAssignment(self, Sols, k):
        import numpy as np
        ParetoInd = self.ParetoFrontiers(Sols)

        delta = {}
        for i in range(len(Sols)):
            Distances = {j: np.sqrt((Sols[i].obj1 - Sols[j].obj1) ** 2 + (Sols[i].obj2 - Sols[j].obj2) ** 2) for j
                         in range(len(Sols))}
            SortedInd = sorted(Distances, key=Distances.get)
            SortedDist = [Distances[i] for i in SortedInd[:k]]
            delta[i] = sum(SortedDist)

        Size = {}
        for ind in range(1, len(ParetoInd)):
            Size[ind] = len(ParetoInd[ind])
        R = {}
        for ind in range(len(ParetoInd)):
            pareto = ParetoInd[ind]
            for i in pareto:
                R[i] = sum(Size[j] for j in range(ind + 1, len(ParetoInd)))
                Sols[i].F = R[i] + 1 / (delta[i] + 2)

    def EnvironmentalSelection(self, Sols, N_):

        F = {sol: -sol.F for sol in Sols}
        SortedF = sorted(F, key=F.get)

        Sols = SortedF[:self.npop]
        return SortedF[:N_]

    def MatingSelection(self, Solutions):
        import numpy as np
        Sols = [sol.JobAssign for sol in Solutions]
        for n in range(2):
            ind1 = np.random.choice(len(Sols), 1, replace=False).tolist()[0]
            ind2 = np.random.choice(len(Sols), 1, replace=False).tolist()[0]

            offspring1 = Solution()
            offspring2 = Solution()

            Sol1seq = Sols[ind1]
            Sol2seq = Sols[ind2]

            RandInt = np.random.randint(len(Sol1seq))

            if np.random.rand() < .1:

                offspring1.JobAssign = Sol1seq[:RandInt]
                offspring1.JobAssign.extend(Sol2seq[RandInt:])

                offspring2.JobAssign = Sol2seq[:RandInt]
                offspring2.JobAssign.extend(Sol1seq[RandInt:])
            else:
                offspring1.JobAssign = Sol1seq.copy()
                offspring2.JobAssign = Sol2seq.copy()

        return Solutions

    def Variation(self, Solutions, nbOffSpring, CrossRate, MuteRate, data):

        NewSolutions = self.CrossOver(Solutions, nbOffSpring, CrossRate, data)

        NewSolutions = self.Mutation(NewSolutions, MuteRate, data)

        return NewSolutions


def PrintEndTime(Sol):
    print(Sol.EndStageTime)
