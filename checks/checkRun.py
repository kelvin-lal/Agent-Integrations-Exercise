"""
Agent Integrations - Take home Exercise
Kelvin Lal
"""
from checks.checkPrint import check_print


class Check:
    metric_counts = {
        "cpu": 0,
        "memory": 0,
        "disk": 0
    } #dont think this will always work, class variables should be inhereted throughout the code

    def __init__(self, metric_type, metric_quantity=0):
        self.metric_type = metric_type
        self.metric_quantity = metric_quantity
        self.results = {}

    def print_results(self):#trying something new here, call an external function within a class when this class is called
        check_print(self)

    def check():
        cpu_check = Check("CPU")
        memory_check = Check("Memory")
        disk_check = Check("Disk")

    def metricsCheck():
        counts = Check.metric_counts
        
        #TODO this should dynamically be set here, hate this hardcode, find a way to dynamically get the metric type or integration 
        cpu_check = Check("CPU", counts["cpu"]) 
        memory_check = Check("Memory", counts["memory"])
        disk_check = Check("Disk", counts["disk"])
        
        check_print(cpu_check)
        check_print(memory_check)
        check_print(disk_check)

