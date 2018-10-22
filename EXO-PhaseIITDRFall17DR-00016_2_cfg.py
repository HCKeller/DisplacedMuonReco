# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --filein file:EXO-PhaseIITDRFall17DR-00016_step1.root --fileout file:EXO-PhaseIITDRFall17DR-00016.root --mc --eventcontent RECOSIM --runUnscheduled --customise SLHCUpgradeSimulations/Configuration/aging.customise_aging_1000,Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-RECO --conditions 93X_upgrade2023_realistic_v2 --beamspot HLLHC14TeV --step RAW2DIGI,L1Reco,RECO --nThreads 8 --geometry Extended2023D17 --era Phase2_timing --python_filename EXO-PhaseIITDRFall17DR-00016_2_cfg.py --no_exec -n 10
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('RECO',eras.Phase2_timing)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2023D17Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

# Input source
process.source = cms.Source("PoolSource",
    #~ fileNames = cms.untracked.vstring('file:EXO-PhaseIITDRFall17DR-00016_step1.root'),
    fileNames = cms.untracked.vstring('file:MuonGun_DR_step1.root'),
    #~ fileNames = cms.untracked.vstring(),
    secondaryFileNames = cms.untracked.vstring(),
    eventsToProcess = cms.untracked.VEventRange('1:1-1:2')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2 nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:EXO-PhaseIITDRFall17DR-00016.root'),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '93X_upgrade2023_realistic_v2', '')

# Add analyzer for seeds of outIn
#~ from RecoMuon.Configuration.DisplacedMuonSeededStep_cff import muonSeededSeedsOutInDisplaced

process.muonSeeds = cms.EDAnalyzer("MuonSeedsAnalyzer",
    tkpt = cms.InputTag("muonSeededSeedsOutIn:tkpt"),
    tketa = cms.InputTag("muonSeededSeedsOutIn:tketa"),
    tkphi = cms.InputTag("muonSeededSeedsOutIn:tkphi"),
    tkd0 = cms.InputTag("muonSeededSeedsOutIn:tkd0"),
    tkdxy = cms.InputTag("muonSeededSeedsOutIn:tkdxy"),
    tkDisplacedpt = cms.InputTag("muonSeededSeedsOutInDisplaced:tkpt"),
    tkDisplacedeta = cms.InputTag("muonSeededSeedsOutInDisplaced:tketa"),
    tkDisplacedphi = cms.InputTag("muonSeededSeedsOutInDisplaced:tkphi"),
    tkDisplacedd0 = cms.InputTag("muonSeededSeedsOutInDisplaced:tkd0"),
    tkDisplaceddxy = cms.InputTag("muonSeededSeedsOutInDisplaced:tkdxy"),
    MuonSeededSeedsOutInDisplacedNumSeeds = cms.InputTag("muonSeededSeedsOutInDisplaced:NumSeeds"),
    MuonSeededSeedsOutInNumSeeds = cms.InputTag("muonSeededSeedsOutIn:NumSeeds"),
    earlyDisplacedMuons = cms.InputTag("earlyDisplacedMuons"),
    genParticles = cms.InputTag("genParticles"),
    MuonSeededTracksOutInDisplaced = cms.InputTag("muonSeededTracksOutInDisplaced"),
    MuonSeededTrackCandidatesOutInDisplaced = cms.InputTag("muonSeededTrackCandidatesOutInDisplaced"),
    #~ MuonSeededTracksOutInDisplacedClassifier = cms.InputTag("muonSeededTracksOutInDisplacedClassifier"),
)

process.muonSeeds_step = cms.Path(process.muonSeeds)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('MuonSeeds.root')
)

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.endjob_step,process.RECOSIMoutput_step,process.muonSeeds_step)
#~ process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.endjob_step,process.RECOSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(1)
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

# End of customisation functions
#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
