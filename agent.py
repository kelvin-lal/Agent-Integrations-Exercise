"""
Agent Integrations - Take home Exercise
Kelvin Lal
"""
from datetime import datetime
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.metric_intake_type import MetricIntakeType
from datadog_api_client.v2.model.metric_payload import MetricPayload
from datadog_api_client.v2.model.metric_point import MetricPoint
from datadog_api_client.v2.model.metric_resource import MetricResource
from datadog_api_client.v2.model.metric_series import MetricSeries

#temporary hard code here, we'll change it to a menu or something later
import os
os.environ["DD_API_KEY"] = ""
os.environ["DD_SITE"] = "datadoghq.com"

def metric_submission(metric_name, metric_value):

    body = MetricPayload(
        series=[
            MetricSeries(
                metric=metric_name, #test metric name
                type=MetricIntakeType.UNSPECIFIED,
                points=[
                    MetricPoint(
                        timestamp=int(datetime.now().timestamp()),
                        value=metric_value,#test metric value
                    ),
                ],
                resources=[
                    MetricResource(
                        name="dummyhost",
                        type="host",
                    ),
                ],
            ),
        ],
    )

    configuration = Configuration()
    with ApiClient(configuration) as api_client:
        api_instance = MetricsApi(api_client)
        response = api_instance.submit_metrics(body=body)

        #print(response)
        print("Test metric sent!")# works as expected for now


def agent():
    print("Agent starting")

    
    # Test metric submission
    metric_submission("system.cpu.filetest", 45.2)


if __name__ == "__main__":
    agent()
