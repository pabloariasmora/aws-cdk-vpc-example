from constructs import Construct
from aws_cdk import (
    Stack,
    aws_ec2 as ec2
)

NAME = "Development"

class AwsCdkVpcExampleStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.vpc = ec2.Vpc(self, "{}-VPC".format(NAME),
            max_azs=2,
            cidr="10.10.0.0/16",
            # configuration will create 3 groups in 2 AZs = 6 subnets.
            subnet_configuration=[ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name="{}-PublicSubnet".format(NAME),
                    cidr_mask=24
                ), ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT,
                    name="{}-PrivateSubnet".format(NAME),
                    cidr_mask=24
                ), ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                    name="{}-DBSubnet".format(NAME),
                    cidr_mask=24
                )
            ],
            # Default Natgateway configuration, 1 per public subnet.
            nat_gateways=2,
            )

