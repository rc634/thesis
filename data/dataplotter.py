import numpy as np
import matplotlib.pyplot as plt
import csv
import re

basedir = 'graze'

dat_file = np.loadtxt(basedir + "/mod_phi_max.dat", unpack=True)

plt.rc('font', size=20) #controls default text size
plt.rc('axes', titlesize=20) #fontsize of the title
plt.rc('axes', labelsize=20) #fontsize of the x and y labels
plt.rc('xtick', labelsize=12) #fontsize of the x tick labels
plt.rc('ytick', labelsize=12) #fontsize of the y tick labels
plt.rc('legend', fontsize=20) #fontsize of the legend


plt.plot(dat_file[0], dat_file[1],color='darkviolet',linewidth=1.2)
plt.title("Global Maximum of Scalar Field")
plt.ylabel(r"$|\varphi|_{\rm max} \cdot m$")
plt.xlabel(r"Evolution Time $t \cdot m$")
plt.xlim([0.,1000.])
plt.show()







dat_file = np.loadtxt(basedir + "/NoetherCharge.dat", unpack=True)
dat_file2 = np.loadtxt("headon/NoetherCharge.dat", unpack=True)

plt.rc('font', size=20) #controls default text size
plt.rc('axes', titlesize=20) #fontsize of the title
plt.rc('axes', labelsize=20) #fontsize of the x and y labels
plt.rc('xtick', labelsize=12) #fontsize of the x tick labels
plt.rc('ytick', labelsize=12) #fontsize of the y tick labels
plt.rc('legend', fontsize=20) #fontsize of the legend


plt.plot(dat_file[0], dat_file[1],color='darkviolet',linewidth=1.2,label='Grazing Collision')
#plt.plot(dat_file2[0], dat_file2[1],color='forestgreen',linewidth=1.2,label='Headon Collision')
plt.title("Late Time Integrated Noether Charge")
plt.ylabel(r"$N$")
plt.xlabel(r"Evolution Time $t \cdot m$")
plt.xlim([550.,1000.])
plt.ylim([0.0144,0.0152])
plt.legend()
plt.show()



dat_file = np.loadtxt(basedir + "/Weyl4_mode_20.dat", unpack=True)
dat_file2 = np.loadtxt(basedir + "/Weyl4_mode_22.dat", unpack=True)

plt.rc('font', size=20) #controls default text size
plt.rc('axes', titlesize=20) #fontsize of the title
plt.rc('axes', labelsize=20) #fontsize of the x and y labels
plt.rc('xtick', labelsize=12) #fontsize of the x tick labels
plt.rc('ytick', labelsize=12) #fontsize of the y tick labels
plt.rc('legend', fontsize=20) #fontsize of the legend


plt.plot(dat_file[0], dat_file[7],color='darkviolet',linewidth=1.2,label='20 Mode')
plt.plot(dat_file2[0], dat_file2[7],color='forestgreen',linewidth=1.2,label='22 Mode')
plt.title("Gravitational Wave Signal")
plt.ylabel(r"$\Psi_4$")
plt.xlabel(r"Evolution Time $t \cdot m$")
plt.xlim([400.,600.])
plt.legend()
#plt.ylim([0.27127,0.27131])
plt.show()


