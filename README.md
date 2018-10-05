# DisplacedMuonReco
Repository to store code that is used to check displaced muon reconstruction (Muon POG)

Steps to setup cmssw:
```
scram p CMSSW CMSSW_9_3_2
cd CMSSW_9_3_2/src/ 
cmsenv
scram b
```

Add packages:
```
git cms-addpkg RecoMuon/Configuration
git cms-addpkg RecoTracker/SpecialSeedGenerators

scram b
```
Get scripts for sequence from GS to DR (only execute when you want to produce new scripts, default version in repo):
```
cmsDriver.py Configuration/GenProduction/python/EXO-PhaseIITDRFall17GS-00014-fragment.py --filein lhe:18525  --fileout file:EXO-PhaseIITDRFall17GS-00014.root --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 93X_upgrade2023_realistic_v2 --beamspot HLLHC14TeV --step GEN,SIM --nThreads 8 --geometry Extended2023D17 --era Phase2_timing --python_filename EXO-PhaseIITDRFall17GS-00014_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10

cmsDriver.py step1 --filein "file:EXO-PhaseIITDRFall17GS-00014.root" --fileout file:EXO-PhaseIITDRFall17DR-00016_step1.root  --mc --eventcontent FEVTDEBUGHLT --pileup NoPileUp --customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-DIGI-RAW --conditions 93X_upgrade2023_realistic_v2 --beamspot HLLHC14TeV --step DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@fake --nThreads 8 --geometry Extended2023D17 --era Phase2_timing --python_filename EXO-PhaseIITDRFall17DR-00016_1_cfg.py --no_exec -n 72

cmsDriver.py step2 --filein file:EXO-PhaseIITDRFall17DR-00016_step1.root --fileout file:EXO-PhaseIITDRFall17DR-00016.root --mc --eventcontent RECOSIM --runUnscheduled --customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RECO --conditions 93X_upgrade2023_realistic_v2 --beamspot HLLHC14TeV --step RAW2DIGI,L1Reco,RECO --nThreads 8 --geometry Extended2023D17 --era Phase2_timing --python_filename EXO-PhaseIITDRFall17DR-00016_2_cfg.py --no_exec -n 10
```
