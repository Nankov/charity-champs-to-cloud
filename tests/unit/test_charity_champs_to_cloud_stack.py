import aws_cdk as core
import aws_cdk.assertions as assertions

from charity_champs_to_cloud.charity_champs_to_cloud_stack import CharityChampsToCloudStack

# example tests. To run these tests, uncomment this file along with the example
# resource in charity_champs_to_cloud/charity_champs_to_cloud_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CharityChampsToCloudStack(app, "charity-champs-to-cloud")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
