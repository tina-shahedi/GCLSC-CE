$inlineCom [ ]
$eolCom //
$title example model definitions
$funcLibin stolib stodclib
Function cdfnorm  /stolib.cdfnormal/
         icdfnorm  /stolib.icdfnormal/;
*********************** GCLSCND ************************************************

*-*-*-*-*-*-*-*-*-*-*-* Set *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
sets
   j index for distribution center /1*5/
   i index for customer point /1*5/
   c index for collection center /1*5/
   h objective function  /obj01,obj02/;
;
*-*-*-*-*-*-*-*-*-*-*-* scalar*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
scalars
   AvPni
   AvPri
   AvVuic
   YYn
   YYr
   TTpu
   TTPl
   XXj
;
scalars
   Hn   holding cost new tire in year
   Hr   holding cost retread tire in year
   Hu   holding cost used tire in year ;

   Hn=uniform(2,12);
   Hr=uniform(2,12);
   Hu=uniform(1,10);

scalars
   Prwn  purchase cost raw material new
   Prwr  purchase cost raw material retread;

   Prwn=uniform(20,30);
   Prwr=uniform(10,20);
scalars
   Pcn  production cost new tire  /40/
   Pcr  production cost retread tire /20/
;


scalars
   XX    number of day in year /360/
   Beta  factor related to transportation cost /0.1/
   teta  factor related to holding cost /0.1/
   alpha percent of retreadable returned tire /0.2/
   Gamma fixed value for cannibalization effect in linear model /0.5/
   Landa coeficient of nirmalized the price /0.01/
;
*-*-*-*-*-*-*-*-*-*-*-* parameters *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
parameters
    eM(j)     distance between manufacturing-remanufac & distribution center j
    eD(i,j)   distance between distribution center j & customer point i
    eS(i,c)   distance between customer point i & collection center c
    eC(c)     distance between collection center c & manufacturing-remanufac
    eR(c)     distance between collection center c & Recycling center
;

 loop(j,
    eM(j)=uniform(5,7);
    );

 loop((i,j),
    eD(i,j)=uniform(1,5);
    );

  loop((i,c),
    eS(i,c)=uniform(3,5);
    );

 loop(c,
    eC(c)=uniform(1,5);
    eR(c)=uniform(2,3);
    );
parameter
 dir(h) 'direction of objective function' /obj01 +1,obj02 -1/
 Results(*)
 ;
parameters
   mn(i)  market potenciel scale of new tire in customer point i
   mr(i)  market potenciel scale of retread tire in customer point i
;
 loop((i),
    mn(i)=uniform(20,30);
    mr(i)=0.85*mn(i);
    );
parameters
   svu(i)       salvage value of used tire
;
    loop((i),
    svu(i)=uniform(10,15);
    );

parameters
   Fd(j)   fixed constructing cost distribution center j
   An(j)   fixed ordering cost new tire in distribution center j
   Ar(j)   fixed ordering cost retread tire in distribution center j
   Pain(j) backorder cost new in distribution center j
   Pair(j) backorder cost retread in distribution center j
;
 loop((j),
    Fd(j)=uniform(200,300);
    An(j)=uniform(1,2);
    Ar(j)=uniform(1,2);
    Pain(j)=3*Hn;
    Pair(j)=3*Hr;
    );

*-*-*-*-*-*-*-*-*-*-*-*-* Transportation-Cost *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
parameters
    Tvcn(j) Transportation variable cost of new tire from m-rem to dis ceneter j
    Tvcr(j) Transportation variable cost of retread tire from m-rem to dis ceneter j
    Tfcn(j) Transportation fixed cost of new tire from m-rem to dis ceneter j
    Tfcr(j) Transportation fixed cost of retread tire from m-rem to dis ceneter j
;

 loop((j),
    Tvcn(j)=uniform(1,2);
    Tvcr(j)=uniform(1,2);
    Tfcn(j)=uniform(1,2);
    Tfcr(j)=uniform(1,2);
    );

parameters
    Tdcn(i,j)  Transportation cost of new tire between customer i & dis center j (depend on Euclidean distance)
    Tdcr(i,j)  Transportation cost of retread tire between customer i & dis center j (depend on Euclidean distance)
;
 loop((i,j),
    Tdcn(i,j)=uniform(5,6);
    Tdcr(i,j)=uniform(5,6);
    );
