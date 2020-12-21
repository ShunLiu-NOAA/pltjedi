import numpy as np
import sys
import statistics
import math
import matplotlib.pyplot as plt
from netCDF4 import Dataset

#from datetime import datetime
#import matplotlib.colors as colors
#import cartopy.crs as ccrs
#import cartopy.feature as cfeature

def plt_ufo_t(filename,OBSTYPE):

   thisobstype=OBSTYPE
   gsihofXBc='specific_humidity@GsiHofXBc'
   gsihofX  ='specific_humidity@GsiHofX'
   ufohofX  ='specific_humidity@hofx'
   f=Dataset(filename, mode='r')
   gsi_observer_withqc=f.variables[gsihofXBc][:]
   gsi_observer_noqc  =f.variables[gsihofX][:]
   ufo                =f.variables[ufohofX][:]
   geopotential_height=f.variables['geopotential_height@MetaData'][:]
#  gsi_observer_withqc=f.variables['radial_velocity@GsiHofXBc'][:]
   f.close()

   plt.rcParams.update({'font.size': 18})
#  plt.rcParams.update({'line.linewidth': 8})
#=========================
   fig = plt.figure(figsize=(8.0,7.5))
   ax=fig.add_subplot(111)


   #plt.plot(gsi_observer,ufo, color='black',label="obs" , linewidth=2, marker='o')
#  plt.scatter(gsi_observer_withqc,ufo, color='blue',label="rw", marker='o', s=3)
   plt.scatter(gsi_observer_noqc,ufo, color='r',label="tsen", marker='o', s=3)

   #box = ax.get_position()
   #ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
#  ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

   plt.xlabel('gsi')
   plt.ylabel('ufo')
   plt.title(thisobstype+':gsi and ufo hofx scatter')
   figname='ufo_'+thisobstype+'_stage1.png'
   plt.savefig(figname,bbox_inches='tight',dpi=100)
#=========================

#=========================
   diff=gsi_observer_noqc
   diff=diff - ufo
   print(diff)

   rms=float(0)
   for x in diff:
      rms=rms+x*x
   rms=math.sqrt(rms/len(diff))
   print("rms=",rms)

   diff=diff*1000.0

   fig1 = plt.figure(figsize=(8.0,7.5))
   ax=fig1.add_subplot(111)
   plt.hist(diff,bins=50)
#  plt.xlim([-0.15,0.15])
   plt.xlabel('(gsi-ufo)*1000')
   plt.title(thisobstype+':gsi and ufo diff histogram')
   figname='ufo_'+thisobstype+'_stage1_hist.png'
   plt.savefig(figname,bbox_inches='tight',dpi=100)
#=========================

#=========================
   fig2 = plt.figure(figsize=(8.0,7.5))
   ax=fig2.add_subplot(111)
   plt.scatter(diff,geopotential_height, color='b',label="rw", marker='o', s=3)
#  plt.xlim([-0.15,0.15])
   plt.xlabel('(gsi-ufo)*1000')
   plt.ylabel('geop-height')
   plt.title(thisobstype+':gsi-ufo diff in vertical')
   figname='ufo_'+thisobstype+'_stage1_vdiff_scatter.png'
   plt.savefig(figname,bbox_inches='tight',dpi=100)
#=========================


#=====================================================================
#=====================================================================
if __name__ == '__main__':

   print("start ploting")

   #call subroutine plt_radar_ref
   print("ploting gsi hofx v.s. ufo hofx")
   fileame=sys.argv[1]
   OBSTYPE=sys.argv[2]
   plt_ufo_t(fileame,OBSTYPE)



#  print(statistics.stdev(diff))
#plt.xticks(np.arange(0,25,3))
#ymin1=imos[0:8].min()
#ymin2=gfs.min()
#ymin=min(ymin1,ymin2)
#ymin=ymin-1.0
#print ymin
#ymax1=imos[0:8].max()
#ymax2=gfs.max()
#ymax=max(ymax1,ymax2)
#ymax=ymax+1.0
#plt.ylim([ymin,ymax])
#plt.xlim([-25,25])
#  plt.xticks(fontsize=15)
#  plt.yticks(fontsize=15)
