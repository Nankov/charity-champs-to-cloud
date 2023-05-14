from aws_cdk import (
    # Duration,
    Stack,
    aws_apigateway as apigw,
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb,
)
from constructs import Construct


class CharityChampsToCloudStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        user_table = dynamodb.Table(
            self, "charitychamps-users",
            table_name="charitychamps-users",
            partition_key=dynamodb.Attribute(
                name="user_id",
                type=dynamodb.AttributeType.STRING
            )
        )

        cause_table = dynamodb.Table(
            self, "charitychamps-causes",
            self, "charitychamps-cause",
            table_name="charitychamps-cause",
            partition_key=dynamodb.Attribute(
                name="cause_id",
                type=dynamodb.AttributeType.STRING
            )
        )

        citiy_table = dynamodb.Table(
            self, "charitychamps-cities",
            table_name="charitychamps-cities",

            partition_key=dynamodb.Attribute(
                name="city_id",
                type=dynamodb.AttributeType.STRING
            )
        )

        user_cause_table = dynamodb.Table(
            self, "charitychamps-user-cause",
            table_name="charitychamps-user-cause",
            partition_key=dynamodb.Attribute(
                name="user_id",
                type=dynamodb.AttributeType.STRING
            ),
            sort_key=dynamodb.Attribute(
                name="cause_id",
                type=dynamodb.AttributeType.STRING
            )
        )

        category_table = dynamodb.Table(
            self, "charitychamps-categories",
            table_name="charitychamps-categories",
            partition_key=dynamodb.Attribute(
                name="category_id",
                type=dynamodb.AttributeType.STRING
            )
        )

        api = apigw.RestApi(
            self, "charitychamps-api",
            rest_api_name="CharityChamps API",
            default_cors_preflight_options=apigw.CorsOptions(
                allow_origins=apigw.Cors.ALL_ORIGINS,
                allow_methods=apigw.Cors.ALL_METHODS
            )
        )

        users_endpoint = api.root.add_resource("users")  # get
        user_endpoint = api.root.add_resource("user")
        user_id_endpoint = user_endpoint.add_resource("{id}")  # post get
        filters_endpoint = api.root.add_resource("filters")  # get post
        causes_endpoint = api.root.add_resource("causes")  # get
        causes_id_endpoint = causes_endpoint.add_resource("{id}")  # post get
        my_causes_endpoint = api.root.add_resource("myCauses")  # get delete
        my_causes_id_endpoint = my_causes_endpoint.add_resource("{id}")
        volunteered_causes_endpoint = api.root.add_resource(
            "volunteeredCauses")
        volunteered_causes_id_endpoint = volunteered_causes_endpoint.add_resource(
            "{id}")  # delete get post

        get_users_lambda = _lambda.Function(
            self, "get_users_lambda",
            runtime=_lambda.Runtime.PYTHON_3_10,
            handler="get_users.handler",
            code=_lambda.Code.asset("lambda"),
        )

        users_endpoint.add_method(
            "GET", apigw.LambdaIntegration(get_users_lambda))
