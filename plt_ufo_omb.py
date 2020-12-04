import numpy as np
import sys
import matplotlib.pyplot as plt
from netCDF4 import Dataset

#from datetime import datetime
#import matplotlib.colors as colors
#import cartopy.crs as ccrs
#import cartopy.feature as cfeature

def plt_ref_vertical(filename):

   f=Dataset(filename, mode='r')
   gsi_observer=f.variables['radial_velocity@GsiHofX'][:]
   ufo=f.variables['radial_velocity@hofx'][:]
   f.close()

   fig = plt.figure(figsize=(8.6,6.37))
   ax=fig.add_subplot(111)

   plt.plot(gsi_observer,ufo, color='black',label="obs" , linewidth=2, marker='o')

   #box = ax.get_position()
   #ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
   ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

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

   plt.savefig('ufo_rw_stage1.png',bbox_inches='tight',dpi=100)


###--------------------------------------------------------------
###--------------------------------------------------------------
if __name__ == '__main__':

   print("start ploting")

   time=sys.argv[1]

   #call subroutine plt_radar_ref
   print("ploting obs radar reflectivity...")
   titlename="obsref_"+time
   fileame=sys.argv[1]
   plt_ref_vertical(fileame)

