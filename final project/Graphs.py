import numpy as np
import matplotlib.pyplot as plt
from Setup import *






def orbits2D():
    fig=plt.figure(figsize=(3.5,2.6),dpi=200)
    ax=fig.add_subplot(1,1,1)
    ax.set_xlabel(r'$x$ (m)')
    ax.set_ylabel(r'$y$ (m)')
    for name in xpos:
        x = np.array(xpos[name]) /149597870700  # from NASA
        y= np.array(ypos[name]) /149597870700
   
        ax.plot(x, y, label = name, lw=0.4)

    ax.xaxis.set_ticks(np.arange(-1.0, 1.01, 0.5))
    ax.yaxis.set_ticks(np.arange(-1.0, 1.01, 0.5))
    ax.legend()
    fig.tight_layout()
    plt.show()
    

def EnergyCons():
    fig=plt.figure(figsize=(3.5,2.6),dpi=200)
    ax=fig.add_subplot(1,1,1)
    ax.set_xlabel(r'$t$ (s)')
    ax.set_ylabel(r'$E$ (J)')

    ax.plot(timeLog, totalEnergy, label="energy", lw=0.4)

    ax.legend()
    fig.tight_layout()
    plt.show()
    

def LinearMomCons():
    fig=plt.figure(dpi=200)
    ax=fig.add_subplot(1,1,1)
    ax.set_xlabel(r'$t$ (s)')
    ax.set_ylabel(r'$ (kg ms^{-1})$')
    
   # linearMom = np.array(linearMom)
    ax.plot(timeLog, linearMom, label="CLM", lw=1)

    ax.legend()
    fig.tight_layout()
    plt.show()

    

def AngMomCons():
    fig=plt.figure(dpi=200)
    ax=fig.add_subplot(1,1,1)
    ax.set_xlabel(r'$t$ (s)')
    ax.set_ylabel(r'$kgms^-2$ (J)')
    
    ax.plot(timeLog, angularMom, label="CAM", lw=0.4)

    ax.legend()
    fig.tight_layout()
    plt.show()
    

def orbits3D():
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    for name in xpos:
        
        # change units to astronomical units
        xx = np.array(xpos[name]) /149597870700
        yy= np.array(ypos[name]) /149597870700
        zz = np.array(zpos[name]) /149597870700
        
        
        ax.plot(xx, yy, zz, label = name, lw=0.4)
        
    ax.set_xlabel(r'$x$ (au)')
    ax.set_ylabel(r'$y$ (au)')
    ax.set_zlabel(r'$z$ (au)')

   # ax.xaxis.set_ticks(np.arange(-1.0, 1.01, 0.5))
   # ax.yaxis.set_ticks(np.arange(-1.0, 1.01, 0.5))
   # ax.zaxis.set_ticks(np.arange(-1.0, 1.01, 0.5))
    ax.xaxis.set_ticks(np.arange(-35.0, 35.0, 10))
    ax.yaxis.set_ticks(np.arange(-35.0, 35.0, 10))
    ax.zaxis.set_ticks(np.arange(-35.0, 35.0, 10))
    ax.legend()
    plt.show()


