"""
Agent Integrations - Take home Exercise
Kelvin Lal
"""

import psutil
#key libraries for this project: https://psutil.readthedocs.io/en/latest/

class Metrics:
    def __init__(self):
        self.metrics = {}

    def cpuMetrics(self):
        #could use something like a yield parameter to get these metrics as a generator, would make sense for something 
        #for simplicity sake, it may be as simple as creating a dictionary of metrics and returning it
        
        metrics =  {}

        metrics['test.metric.cpu_usage'] = psutil.cpu_percent()
        metrics['test.metric.cpu_count'] = psutil.cpu_count()

        return metrics

    def memoryMetrics(self):

        metrics =  {}

        metrics['test.metric.memory_usage'] = psutil.virtual_memory().percent
        metrics['test.metric.memory_available'] = psutil.virtual_memory().free

        return metrics

    def diskMetrics(self):
        #ran into a few issues here, not sure if it's because of the way I'm using the library or what
        metrics =  {}

        metrics['test.metric.disk_usage'] = psutil.disk_usage('/').percent #using percent for now to extract a float, need to revisit this in the future for a better solution
        #metrics['test.metric.disk_io_counters'] = psutil.disk_io_counters()
        #this variable doenst have a .percent attribute. another revisit, also why can we use a float here and not on the metric above?

        return metrics



