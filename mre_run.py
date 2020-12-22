from coffea import processor
from coffea.util import load
import mre_processor

# Load samples
samplesdict = load('mre_sample.coffea')
flist = {}
for k in samplesdict.keys():
  flist[k] = samplesdict[k]['files']

# Run the processor 
nworkers = 8
processor_instance = mre_processor.AnalysisProcessor(samplesdict)
#output = processor.run_uproot_job(flist, treename='Events', processor_instance=processor_instance, executor=processor.iterative_executor, executor_args={'nano':True,'workers': nworkers, 'pre_workers': 1}, chunksize=500000)
output = processor.run_uproot_job(flist, treename='Events', processor_instance=processor_instance, executor=processor.futures_executor, executor_args={'nano':True,'workers': nworkers, 'pre_workers': 1}, chunksize=500000)
