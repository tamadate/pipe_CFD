import matplotlib.pyplot as plt
import numpy as np

##  To organize figure style
def pltNormal():
    plt.rcParams['ytick.direction'] = 'in'
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['figure.subplot.bottom'] = 0.15
    plt.rcParams['figure.subplot.left'] = 0.2
    plt.rcParams["font.size"]=10

def axNormal(ax):
    ax.xaxis.set_ticks_position('both')
    ax.yaxis.set_ticks_position('both')
    ax.tick_params(axis='x')
    ax.tick_params(axis='y')

def Cc(dp):
	lamda=67.0e-9
	ap=dp/2.0
	return 1+lamda/ap*(1.257+0.4*np.exp(-1.1*ap/lamda))

pltNormal()
fig, axs = plt.subplots(1,1,figsize=(5,5))
axNormal(axs)

#for i in np.arange(1000):
#    data=np.loadtxt("../../../../pipe/result/position."+str(i))
#    axs.plot(data.T[0],data.T[2])
#plt.show()

L=0.52
Dpipe=12.7e-3
Uave=11.84
rho=1.2
mu=1.8e-5
nu=mu/rho
Re=rho*Uave*Dpipe/mu
fanning=0.316/4.0/Re**0.25
Ustar=((0.5*fanning)**0.5)*Uave
rhop=1000
A=np.pi*Dpipe*Dpipe/4.0
Q=Uave*A
S=np.pi*Dpipe*L
particleSizes=[1,2,5,10]

x=[]
y=[]
for dp in particleSizes:
    loc="../../../../pipe/"+str(dp)+"um/"
    data=np.loadtxt(loc+"finalPosition.dat")
    initialVelocity=np.loadtxt(loc+"initialVelocity.dat")

    Dp=1e-6*dp
    tau=rhop*Dp*Dp*Cc(Dp)/18.0/mu
    taup=tau*Ustar*Ustar/nu
    Iout=0
    Idep=0
    for i in np.arange(np.size(data.T[0])):
        if(data[i][4]==1):
            Iout+=initialVelocity[i][2]
        if(data[i][4]==2):
            Idep+=initialVelocity[i][2]
    P=Iout/(Iout+Idep)

    Vp=Q/S*np.log(1/P)/Ustar
    x=np.append(x,taup)
    y=np.append(y,Vp)
    print(str(taup)+" "+str(Vp))

axs.set_xscale("log")
axs.set_yscale("log")
axs.scatter(x,y)
plt.show()
