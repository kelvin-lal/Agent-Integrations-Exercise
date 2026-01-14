"""
Agent Integrations - Take home Exercise
Kelvin Lal
"""
from metrics.metricSubmission import metric_submission


class CustomCheck:
    def gauge(self, metric_name, value):
        metric_submission(metric_name, value)

    def run(self):
        self.gauge('custom.check.metric', 1)
