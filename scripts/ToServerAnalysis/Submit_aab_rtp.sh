  GNU nano 2.3.1                                                File: Submit_aab_rtp.sh                                                                                            Modified  

#!/bin/bash -l

files="athal scere dmel eugra potra"
links="reaction binding regulation catalysis"
outFolder=$(realpath "./results/tpot")
tpot=$(realpath "./analysisTPOT.py")
runTPOT=$(realpath "./aab_rtp.sh")

if [ ! -d $outFolder ]; then
  mkdir $outFolder
fi

module load conda
source conda_init.sh
conda activate aab_rtp


for x in $files; do

if [ ! -d $outFolder/$x ]; then
  mkdir $outFolder/$x
fi

for i in $links; do
for cv in 1 2 3 4 5 6 7 8 9 10;do
rtpFile=$(realpath dataToServer/$x_$i_to_Sk$cv.pkl)
 $runTPOT  $tpot $rtpFile

done
done



