parameters
    Trcu(i,c)  transportation cost used tire from customer point i to collection center c
;

   loop((i,c),
    Trcu(i,c)=uniform(10,20);
);

parameters
    Trmu(c)  transportation cost used tire from c to m-rem
    Tru(c)   transportation cost used tire from c to recycle center
;

   loop((c),
    Trmu(c)=uniform(0.1,1);
    Tru(c)=uniform(0.1,1);
);

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
parameters
    Ln(j)     lead time for new tire in dis center j
    Lr(j)     lead time for retread tire in dis center j
;

   loop((j),
    Ln(j)=uniform(5,10);
    Lr(j)=uniform(5,10);
);
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
parameters
    Sigman1(i)    standard deviation of nue i  for new tire
    Sigmar1(i)    standard deviation of nue i  for retread tire
    Sigman2(i)    standard deviation of epsilon i  for new tire
    Sigmar2(i)    standard deviation of epsilon i  for retread tire
;
   loop((i),
    Sigman1(i)=0.01;
    Sigmar1(i)=0.01;
    Sigman2(i)=0.01;
    Sigmar2(i)=0.01;
);
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
parameters
    tn(j)   inventory review interval in dis center j for new tire
    tr(j)   inventory review interval in dis center j for retread tire
;
   loop((j),
    tn(j)=7;
    tr(j)=7;
);
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
parameters
    Tu(c)    inventory review interval in collection center c for used tire
    Fc(c)    fixed cost of constructing collection center c
;
   loop((c),
    Tu(c)=7;
    Fc(c)=uniform(100,300)
);

parameters

    Bu(i,c)  quantity of returned used tire from customer point i to collection cenetr c
;

   loop((i,c),
    Bu(i,c)=round(uniform(10,20));
);

*-*-*-*-*-*-*-*-*-*-*-*-*-Selling Price-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
parameters
    Rs(i,c) Selling price used tire returned from customer point i by collection center c to m-rem center
    Rp(i,c) Selling price used tire returned from customer point i by collection center c to recycle center
;

   loop((i,c),
    Rp(i,c)=uniform((svu(i)+Trcu(i,c)),(svu(i)+Trcu(i,c))*1.2);
    Rs(i,c)=uniform(Rp(i,c),(Rp(i,c))*1.3);
);

*-*-*-*-*-*-*-*-*-*-*-*-*-environmental Impact-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
parameters
    eI(j)    environmental Impact transporting to dis center j
    eIs(j)   environmental Impact establish dis center j
;

   loop((j),
    eI(j)=uniform(1,3);
    eIs(j)=uniform(10,20);
);

parameters
    eId(i,j)   environmental Impact transporting from dis center j to customer point i
;

   loop((i,j),
    eId(i,j)=uniform(1,3);
);

parameters
    eIc(i,c)   environmental Impact transporting from customer point i to collection center c
;

   loop((i,c),
     eIc(i,c)=uniform(3,5);
);

parameters
    eIm(c)   environmental Impact transporting from collection center c to m-rem center
    eIr(c)   environmental Impact transporting from collection center c to recycle center
    eIe(c)  environmental Impact establish collection center c
;
   loop((c),
         eIm(c)=uniform(1,2);
         eIr(c)=uniform(1,2);
         eIe(c)=uniform(2,3);
);
*-*-*-*-*-*-*-*-*-*-*-* normal distribution *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

parameters
    sln(j)    service level new tire
    slr(j)    service level retread tire
;
loop((j),
    sln(j)=1-((teta*Hn*tn(j))/(Pain(j)*XX));
    slr(j)=1-((teta*Hr*tr(j))/(Pair(j)*XX));
);

parameter
    Ztn(j)          'Value of the accumulated standard normal distribution such that P(Z<Ztn(j))=sln(j)'
    ;
    loop((j),
    Ztn(j)=icdfnorm(sln(j),0,1);
    );

parameter
    Ztr(j)          'Value of the accumulated standard normal distribution such that P(Z<Ztr(j))=slr(j)'
    ;
    loop((j),
    Ztr(j)=icdfnorm(slr(j),0,1);
    );
parameter
    phiZtn(j)       standard normal cumulative distribution function
    ;
    loop((j),
    phiZtn(j)=cdfnorm(Ztn(j),0,1);
    );

