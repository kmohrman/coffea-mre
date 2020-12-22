import numpy as np
from coffea import hist, processor

class AnalysisProcessor(processor.ProcessorABC):
    def __init__(self):
        # Create the histograms
        self._accumulator = processor.dict_accumulator({
        'dummy'   : hist.Hist("Dummy" , hist.Cat("sample", "sample"), hist.Bin("dummy", "Number of events", 1, 0, 1)),
        })

    @property
    def accumulator(self):
        return self._accumulator

    def process(self, events):
        dataset = events.metadata['dataset']
        hout = self.accumulator.identity()
        hout['dummy'].fill(sample=dataset, dummy=1, weight=events.size)
        return hout

    def postprocess(self, accumulator):
        return accumulator

