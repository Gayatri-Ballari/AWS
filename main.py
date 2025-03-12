import json
import boto3
from botocore.exceptions import ClientError


# Load the JSON file
with open("aws_credentials.json", "r", encoding="utf-8-sig") as file:
    data = file.read()  # Read the file content
    credentials = json.loads(data) 

# Extract credentials
aws_access_key_id = credentials["aws_access_key_id"]
aws_secret_access_key = credentials["aws_secret_access_key"]

# Initialize the Bedrock client with the credentials
client = boto3.client(
    service_name='bedrock-runtime',
    region_name='ap-south-1',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)
input_data = {
 "modelId": "meta.llama3-8b-instruct-v1:0",
 "contentType": "application/json",
 "accept": "application/json",
 "body": "{\"prompt\":\"where is kerala\",\"max_gen_len\":512,\"temperature\":0.5,\"top_p\":0.9}"
}
response = client.invoke_model(contentType='application/json', body=input_data['body'], modelId=input_data['modelId'])

Data = json.loads(response['body'].read().decode('utf-8'))
print(Data)