parameter
    phiZtr(j)       standard normal cumulative distribution function
    ;
    loop((j),
    phiZtr(j)=cdfnorm(Ztr(j),0,1);
    );
*-*-*-*-*-*-*-*-*-*-*-* Variables *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

       variables
          Z(H)
       positive variables
          Z1
          Z2
          C1(j)            auxilary positive variable 1
          C2(j)            auxilary positive variable 2
          pn(i)            price new tire in customer point i
          pr(i)            price retread tire in customer point i
          vu(i,c)          price used tire in customer point i purchase by collection center c
       Binary variables
          X(j)             if establish dis j equal 1- other wise 0
          Tpu(i,c)         if used tire of customer point i selling to TPL c equal 1- other wise 0
          Tpl(c)           if establish TPL c equal 1- other wise 0
          Yn(i,j)          if meet new tire demand of customer point i by dis center j equal 1- other wise 0
          Yr(i,j)          if meet retread tire demand of customer point i by dis center j equal 1- other wise 0
       Equations
          obj1
          obj11
          obj2
          obj21
          eq44(j)
          eq45(j)
          eq46(i,j)
          eq47(i,j)
          eq48(i)
          eq49(i)
          eq50(i,j)
          eq51(i,j)
          eq52(i)
          eq53(i)
          eq54(i)
          eq55(i)
          eq56(i)
          eqq56(i)
          eq57(i,c)
          eq58(i,c)
          eqq58(i,c)
          eq59(i)
          eq60(i,c)
          eq61(i)
;
*-*-*-*-*-*-*-*-*-*-*-* Objective functions *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
obj1(H)$(ord(H)=1)..  Z(H)=e=Z1  ;
obj11    ..    Z1=e=sum((i),(pn(i)-Pcn-Prwn)*XX*mn(i)*(1-((Landa/(1-Gamma))*pn(i))+(((Landa*Gamma)/(1-Gamma))*pr(i))))-
                   sum((i,j),Beta*XX*Tdcn(i,j)*eD(i,j)*Yn(i,j)*mn(i)*(1-((Landa/(1-Gamma))*pn(i))+(((Landa*Gamma)/(1-Gamma))*pr(i))))-
                   sum(j,An(j)*(XX/tn(j))*X(j))-sum(j,Beta*Tfcn(j)*(XX/tn(j))*X(j))-
                   sum((i,j),Beta*XX*Tvcn(j)*eM(j)*Yn(i,j)*mn(i)*(1-((Landa/(1-Gamma))*pn(i))+(((Landa*Gamma)/(1-Gamma))*pr(i))))-
                   sum((i,j),0.5*teta*Hn*tn(j)*Yn(i,j)*mn(i)*(1-((Landa/(1-Gamma))*pn(i))+(((Landa*Gamma)/(1-Gamma))*pr(i))))-
                   sum(j,((Pain(j)*XX)/tn(j))*phiztn(j)*c1(j))+
                   sum((i),(pr(i)-Pcr-Prwr)*XX*mr(i)*(1-((Landa/(1-Gamma))*pr(i))+(((Landa*Gamma)/(1-Gamma))*pn(i))))-
                   sum((i,j),Beta*XX*Tdcr(i,j)*eD(i,j)*Yr(i,j)*mr(i)*(1-((Landa/(1-Gamma))*pr(i))+(((Landa*Gamma)/(1-Gamma))*pn(i))))-
                   sum(j,Ar(j)*(XX/tr(j))*X(j))-sum(j,Beta*Tfcr(j)*(XX/tr(j))*X(j))-
                   sum((i,j),Beta*XX*Tvcr(j)*eM(j)*Yr(i,j)*mr(i)*(1-((Landa/(1-Gamma))*pr(i))+(((Landa*Gamma)/(1-Gamma))*pn(i))))-
                   sum((i,j),0.5*teta*Hr*tr(j)*Yr(i,j)*mr(i)*(1-((Landa/(1-Gamma))*pr(i))+(((Landa*Gamma)/(1-Gamma))*pn(i))))-
                   sum(j,((Pair(j)*XX)/tr(j))*phiztr(j)*C2(j))-
                   sum(j,Fd(j)*X(j))+sum((i,c),Rs(i,c)*alpha*Bu(i,c)*Tpu(i,c)*XX)+
                   sum((i,c),Rp(i,c)*(1-alpha)*Bu(i,c)*Tpu(i,c)*XX)-
                   sum((i,c),vu(i,c)*Bu(i,c)*XX*Tpu(i,c))-
                   sum(c,Fc(c)*Tpl(c))-sum((i,c),0.5*teta*Hu*Bu(i,c)*Tpu(i,c)*Tu(c))-
                   sum((i,c),Beta*Trcu(i,c)*eS(i,c)*Bu(i,c)*XX*Tpu(i,c))-
                   sum((i,c),Beta*Trmu(c)*eC(c)*alpha*Bu(i,c)*Tpl(c)*XX)-
                   sum((i,c),Beta*Tru(c)*eR(c)*(1-alpha)*Bu(i,c)*Tpl(c)*XX);
