import sys
import os
import shutil
from pathlib import Path
#from solo.logger import Logger
from solo.netcdf import NetCDF
from netCDF4 import Dataset


output = '/work/noaa/da/sliu/R2D2/gfs/diag/a064_save/PT6H/tmp/'
output1 = '/work/noaa/da/sliu/R2D2/gfs/diag/a064_save/PT6H/tmp1'
part = output+'diag'
netcdf_files = []
# the number of files depends on the number of processors used but also on the
# layout in the geometry. We merge whats we find, files are numbered 0000, 0001 etc...

part_no = 0
go = True
while go:
    #filename = f'{part}_{part_no:04}.nc4'
    filename = f'{part}_{part_no}.nc4'
    print(filename)
    if os.path.exists(filename):
        data = Dataset(filename)
        if len(data.dimensions['nlocs']) > 0:
            netcdf_files.append(filename)
    else:
        go = False
    
    if part_no > 10:
        go = False
        
    part_no += 1

# Concatenate each obs file into one file, based on current obs window
obs_name='test.nc'
if (len(netcdf_files)) > 0:
    nc = NetCDF(obs_name)
    nc.concat_files(netcdf_files, output1, compression=True)
else:
    # no data to concatenate, copy initial file as output
    shutil.copy(f'{part}_0000.nc4', output1)
