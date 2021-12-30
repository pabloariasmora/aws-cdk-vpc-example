#!/usr/bin/env python3

import aws_cdk as cdk

from aws_cdk_vpc_example.aws_cdk_vpc_example_stack import AwsCdkVpcExampleStack


app = cdk.App()
AwsCdkVpcExampleStack(app, "aws-cdk-vpc-example")

app.synth()
