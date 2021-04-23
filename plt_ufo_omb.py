import numpy as np
import sys
import statistics
import math
import matplotlib.pyplot as plt
from netCDF4 import Dataset
import argparse

#from datetime import datetime
#import matplotlib.colors as colors
#import cartopy.crs as ccrs
#import cartopy.feature as cfeature

def plt_ufo_t(filename,OBSTYPE,VarName):

   thisobstype=OBSTYPE
   thisvarname=VarName
   gsihofXBc=thisvarname+'@GsiHofXBc'
   gsihofX  =thisvarname+'@GsiHofX'
   ufohofX  =thisvarname+'@hofx'
   f=Dataset(filename, mode='r')
   gsi_observer_hofXBc=f.variables[gsihofXBc][:]
   gsi_observer_hofX  =f.variables[gsihofX][:]
   ufo                =f.variables[ufohofX][:]
   geopotential_height=f.variables['height@MetaData'][:]
#  gsi_observer_withqc=f.variables['radial_velocity@GsiHofXBc'][:]
   f.close()


   plt.rcParams.update({'font.size': 12})
#  plt.rcParams.update({'line.linewidth': 8})
#=========================
   fig = plt.figure(figsize=(6,12))
   ax1=fig.add_subplot(211)
   ax1.scatter(gsi_observer_hofXBc,ufo, color='blue',label="rw", marker='o', s=3)
   plt.xlabel('gsi')
   plt.ylabel('ufo')
   plt.title(thisobstype+':gsi and ufo hofx scatter')
   figname='ufo_'+thisobstype+'_scatter.png'

   ax2=fig.add_subplot(212)
   ax2.scatter(gsi_observer_hofXBc,gsi_observer_hofX, color='blue',label="rw", marker='o', s=3)
   plt.xlabel('gsi')
   plt.ylabel('ufo')
   plt.title(thisobstype+':gsihofXBc and hofX scatter')

   plt.savefig(figname,bbox_inches='tight',dpi=100)
#=========================


#=====================================================================
#=====================================================================
if __name__ == '__main__':

   ap = argparse.ArgumentParser(description='get JEDI-GDAS output')
   ap.add_argument('-i','--inputfile', type=str, help='path to input YAML file for this analysis cycle', required=True)
   ap.add_argument('-otype', '--obstype',   type=str, help='observation type', required=True)
   ap.add_argument('-vname', '--varname',   type=str, help='variable name', required=True)
   MyArgs=ap.parse_args()
   
   print("start ploting gsi hofx v.s. ufo hofx")
   filename=MyArgs.inputfile
   OBSTYPE=MyArgs.obstype
   VarName=MyArgs.varname
   plt_ufo_t(filename,OBSTYPE,VarName)

