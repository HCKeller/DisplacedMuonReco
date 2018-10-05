#!/bin/bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630
if [ -r CMSSW_9_3_8/src ] ; then 
 echo release CMSSW_9_3_8 already exists
else
scram p CMSSW CMSSW_9_3_8
fi
cd CMSSW_9_3_8/src
eval `scram runtime -sh`

curl -s --insecure https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/EXO-PhaseIISummer17pLHE-00018 --retry 2 --create-dirs -o Configuration/GenProduction/python/EXO-PhaseIISummer17pLHE-00018-fragment.py 
[ -s Configuration/GenProduction/python/EXO-PhaseIISummer17pLHE-00018-fragment.py ] || exit $?;

scram b
cd ../../
cmsDriver.py Configuration/GenProduction/python/EXO-PhaseIISummer17pLHE-00018-fragment.py --filein lhe:18525  --fileout file:EXO-PhaseIISummer17pLHE-00018.root --mc --eventcontent LHE --datatier LHE --conditions 93X_upgrade2023_realistic_v5 --step NONE --python_filename EXO-PhaseIISummer17pLHE-00018_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10000 || exit $? ; 
