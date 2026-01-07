"""
Agent Integrations - Take home Exercise
Kelvin Lal
"""
import time
import os
from metrics.metrics import cpuMetrics, memoryMetrics, diskMetrics
from metrics.metricSubmission import metric_submission

# Temporary hard code here, we'll change it to a menu or something later
os.environ["DD_API_KEY"] = "add_api_key_here"
os.environ["DD_SITE"] = "datadoghq.com"

def agent():
    print("Agent starting")
    
    while True:
        cpu_metrics = cpuMetrics()
        for metric_name, metric_value in cpu_metrics.items():
            metric_submission(metric_name, metric_value) 
        memory_metrics = memoryMetrics()
        for metric_name, metric_value in memory_metrics.items():
            metric_submission(metric_name, metric_value) 
        disk_metrics = diskMetrics()
        for metric_name, metric_value in disk_metrics.items():
            metric_submission(metric_name, metric_value) 
        
        time.sleep(1)


if __name__ == "__main__":
    agent()
