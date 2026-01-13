"""
Agent Integrations - Take home Exercise
Kelvin Lal
"""


def check_print(check):
    print("Status Check starting...\n")
    print(f"{check.metric_type} Metrics:")
    print(f"Metrics Collected: {check.metric_quantity}")
    
    for name, value in check.results.items():
        print(f"  {name}: {value}")

