"""
Agent Integrations - Take home Exercise
Kelvin Lal
"""

import psutil


def cpuMetrics():
    #could use something like a yield parameter to get these metrics as a generator, would make sense for something 
    #for simplicity sake, it may 
    
    metrics =  {}

    metrics['test.metric.cpu_usage'] = psutil.cpu_percent()
    metrics['test.metric.cpu_count'] = psutil.cpu_count()

    return metrics