obj2(H)$(ord(H)=2)..  Z(H)=e=Z2  ;
obj21    ..   Z2=e=sum((i,j),eI(j)*eM(j)*XX*Yn(i,j)*mn(i)*(1-((Landa/(1-Gamma))*pn(i))+(((Landa*Gamma)/(1-Gamma))*pr(i))))+
                  sum((i,j),eI(j)*eM(j)*XX*Yr(i,j)*mr(i)*(1-((Landa/(1-Gamma))*pr(i))+(((Landa*Gamma)/(1-Gamma))*pn(i))))+
                  sum((i,j),eId(i,j)*eD(i,j)*XX*Yr(i,j)*mr(i)*(1-((Landa/(1-Gamma))*pr(i))+(((Landa*Gamma)/(1-Gamma))*pn(i))))+
                  sum((i,j),eId(i,j)*eD(i,j)*XX*Yn(i,j)*mn(i)*(1-((Landa/(1-Gamma))*pn(i))+(((Landa*Gamma)/(1-Gamma))*pr(i))))+
                  sum(j,eIs(j)*X(j))+sum(c,eIe(c)*Tpl(c))+sum((i,c),eIc(i,c)*eS(i,c)*Bu(i,c)*XX*Tpu(i,c))+
                  sum((i,c),eIm(c)*eC(c)*alpha*Bu(i,c)*Tpl(c)*XX)+
                  sum((i,c),eIr(c)*eR(c)*(1-alpha)*Bu(i,c)*Tpl(c)*XX)

;


*-*-*-*-*-*-*-*-*-*-*-* Constraints *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
eq44(j)..       (C1(j)**2)=g=sum(i,(tn(j)+Ln(j))*(Sigman1(i)**2)*Yn(i,j)*(mn(i)**2)*(((((1-Gamma-Landa)/(1-Gamma))*pn(i))**2)+((((Landa*Gamma)/(1-Gamma))*pr(i))**2)+(2*pn(i)*pr(i)*(((Landa*Gamma)-(Landa*(Gamma**2))-((Landa**2)*Gamma))/((1-Gamma)**2)))))+sum(i,(tn(j)+Ln(j))*(Sigman2(i)**2)*Yn(i,j));
eq45(j)..       (C2(j)**2)=g=sum(i,(tr(j)+Lr(j))*(Sigmar1(i)**2)*Yr(i,j)*(mr(i)**2)*(((((1-Gamma-Landa)/(1-Gamma))*pr(i))**2)+((((Landa*Gamma)/(1-Gamma))*pn(i))**2)+(2*pr(i)*pn(i)*(((Landa*Gamma)-(Landa*(Gamma**2))-((Landa**2)*Gamma))/((1-Gamma)**2)))))+sum(i,(tr(j)+Lr(j))*(Sigmar2(i)**2)*Yr(i,j));
eq46(i,j)..      X(j)=g=Yn(i,j);
eq47(i,j)..      X(j)=g=Yr(i,j);
eq48(i)..        sum(j,Yn(i,j))=e=1;
eq49(i)..        sum(j,Yr(i,j))=e=1;
eq50(i,j)..      pn(i)=g=(Tvcn(j)+Tfcn(j)+Prwn+Pcn)*Yn(i,j);
eq51(i,j)..      pr(i)=g=(Tvcr(j)+Tfcr(j)+Prwr+Pcr)*Yr(i,j);
eq52(i)..        pn(i)=l=((1-Gamma)/Landa)+Gamma*pr(i);
eq53(i)..        pr(i)=l=((1-Gamma)/Landa)+Gamma*pn(i);
eq54(i)..        pn(i)=g=Gamma*pr(i);
eq55(i)..        pr(i)=g=Gamma*pn(i);
eq56(i)..        pr(i)=l=pn(i);
eqq56(i)..       pn(i)=l=(1/Landa);
eq57(i,c)..      vu(i,c)=l=pr(i);
eq58(i,c)..      vu(i,c)=l=Rp(i,c)-Trcu(i,c);
eqq58(i,c)..     svu(i)=l=vu(i,c);
eq59(i)..        sum(c,Tpu(i,c))=e=1;
eq60(i,c)..      Tpu(i,c)=l=Tpl(c);
eq61(i)..        mn(i)*(1-((Landa/(1-Gamma))*pn(i))+(((Landa*Gamma)/(1-Gamma))*pr(i)))=g=5;


