import numpy as np
import sys
import statistics
import math
import matplotlib.pyplot as plt
from netCDF4 import Dataset
import argparse
import time
import yaml
from scipy import stats

#from datetime import datetime
#import matplotlib.colors as colors
#import cartopy.crs as ccrs
#import cartopy.feature as cfeature

#def matchobstype(gsi_hofx,gsiobstype):
#   nloc=len(gsi_hofx)
#   gsi_hofx_obstype=[]
#   j=0
#   for i in range(0,nloc):
#      if(gsiobstype[i]==120):
#        gsi_hofx_obstype[j]=gsi_hofx[i]
#        j=j+1
#   return gsi_hofx_obstype

def read_diag(filename,OBSTYPE,VarName):
   thisobstype=OBSTYPE
   thisvarname=VarName
   gsihofXBc=thisvarname+'@GsiHofXBc'
   gsihofX  =thisvarname+'@GsiHofX'
   ufohofX  =thisvarname+'@hofx'
   obstype_num  =thisvarname+'@ObsType'
   ufo_effectiveqc  =thisvarname+'@EffectiveQC'
   f=Dataset(filename, mode='r')
   gsi_observer_hofXBc=f.variables[gsihofXBc][:]
   gsi_observer_hofX  =f.variables[gsihofX][:]
   ufo                =f.variables[ufohofX][:]
   gsiobstype         =f.variables[obstype_num][:]
   height             =f.variables['height@MetaData'][:]
   pres               =f.variables['air_pressure@MetaData'][:]
   ufoqc              =f.variables[ufo_effectiveqc][:]
   f.close()
   height=height/1000.0
   return gsi_observer_hofX,ufo,height,pres

def han(gsi,ufo):
#  k2,p=stats.mstats.normaltest(gsi)
#  print("==================")
#  print("normaltest::")
#  print(k2,p)
#  print("==================")

#  print(stats.describe(gsi_observer_noqc))
#  print(stats.tstd(gsi_observer_noqc))
#  exit()

   diff=ufo-gsi
   k2,p=stats.mstats.ttest_1samp(diff,0.0)
   print("1 sample test gsi-ufo::")
   print(k2,p)
   print("==================")

   k2,p=stats.mstats.ttest_ind(ufo, gsi)
   print("two sample test ufo-gsi with QC::")
   print(k2,p)
   print("==================")
     
def plt_ufo_t(gsi,ufo,hgt,OBSTYPE):

#  for i in range(0,len(gsiobstype)):
#    if(gsi_observer_hofX[i]<-100):
#      print(gsi_observer_hofX[i],gsiobstype[i])
#  gsi_hofx_220=matchobstype(gsi_observer_hofX,gsiobstype) 
#  print(len(gsi_hofx_220))
   thisobstype=OBSTYPE

   gsix=gsi
   thistime=time.strftime("%Y%m%d_%H%M")

   plt.rcParams.update({'font.size': 12})
#  plt.rcParams.update({'line.linewidth': 8})
#=========================
   fig = plt.figure(figsize=(12,12))
   ax1=fig.add_subplot(221)
   ax1.scatter(gsi,ufo, color='blue',label="rw", marker='o', s=3)
   plt.xlabel('gsi')
   plt.ylabel('ufo')
   plt.title(thisobstype+':gsi and ufo hofx scatter')

   diff=gsi-ufo
   ax2=fig.add_subplot(222)
#  ax2.scatter(gsi,gsix, color='blue',label="rw", marker='o', s=3)
   plt.xlabel('gsi')
   plt.ylabel('ufo')
   plt.hist(diff,bins=50)
#  plt.text(180,300,'obstype 120')
   plt.title(thisobstype+':gsi and ufo hofx scatter')

   diff=gsi-ufo
   ax3=fig.add_subplot(223)
   ax3.scatter(diff,hgt, color='blue',label="rw", marker='o', s=3)
   plt.xlabel('gsi')
   plt.ylabel('height')
   plt.grid(True)
   plt.title(thisobstype+':gsi-ufo scatter in vertical')

#  diff=gsi-gsix
   ax4=fig.add_subplot(224)
   ax4.scatter(gsi,hgt, color='blue',label="rw", marker='o', s=3)
   plt.xlabel('gsi')
   plt.ylabel('height')
   plt.grid(True)
   plt.title(thisobstype+':gsi hofx in vertical')

#  plt.title(thisobstype+':gsihofXBc and hofX scatter')

   figname='ufo_'+thisobstype+'_scatter_'+thistime+'.png'
   plt.savefig(figname,bbox_inches='tight',dpi=100)
#=========================


#=====================================================================
#=====================================================================
if __name__ == '__main__':

#  ap = argparse.ArgumentParser(description='get JEDI-GDAS output')
#  ap.add_argument('-i',     '--inputfile', \
#                  type=str, help='path to input YAML file', required=True)
#  ap.add_argument('-otype', '--obstype',   type=str, help='observation type', required=True)
#  ap.add_argument('-vname', '--varname',   type=str, help='variable name', required=True)
#  MyArgs=ap.parse_args()
#  print("start ploting gsi hofx v.s. ufo hofx")

   print("read diag files:")

   stream = open("config.yaml", 'r')
   config = yaml.safe_load(stream)

   OBSTYPE=config['OBSTYPE']
   VarName=config['VarName']
   fldir=config['paths']['inputdir']

   i=0
   filename=fldir+'/'+config['inputfile']+'_'+str(i)+'.nc4'
   gsi,ufo,hgt,pres,ufoqc=read_diag(filename,OBSTYPE,VarName)

#  for i in range(1,116):
   for i in range(1,112):
     filename=fldir+'/'+config['inputfile']+'_'+str(i)+'.nc4'
     print(filename)
     gsitmp,ufotmp,hgttmp,prestmp,ufoqc=read_diag(filename,OBSTYPE,VarName)
     print(len(gsitmp))
     gsi=np.ma.concatenate((gsi,gsitmp))
     ufo=np.ma.concatenate((ufo,ufotmp))
     hgt=np.ma.concatenate((hgt,hgttmp))
     pres=np.ma.concatenate((pres,prestmp))
#    print(len(gsi))
#    print(type(gsitem))

   print(gsi.count())
   print(ufo.count())
   print(hgt.count())
   print(pres.count())
#  ufo=np.ma.masked_where(np.ma.getmask(gsi),ufo)
   ufo=np.ma.masked_where(np.ma.getmask(gsi),ufo)
#  print(ufo.count())
   exit()
   if OBSTYPE=='SPFH' :
     gsi=gsi*1000.0
     ufo=ufo*1000.0
#  plt_ufo_t(gsi,ufo,hgt,OBSTYPE)
#  han(gsi,ufo)

