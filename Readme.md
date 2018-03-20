#### Requirement points:

1. Ubuntu 16.04 server
2. One AWS account 
3. Alexa developer console

#### Access keys requirements
1. Generate Access key and secret key using aws iam console.
2. Generate google maps api key

### Cloud services that we are going to use
1. AWS lambda(For serverless compute)
2. AWS dynamo DB(for NoSQL database service)
3. AWS SNS service(for messaging and notification service)
4. S3(for static data files storage)
5. AWS IOT endpoint (using mqtt and iot endpoint transmitting data to police control dasgboard)

#### Machine learning, NLP,NLU use
1. For user speech and emotion analysis using tensorflow




####Softwares needs to be installed on server
1. setup virtual environement for python
2. apt-get install awscli
3. pip install boto3
4. pip install flask
5. pip install boto3
6. pip install pytz
7. pip install requests

###configure  aws credentials
execute command 'aws configure'
AWS Access Key ID [****************L4WQ]:  AWS_ACCESS_ID
AWS Secret Access Key [****************YXwd]: AWS_SECRET_KEY
Default region name [us-east-1]: REGION_NAME
Default output format [json]: JSON

######lambda functions
Hackathon-Git-Data/AlexaFile/lambda.py
Hackathon-Git-Data/AlexaFile/
##### flask configuration and setup

#####Alexa configuration and setup
After setting up alexa developer account use following option:
1. create alexa skill and copy-paste json data(it contains user utterances and intents) which is located at Hackathon-Git-Data/AlexaFile/speech.json
2. Paste lamnda code in lambda editor Hackathon-Git-Data/AlexaFile/lambda.py








