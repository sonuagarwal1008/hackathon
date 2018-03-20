import boto3
dynamodb_client = boto3.client('dynamodb', region_name='us-east-1')
response = dynamodb_client.scan(
    TableName='S_registration_data',
    
    AttributesToGet=[
        'id',
    ],
	Select='SPECIFIC_ATTRIBUTES'
)
inp =[]
for i in range(0,response['Count'],1):
	inp.append(response['Items'][i]['id']['N'])

print max(inp)
	
print response

