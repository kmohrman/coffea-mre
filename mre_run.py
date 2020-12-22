from coffea import processor
from coffea.util import load
import mre_processor

flist = {
    'TTTo2L2Nu' : [
        'root://ndcms.crc.nd.edu//store/mc/RunIISummer19UL17NanoAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/NANOAODSIM/106X_mc2017_realistic_v6-v1/260000/10470AF9-B021-3742-A885-12D32B903131.root'
        #'root://global.cern.ch//store/mc/RunIISummer19UL17NanoAOD/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/NANOAODSIM/106X_mc2017_realistic_v6-v1/260000/10470AF9-B021-3742-A885-12D32B903131.root'
    ]
}

# Run the processor 
nworkers = 8
processor_instance = mre_processor.AnalysisProcessor()
#output = processor.run_uproot_job(flist, treename='Events', processor_instance=processor_instance, executor=processor.iterative_executor, executor_args={'nano':True,'workers': nworkers, 'pre_workers': 1}, chunksize=500000)
output = processor.run_uproot_job(flist, treename='Events', processor_instance=processor_instance, executor=processor.futures_executor, executor_args={'nano':True,'workers': nworkers, 'pre_workers': 1}, chunksize=500000)
