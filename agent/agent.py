"""
Agent Integrations - Take home Exercise
Kelvin Lal
"""
import sys
import os
import time
import threading #for the menu, run the agent in a thread. check overhead for this vs loop
from metrics.metrics import Metrics
from metrics.metricSubmission import metric_submission

# Temporary hard code here, we'll change it to a menu or something later
os.environ["DD_API_KEY"] = "api-key"
os.environ["DD_SITE"] = "datadoghq.com"

# global param (could be a class variable???)
agent_running = False


def agent():
    global agent_running
    print("Agent starting...")
    metrics = Metrics()
    
    while agent_running:
        cpu_metrics = metrics.cpuMetrics()
        for metric_name, metric_value in cpu_metrics.items():
            metric_submission(metric_name, metric_value) 
        memory_metrics = metrics.memoryMetrics()
        for metric_name, metric_value in memory_metrics.items():
            metric_submission(metric_name, metric_value) 
        disk_metrics = metrics.diskMetrics()
        for metric_name, metric_value in disk_metrics.items():
            metric_submission(metric_name, metric_value) 
        
        time.sleep(1)
    
    print("Agent stopped.")

