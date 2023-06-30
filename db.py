# Use this code snippet in your app.
# If you need more information about configurationsbot
# or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developer/language/python/

import boto3
import json
from botocore.exceptions import ClientError


def get_secret():

    secret_name = "docker-mysql-prac"
    region_name = "ap-northeast-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']

    env_file = '.env'

    with open(env_file, "w") as f:
            for key, value in secret.items():
                f.write(f"{key}={value}\n")

    return json.loads(secret)

    # Your code goes here.


secrets = get_secret()

print("username", secrets["username"])
print("password", secrets["password"])