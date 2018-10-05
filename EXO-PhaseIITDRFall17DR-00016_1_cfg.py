# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --filein dbs:/DarkSUSY_mH_125_mGammaD_20_cT_1000_TuneCUETP8M1_14TeV_pythia8/PhaseIITDRFall17GS-93X_upgrade2023_realistic_v2-v1/GEN-SIM --fileout file:EXO-PhaseIITDRFall17DR-00016_step1.root --mc --eventcontent FEVTDEBUGHLT --pileup NoPileUp --customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-DIGI-RAW --conditions 93X_upgrade2023_realistic_v2 --beamspot HLLHC14TeV --step DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@fake --nThreads 8 --geometry Extended2023D17 --era Phase2_timing --python_filename EXO-PhaseIITDRFall17DR-00016_1_cfg.py --no_exec -n 72
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT',eras.Phase2_timing)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2023D17Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_Fake_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring(
        'file:EXO-PhaseIITDRFall17GS-00014.root',
        #~ '/store/mc/PhaseIITDRFall17GS/DarkSUSY_mH_125_mGammaD_20_cT_1000_TuneCUETP8M1_14TeV_pythia8/GEN-SIM/93X_upgrade2023_realistic_v2-v1/80000/A615866D-6A5B-E811-818A-FA163EAF58A2.root', 
        #~ '/store/mc/PhaseIITDRFall17GS/DarkSUSY_mH_125_mGammaD_20_cT_1000_TuneCUETP8M1_14TeV_pythia8/GEN-SIM/93X_upgrade2023_realistic_v2-v1/80000/1C1CE6B3-655B-E811-9DB4-FA163E63900C.root', 
        #~ '/store/mc/PhaseIITDRFall17GS/DarkSUSY_mH_125_mGammaD_20_cT_1000_TuneCUETP8M1_14TeV_pythia8/GEN-SIM/93X_upgrade2023_realistic_v2-v1/80000/0EC6A304-6B5B-E811-A836-FA163E164C6B.root', 
        #~ '/store/mc/PhaseIITDRFall17GS/DarkSUSY_mH_125_mGammaD_20_cT_1000_TuneCUETP8M1_14TeV_pythia8/GEN-SIM/93X_upgrade2023_realistic_v2-v1/80000/CC552FC3-695B-E811-9AAA-FA163E36B86F.root', 
        #~ '/store/mc/PhaseIITDRFall17GS/DarkSUSY_mH_125_mGammaD_20_cT_1000_TuneCUETP8M1_14TeV_pythia8/GEN-SIM/93X_upgrade2023_realistic_v2-v1/80000/BE85E873-655B-E811-A24E-FA163EA45447.root', 
        #~ '/store/mc/PhaseIITDRFall17GS/DarkSUSY_mH_125_mGammaD_20_cT_1000_TuneCUETP8M1_14TeV_pythia8/GEN-SIM/93X_upgrade2023_realistic_v2-v1/80000/4C985A9F-6D5B-E811-B8FB-FA163E960220.root', 
        #~ '/store/mc/PhaseIITDRFall17GS/DarkSUSY_mH_125_mGammaD_20_cT_1000_TuneCUETP8M1_14TeV_pythia8/GEN-SIM/93X_upgrade2023_realistic_v2-v1/80000/10134CDA-6B5B-E811-8C61-FA163E0C21C6.root', 
        #~ '/store/mc/PhaseIITDRFall17GS/DarkSUSY_mH_125_mGammaD_20_cT_1000_TuneCUETP8M1_14TeV_pythia8/GEN-SIM/93X_upgrade2023_realistic_v2-v1/80000/2E84EAD9-6B5B-E811-982E-FA163E0C21C6.root', 
        #~ '/store/mc/PhaseIITDRFall17GS/DarkSUSY_mH_125_mGammaD_20_cT_1000_TuneCUETP8M1_14TeV_pythia8/GEN-SIM/93X_upgrade2023_realistic_v2-v1/80000/74D15AFF-6F5B-E811-8A4B-FA163E7026C7.root', 
        #~ '/store/mc/PhaseIITDRFall17GS/DarkSUSY_mH_125_mGammaD_20_cT_1000_TuneCUETP8M1_14TeV_pythia8/GEN-SIM/93X_upgrade2023_realistic_v2-v1/80000/A0385F5B-085C-E811-BD46-FA163E854D3B.root'
        ),
    inputCommands = cms.untracked.vstring('keep *', 
        'drop *_genParticles_*_*', 
        'drop *_genParticlesForJets_*_*', 
        'drop *_kt4GenJets_*_*', 
        'drop *_kt6GenJets_*_*', 
        'drop *_iterativeCone5GenJets_*_*', 
        'drop *_ak4GenJets_*_*', 
        'drop *_ak7GenJets_*_*', 
        'drop *_ak8GenJets_*_*', 
        'drop *_ak4GenJetsNoNu_*_*', 
        'drop *_ak8GenJetsNoNu_*_*', 
        'drop *_genCandidatesForMET_*_*', 
        'drop *_genParticlesForMETAllVisible_*_*', 
        'drop *_genMetCalo_*_*', 
        'drop *_genMetCaloAndNonPrompt_*_*', 
        'drop *_genMetTrue_*_*', 
        'drop *_genMetIC5GenJs_*_*'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1 nevts:72'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:EXO-PhaseIITDRFall17DR-00016_step1.root'),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.digitizers = cms.PSet(process.theDigitizersValid)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '93X_upgrade2023_realistic_v2', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi_valid)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.FEVTDEBUGHLToutput_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(8)
process.options.numberOfStreams=cms.untracked.uint32(0)

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.aging
from SLHCUpgradeSimulations.Configuration.aging import customise_aging_1000 

#call to customisation function customise_aging_1000 imported from SLHCUpgradeSimulations.Configuration.aging
process = customise_aging_1000(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
