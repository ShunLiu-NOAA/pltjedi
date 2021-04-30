#!/bin/bash

genyaml=false

if [ $genyaml = "true" ]; then
   echo "generating confg.yaml"
fi

exp=a05v
diagdir=/work/noaa/da/sliu/R2D2/gfs/diag/$exp/PT6H/tmp

cat > config.yaml <<EOF
paths:
   inputdir: ${diagdir}
   outputdir: ./
VarName: air_temperature
inputfile: diag
OBSTYPE: T
subtask: 5
EOF

python plt_ufo_omb.py



#python plt_ufo_omb.py -i /work/noaa/da/sliu/R2D2/gfs/diag/a05v/PT6H/2020-12-14/gfs.a05v.diag.PT6H.sondes.2020-12-14T21:00:00Z.PT6H.nc4  \
#                   -otype Ps -vname air_temperature
