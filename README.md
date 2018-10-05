# DisplacedMuonReco
Repository to store code that is used to check displaced muon reconstruction (Muon POG)

Steps to setup cmssw:
```
scram p CMSSW CMSSW_9_3_2
cd CMSSW_9_3_2/src/ 
cmsenv
scram b
```

Add packages
```
git cms-addpkg RecoMuon/Configuration
git cms-addpkg RecoTracker/SpecialSeedGenerators

scram b
```
