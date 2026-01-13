"""
Agent Integrations - Take home Exercise
Kelvin Lal
"""
from checks.checkPrint import check_print


class Check:

    def __init__(self, metric_type):
        self.metric_type = metric_type
        self.results = {}

    def print_results(self):#trying something new here, call an external function within a class when this class is called
        check_print(self)

    def check():
        # Initialize each metric check
        cpu_check = Check("CPU")
        memory_check = Check("Memory")
        disk_check = Check("Disk")
        
        # Pass each to checkPrint
        check_print(cpu_check)
        check_print(memory_check)
        check_print(disk_check)

