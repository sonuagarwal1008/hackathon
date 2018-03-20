SetUp AWS IOT and AWS Cognito Point and Script:

Use case is:
It will automatically open police console and highlight the entry and highlights user latitude and longitude:

File that needs to be edited:
1. 'aws_iot.js':  
 	location: Hackathon-Git-Data/AWS-Files/aws/Amazon-IOT/webapp-thing/js
	
#### Steps

Create a new AWS Cognito Identity Pool

1. Login to the AWS Cognito console
1. Click the second blue button called "Manage Federated Identities"
1. Click "Create new identity pool"
  + Check the box to "Enable access to unauthenticated providers"
1. The next page states "Your Cognito identites require access to your resources."  This is fine, just click the blue "Allow" button to continue.
  + Two new empty IAM roles are created for you, called ```Cognito_MyPoolAuth_Role``` and ```Cognito_MyPoolUnauth_Role```.
1. Once your pool is created, click on the "Sample Code" menu item
1. Within your code, find the RED string called Identity Pool ID and record this as your IdentityPoolId.

Add permissions to users of your Identity Pool:
1. Go to the AWS IAM Console
1. Click Roles
1. Click on the new Unauth role, such as Cognito_MyPoolUnauth_Role
1. Click the "Attach Policy" button to add the appropriate permissions to your role
1. For the IOT webapp, choose ```AWSIoTDataAccess``` or define a specific set of permissions.

Apply all settings:
1. Open the Amazon-IOT/webapp-thing/js folder and locate the file ```aws_config.js```
1. Modify the fields labeled REGION and mqttEndpoint and IdentityPoolId

#### Launch the page



 + Open in the page thing1.html in your favorite browser(Hackathon-Git-Data/AWS-Files/aws/Amazon-IOT/webapp-thing/thing1.html).
   + You can open the page right from within your project folder, you do not need to host it on a website.
 + The page should display with a green status label saying "CONNECTED"



 
