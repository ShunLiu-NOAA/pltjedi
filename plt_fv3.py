import numpy as np
import sys
from netCDF4 import Dataset
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import cartopy.crs as ccrs
import cartopy.feature as cfeature

def plt_ref_vertical(figname):

   f=Dataset(figname, mode='r')
   print (f)
   nlon=f.dimensions['lon'].size
   nlat=f.dimensions['lat'].size
   lat=f.variables['lats'][:]
   lon=f.variables['lons'][:]
   sphum=f.variables['sphum'][:,:,:,:]
   temp=f.variables['T'][:,:,:,:]
   f.close()

   x,y=np.meshgrid(lon,lat)

   print(x[:,:])
   print(y[:,:])

   # create figure and axes instances
   plt.figure(figsize=(15,12))
   ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=0))
   ax.add_feature(cfeature.GSHHSFeature(scale='auto'))
#  ax.coastlines()
   ax.set_extent([-180, 180, -90, 90])
 

#  cmap,bounds,norm=ncepy.create_ncep_radar_ref_color_table()
#  cs=plt.scatter(glat,nlev,c=oref,s=58,cmap=cmap,norm=norm,marker="s",edgecolor='none')
#  cmap=plt.get_cmap("Greys")
  
   data=np.zeros((nlat,nlon))
   data[:,:]=temp[0,0,:,:]
   print (data)
   upperbound = np.max(data)
   lowerbound = np.min(data)
   bins = (upperbound - lowerbound)/10.0
   clevs=np.arange(lowerbound, upperbound+bins, bins)
   norm = colors.BoundaryNorm(boundaries=clevs, ncolors=256)

   #cs=plt.scatter(x,y,c=pres,s=40,cmap=cmap,norm=norm,marker=(verts_function(1,1,0.25),0),edgecolor='none')
   #cs=plt.scatter(x,y,c=pres,s=40,cmap='bwr',norm=norm,marker="s",edgecolor='none')
   #cs=plt.scatter(x,y,c=data,s=10,cmap='bwr',norm=norm,transform=ccrs.PlateCarree())
   cs=plt.contourf(x,y,data,clevs,cmap='bwr',transform=ccrs.PlateCarree())

   cb = plt.colorbar(cs, shrink=0.5, pad=.04, extend='both')
   cb.ax.tick_params(labelsize=5.0)

#  plt.ylim([0,60])
#  plt.xlim([24,52])
#  plt.title(titlename+' latitude CREF',fontsize=25)

#  clevs=bins
#  cbar = plt.colorbar(cs,location='bottom',pad=0.05,ticks=clevs)

#  titlename=
   plt.savefig('./'+figname+'.png',bbox_inches='tight',dpi=100)


###--------------------------------------------------------------
###--------------------------------------------------------------
if __name__ == '__main__':

   print("start ploting vertical section of reflectiivty'r")

   time=sys.argv[1]

   #call subroutine plt_radar_ref
   print("ploting obs radar reflectivity...")
   figname=sys.argv[1]
   plt_ref_vertical(figname)