model example /all/;

$sTitle eps-constraint Method
Set
   k1(h)  'the first element of k'
   km1(h) 'all but the first elements of k'
   kk(h)  'active objective function in constraint allobj';

k1(h)$(ord(h) = 1) = yes;
km1(h)  = yes;
km1(k1) =  no;

Parameter
   rhs(h)    'right hand side of the constrained obj functions in eps-constraint'
   maxobj(h) 'maximum value from the payoff table'
   minobj(h) 'minimum value from the payoff table'
   numk(h)   'ordinal value of k starting with 1';
Scalar
   iter         'total number of iterations'
   infeas       'total number of infeasibilities'
   elapsed_time 'elapsed time for payoff and e-sonstraint'
   start        'start time'
   finish       'finish time';

Variable
   a_objval 'auxiliary variable for the objective function'
   obj      'auxiliary variable during the construction of the payoff table'
   sl(h)    'slack or surplus variables for the eps-constraints'
;

Positive Variable sl;

Equation
   con_obj(h) 'constrained objective functions'
   augm_obj   'augmented objective function to avoid weakly efficient solutions'
   allobj     'all the objective functions in one expression';

con_obj(km1).. z(km1) - dir(km1)*sl(km1) =e= rhs(km1);

* We optimize the first objective function and put the others as constraints
* the second term is for avoiding weakly efficient points

augm_obj..
   a_objval =e= sum(k1,dir(k1)*z(k1))
         + 1e-3*sum(km1,power(10,-(numk(km1) - 1))*sl(km1)/(maxobj(km1) - minobj(km1)));

allobj .. sum(kk, dir(kk)*z(kk))=e= obj ;

Model
   mod_payoff    / example, allobj            /
   mod_epsmethod / example, con_obj, augm_obj /;

Parameter payoff(h,h) 'payoff tables entries';

Alias (h,kp);

option optcr=0,optca=0 ,reslim=35,iterlim=1000, limRow = 0, limCol = 0, solPrint = on, solveLink = %solveLink.LoadLibrary%;

* Generate payoff table applying lexicographic optimization
loop(kp,
   kk(kp) = yes;
   repeat
      option reslim=35;
      option iterlim=1000;
      solve mod_payoff using MINLP maximizing obj;
      payoff(kp,kk) = z.l(kk);
      z.fx(kk) = z.l(kk); // freeze the value of the last objective optimized
      kk(h++1) = kk(h);   // cycle through the objective functions
   until kk(kp);
   kk(kp) = no;
*  release the fixed values of the objective functions for the new iteration
   z.up(h) =  inf;
   z.lo(h) = -inf;
);
if(mod_payoff.modelStat <> %modelStat.Optimal% and
   mod_payoff.modelStat <> %modelStat.Integer Solution%,
   abort 'no optimal solution for mod_payoff');

File fx / proj.txt /;
put  fx ' PAYOFF TABLE'/;
loop(kp,
   loop(h, put payoff(kp,h):12:2);
   put /;
);

minobj(h) = smin(kp,payoff(kp,h));
maxobj(h) = smax(kp,payoff(kp,h));

* gridpoints are calculated as the range (difference between max and min) of
* the 2nd objective function from the payoff table
$if not set gridpoints $set gridpoints 7
Set
   g1         'grid points' / g0*g%gridpoints% /
   grid(h,g1) 'grid';

Parameter
   gridrhs(h,g1) 'RHS of eps-constraint at grid point'
   maxg(h)      'maximum point in grid for objective'
   posg(h)      'grid position of objective'
   firstOffMax  'some counters'
   lastZero     'some counters'
