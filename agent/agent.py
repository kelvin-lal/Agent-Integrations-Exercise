"""
Agent Integrations - Take home Exercise
Kelvin Lal
"""

#TODO add all package level imports to init/clean this up
import sys
import os
import time
import threading #for the menu, run the agent in a thread. check overhead for this vs loop
from metrics.metrics import Metrics
from metrics.metricSubmission import metric_submission
from checks.checkRun import Check

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
            Check.metric_counts["cpu"] += 1
        
        memory_metrics = metrics.memoryMetrics()
        for metric_name, metric_value in memory_metrics.items():
            metric_submission(metric_name, metric_value)
            Check.metric_counts["memory"] += 1
        
        disk_metrics = metrics.diskMetrics()
        for metric_name, metric_value in disk_metrics.items():
            metric_submission(metric_name, metric_value)
            Check.metric_counts["disk"] += 1 
        
        time.sleep(1)
    
    print("Agent stopped.")

