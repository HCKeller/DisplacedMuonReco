#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630
if [ -r CMSSW_9_3_6/src ] ; then 
 echo release CMSSW_9_3_6 already exists
else
scram p CMSSW CMSSW_9_3_6
fi
cd CMSSW_9_3_6/src
eval `scram runtime -sh`

curl -s --insecure https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/EXO-PhaseIITDRFall17GS-00014 --retry 2 --create-dirs -o Configuration/GenProduction/python/EXO-PhaseIITDRFall17GS-00014-fragment.py 
[ -s Configuration/GenProduction/python/EXO-PhaseIITDRFall17GS-00014-fragment.py ] || exit $?;

scram b
cd ../../
cmsDriver.py Configuration/GenProduction/python/EXO-PhaseIITDRFall17GS-00014-fragment.py --filein lhe:18525  --fileout file:EXO-PhaseIITDRFall17GS-00014.root --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 93X_upgrade2023_realistic_v2 --beamspot HLLHC14TeV --step GEN,SIM --nThreads 8 --geometry Extended2023D17 --era Phase2_timing --python_filename EXO-PhaseIITDRFall17GS-00014_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 2264 || exit $? ; 

