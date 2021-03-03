#!/usr/bin/env python3
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import netCDF4 as nc
import numpy as np
import argparse
import glob
import os

def plot_world_map(lon, lat, lont, latt, plotpath):
    # plot generic world map
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
#   ax.add_feature(cfeature.GSHHSFeature(scale='auto'))
#   ax.set_extent([-138, -56.5, 17.5, 60.0],crs=ccrs.PlateCarree())
    ax.set_extent([-100.25, -100.0, 40, 40.25],crs=ccrs.PlateCarree())
    cmap = 'viridis'
    cbarlabel = 'grid'
#       cmap = 'bwr'
    cs = ax.scatter(lon, lat,s=35,marker="o",c='r')
    cs = ax.scatter(lont, latt,s=35,marker="s",c='b')
#   cs = ax.pcolormesh(lons, lats, data,vmin=vmin,vmax=vmax,cmap=cmap)
#   cb = plt.colorbar(cs, orientation='horizontal', shrink=0.5, pad=.04)
#   cb.set_label(cbarlabel, fontsize=12)

    plttitle = 'JEDI FV3 grid in 0.25x0.25 box by %s' % (os.environ['LOGNAME'])
    plt.title(plttitle)
    plt.savefig(plotpath,bbox_inches='tight',dpi=100)
    plt.close('all')

def read_var(geopath):
    tmpdata = nc.Dataset(geopath,'r')
    tmplatt = tmpdata.variables['grid_latt'][:]
    tmplat = tmpdata.variables['grid_lat'][:]
    tmpdata.close()

    arrayshapet = tmplatt.shape
    lontout = np.empty(arrayshapet)
    lattout = np.empty(arrayshapet)

    arrayshape = tmplat.shape
    lonout = np.empty(arrayshape)
    latout = np.empty(arrayshape)

    geonc = nc.Dataset(geopath)
    lat = geonc.variables['grid_lat'][:]
    lon = geonc.variables['grid_lon'][:]
    latt = geonc.variables['grid_latt'][:]
    lont = geonc.variables['grid_lont'][:]
    geonc.close()

    latout[:,:] = lat
    lonout[:,:] = lon
    lattout[:,:] = latt
    lontout[:,:] = lont

    return lonout, latout, lontout, lattout


def gen_figure(geopath):
    # read the files to get the 2D array to plot
    lon, lat, lont, latt = read_var(geopath)
    plotpath ='fv3grid.png'
    plot_world_map(lon, lat, lont, latt, plotpath)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument('-g', '--geoin', help="path to prefix of input files with geolat/geolon", required=True)
    MyArgs = ap.parse_args()
    gen_figure(MyArgs.geoin)