*  numk(k) 'ordinal value of k starting with 1'
   numg(g1)      'ordinal value of g starting with 0'
   step(h)      'step of grid points in objective functions'
   jump(h)      'jumps in the grid points traversing';

lastZero = 1;
loop(km1,
   numk(km1) = lastZero;
   lastZero  = lastZero + 1;
);
numg(g1) = ord(g1) - 1;

grid(km1,g1) = yes; // Here we could define different grid intervals for different objectives
maxg(km1)   = smax(grid(km1,g1), numg(g1));
step(km1)   = (maxobj(km1) - minobj(km1))/maxg(km1);
gridrhs(grid(km1,g1))$(dir(km1) = -1) = maxobj(km1) - numg(g1)/maxg(km1)*(maxobj(km1) - minobj(km1));
gridrhs(grid(km1,g1))$(dir(km1) =  1) = minobj(km1) + numg(g1)/maxg(km1)*(maxobj(km1) - minobj(km1));

put / ' Grid points' /;
loop(g1,
   loop(km1, put gridrhs(km1,g1):12:2);
   put /;
);
put / 'Efficient solutions' /;

* Walk the grid points and take shortcuts if the model becomes infeasible or
* if the calculated slack variables are greater than the step size
posg(km1) = 0;
iter   = 0;
infeas = 0;
start  = jnow;

repeat
   rhs(km1) = sum(grid(km1,g1)$(numg(g1) = posg(km1)), gridrhs(km1,g1));
   option reslim=35;
   option iterlim=1000;
   solve mod_epsmethod maximizing a_objval using MINLP;
   iter = iter + 1;
   if(mod_epsmethod.modelStat<>%modelStat.Optimal% and
      mod_epsmethod.modelStat<>%modelStat.Integer Solution%,
      infeas = infeas + 1; // not optimal is in this case infeasible
      put iter:5:0, '  infeasible' /;
      lastZero = 0;
      loop(km1$(posg(km1)  > 0 and lastZero = 0), lastZero = numk(km1));
      posg(km1)$(numk(km1) <= lastZero) = maxg(km1); // skip all solves for more demanding values of rhs(km1)
   else
      put iter:5:0;
      loop(h, put z.l(h):12:2);
      jump(km1) = 1;
*     find the first off max (obj function that hasn't reach the final grid point).
*     If this obj.fun is k then assign jump for the 1..k-th objective functions
*     The jump is calculated for the innermost objective function (km=1)
      jump(km1)$(numk(km1) = 1) = 1 + floor(sl.L(km1)/step(km1));
      put '    'z1.l,z2.l :12:2;
      loop(km1$(jump(km1)  > 1), put '   jump');
      put /;
   );
*  Proceed forward in the grid
   firstOffMax = 0;
   loop(km1$(posg(km1) < maxg(km1) and firstOffMax = 0),
      posg(km1)   = min((posg(km1) + jump(km1)),maxg(km1));
      firstOffMax = numk(km1);
   );
   posg(km1)$(numk(km1) < firstOffMax) = 0;
   abort$(iter > 1000) 'more than 1000 iterations, something seems to go wrong'
until sum(km1$(posg(km1) = maxg(km1)),1) = card(km1) and firstOffMax = 0;
display payoff;
finish = jnow;
elapsed_time = (finish - start)*60*60*24;

YYn=sum((i,j),Yn.l(i,j));
YYr=sum((i,j),Yr.l(i,j));
TTpu=sum((i,c),Tpu.l(i,c));
TTPl=sum(c,Tpl.l(c));
XXj=sum(j,x.l(j));
AvPni=sum(i,pn.l(i)/YYn);
AvPri=sum(i,pr.l(i)/YYr);
AvVuic=sum((i,c),vu.l(i,c)*Tpu.l(i,c)/TTpu);


   Results('Average new tire price')=AvPni;
   Results('Average retread tire price')=AvPri;
   Results('Average used tire price')=AvVuic;
   Results('total distribute new tire')=YYn;
   Results('total distribute reterad tire')=YYr;
   Results('total PURCHASE CUSTOMER')=TTpu;
   Results('total open DC')=XXj;
   Results('total Collector')=TTPl;

display Results;

execute_unload 'CLSCND.gdx';
put /;
put 'Infeasibilities = ', infeas:5:0 /;
put 'Elapsed time: ',elapsed_time:10:2, ' seconds' /;

execute_unload 'proj.gdx'
