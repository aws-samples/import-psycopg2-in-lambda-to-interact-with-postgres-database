import aws_cdk as cdk
from aws_cdk import aws_iam as iam, aws_lambda as aws_lambda, Duration


class LambdaStack(cdk.Stack):
    def __init__(self, scope: cdk.App, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Lambda function role
        lambda_role = iam.Role(
            self,
            "LambdaRole",
            role_name=f"lambda-execution-role-{self.region}",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_managed_policy_arn(
                    self,
                    "LambdaPolicy",
                    "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole",
                ),
            ],
        )

        # Deploy Lambda function from a zip file
        lambda_zip = aws_lambda.Function(
            self,
            "LambdaPsycopg2Zip",
            function_name="lambda-from-zip",
            runtime=aws_lambda.Runtime.PYTHON_3_8,
            code=aws_lambda.Code.from_asset("Constructs/lambda/lambda_deploy.zip"),
            handler="lambda_code.handler",
            role=lambda_role,
            timeout=Duration.seconds(10),
        )

        # Deploy Lambda function from a Docker file
        lambda_docker = aws_lambda.DockerImageFunction(
            self,
            "LambdaPsycopg2Docker",
            function_name="lambda-from-docker",
            code=aws_lambda.DockerImageCode.from_image_asset(
                directory="Constructs", cmd=["lambda_code.handler"]
            ),
            role=lambda_role,
            timeout=Duration.seconds(10),
        )

        # Checkov excepetions
        cfn_lambda_zip = lambda_zip.node.default_child
        cfn_lambda_zip.cfn_options.metadata = {
            "checkov": {
                "skip": [
                    {"id": "CKV_AWS_116", "comment": "Lambda with no DLQ"},
                ]
            }
        }
        cfn_lambda_docker = lambda_docker.node.default_child
        cfn_lambda_docker.cfn_options.metadata = {
            "checkov": {
                "skip": [
                    {"id": "CKV_AWS_116", "comment": "Lambda with no DLQ"},
                ]
            }
        }
