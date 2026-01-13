"""
Agent Integrations - Take home Exercise
Kelvin Lal

Print utilities for checks.
"""


def check_print(check):
    """
    Print check results.
    
    Args:
        check: A Check instance with metric_type and results attributes
    """
    print("Status Check starting...\n")
    print(f"{check.metric_type} Metrics:")
    
    for name, value in check.results.items():
        print(f"  {name}: {value}")

