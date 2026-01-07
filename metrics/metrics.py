"""
Agent Integrations - Take home Exercise
Kelvin Lal
"""

import psutil
#key libraries for this project: https://psutil.readthedocs.io/en/latest/


def cpuMetrics():
    #could use something like a yield parameter to get these metrics as a generator, would make sense for something 
    #for simplicity sake, it may be as simple as creating a dictionary of metrics and returning it
    
    metrics =  {}

    metrics['test.metric.cpu_usage'] = psutil.cpu_percent()
    metrics['test.metric.cpu_count'] = psutil.cpu_count()

    return metrics

def memoryMetrics():

    metrics =  {}

    metrics['test.metric.memory_usage'] = psutil.virtual_memory().percent
    metrics['test.metric.memory_available'] = psutil.virtual_memory().free

    return metrics

def diskMetrics():

    metrics =  {}

    metrics['test.metric.disk_usage'] = psutil.disk_usage()
    metrics['test.metric.disk_io_counters'] = psutil.disk_io_counters()

    return metrics



