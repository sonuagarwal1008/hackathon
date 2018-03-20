import boto3
import pytz
from random import randint
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
	name = request.form['name']
	username = request.form['username']
	password = request.form['password']
	country = request.form['country'] 
	state = request.form['state']
	city  = request.form['city']
	zipcode = int(request.form['zip'])
	user_mobile = request.form['mobile']
	numbers = [randint(0, 9) for _ in range(5)]
	#session['attributes']['otp'] = [9,0,2,8,0]
	num = ''
	for i in numbers:
	    num=num+str(i)
	msg = "your otp for alexa service is "+num
	client = boto3.client('sns')
	resp = client.set_sms_attributes(attributes={'DefaultSMSType': 'Transactional'})
	client.publish(PhoneNumber='+918696126602',Message=msg)
	client.publish(PhoneNumber='+919587337602',Message=msg)
	

	dynamodb_otp = boto3.resource('dynamodb', region_name='us-east-1')
	table_otp = dynamodb_otp.Table('S_otp')
	response_otp = table_otp.put_item(
	   Item={

		        'otp': num
			



		}
	)
	######    dynamodb for registration data ####
	dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

	table = dynamodb.Table('S_registration_data')
	
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
		inp.append(int(response['Items'][i]['id']['N']))

	print max(inp)


	response = table.put_item(
	   Item={
			'id': int(max(inp))+1,
			'appid': "irj-"+str(int(max(inp))+1),
			'name': name,
			'password': password,
			'country': country,
			'state': state,
			'city': city,
			'latitude': "27.0",
			'longitude': "80.0",
			'user_mobile': "+91"+user_mobile,
			'username': username,
			'zipcode': zipcode,
			'demo_desc': "demo_entry"
			
			
		}
	)
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            #error = 'Please verify with your OTP number.'
	    return redirect(url_for('otp'))
        else:
            return redirect(url_for('/'))
    return render_template('login.html', error=error)
@app.route("/help", methods=['GET', 'POST'])
def help():
    error =None
    latitude=26.887594
    longitude=75.813964
    appid="irj-99"
    tz = pytz.timezone('Asia/Kolkata')
    currenttime = str(datetime.now(tz))
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('S_report')
    response = table.put_item(
           Item={
                        
                        'appid': "irj-3",
                        'latitude': "26.887594",
			'longitude': "75.813964",
			'time': currenttime
                        
                        


                }
        )
#    if request.form['username'] != 'admin' or request.form['password'] != 'admin':
 #           error = 'Location details sent successfully.'
  #  else:
   #         return redirect(url_for('/'))
     
    return render_template('help.html', error=error)
@app.route("/otp", methods=['GET', 'POST'])
def otp():
    error =None
    msg =None
    if request.method == 'POST':
        receiveotp = request.form['otp']
    	dynamodb_client = boto3.client('dynamodb', region_name='us-east-1')
    	response = dynamodb_client.scan(
    	TableName='S_otp',

    	AttributesToGet=[
		'otp',
    	],
        Select='SPECIFIC_ATTRIBUTES'
    	)
    	otpvalue = []
    	for i in range(0,int(response['Count']),1):
        	otpvalue.append(str(response['Items'][i]['otp']['S']))
    	if receiveotp in otpvalue:
	    msg = "you have been registered successfully"
	else:
	    msg = "please enter a valid otp."
#    if request.form['username'] != 'admin' or request.form['password'] != 'admin':
 #           error = 'Location details sent successfully.'
  #  else:
   #         return redirect(url_for('/'))

    return render_template('otp.html', error=msg)
if __name__ == "__main__":
    app.run(host='10.128.0.2')
