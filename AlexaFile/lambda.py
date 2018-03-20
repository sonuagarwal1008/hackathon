import urllib2
import json
import boto3
import os
import commands
import time
import decimal
import datetime
import collections
from random import randint
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
#from language_strings import get_message 

##########################################
#
# Global default settings
#
##########################################
#parameter_name : skill_name
#description : Defines skill name to be announced in Welcome message
#sample_definition : skill_name = "A W S Manager"
skill_name = ""


##########################################
#
# Main lambda handler
#
##########################################

def lambda_handler(event, context):
    
    # To restrict access of this Lambda function from sepecific Alexa applications
    # add alexa skill id below and uncomment the section
    #if (event["session"]["application"]["applicationId"] !=
    #        "amzn1.ask.skill.f6599869-0e99-4d22-8922-adbc95c42773"):
    #    raise ValueError("Invalid Application ID")


    if event["session"]["new"]:
        event["session"]["attributes"] = {}
        on_session_started({"requestId": event["request"]["requestId"]}, event["session"])

    if event["request"]["type"] == "LaunchRequest":
        return on_launch(event["request"], event["session"])
    elif event["request"]["type"] == "IntentRequest":
        return on_intent(event["request"], event["session"])
    elif event["request"]["type"] == "SessionEndedRequest":
        return on_session_ended(event["request"], event["session"])



    
##################################################################################
#
# Functions handling the events
#
##################################################################################

def on_session_started(session_started_request, session):
    print "Starting new session."
    


def on_launch(launch_request, session):
    return get_welcome_response(session)
    

def on_intent(intent_request, session):
    intent = intent_request["intent"]
    intent_name = intent_request["intent"]["name"]
    if intent_name == "askdetails":
        return intent_ask_details(intent, session)
    elif intent_name == "currentissue":
        return intent_current_issue(intent, session)
    elif intent_name == "ClosingIntent":
        return intent_closing(intent, session)
    elif intent_name == "AMAZON.YesIntent" or intent_name == "everythingelse":
        return intent_response_yes(intent, session)
    elif intent_name == "AMAZON.NoIntent":
        return intent_response_no(intent, session)
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        return unrecognized_intent(session)


def on_session_ended(session_ended_request, session):
    print "Ending session."
    # Cleanup goes here...
    session['attributes'] ={}
    card_title = "ending session"
    speech_output = "now closing the session"
    reprompt_text = "closing the session"
    should_end_session = True
    
    
    
    return build_response(session['attributes'], build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))
    




##################################################################################
#
# Functions directly called from functions handling the events
#
##################################################################################

def get_welcome_response(session):
    #This function is triggered on skill launch only
    #Add Welcome message here
    
    session['attributes'] = {}
    current_multi_action_task = "welcome"
    current_step = "welcome"
    session['attributes']['current_multi_action_task'] = current_multi_action_task
    session['attributes']['current_step'] = current_step
    
    parameters = []
    message = get_message(current_step,parameters, session)
    
    card_title = message['card_title']
    should_end_session = False
    
    # Function variables
    userid = session["user"]["userId"]
    
    # temporary debug code
    print "printing userId"
    print userid
    
    try:
        speech_output = message['speech_output']
        reprompt_text = message['reprompt_text']
    except:
        speech_output = "please provide valid input"
        reprompt_text = ""
        
    return build_response(session['attributes'], build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))



##################################################################################
#
# Functions handling the user Intents
#
##################################################################################
def intent_ask_details(intent, session):
    #Provide description of the function here
    
    if "current_multi_action_task" in session['attributes']:
        previous_multi_action_task = session['attributes']['current_multi_action_task']
        previous_step = session['attributes']['current_step']
    current_multi_action_task = "ask_details"
    current_step = "ask_details"
    session['attributes']['current_multi_action_task'] = current_multi_action_task
    session['attributes']['current_step'] = current_step
    
    parameters = []
   
            
    
    
    card_title = ""
    should_end_session = False 
    try:
        #Your code here
        incidentCount = query_dynamodb_get_count()
        speech_output = "I found out "+str(incidentCount)+" incident in your database till date."
        reprompt_text =  ""
        
    except:
        speech_output = "Sorry, please could you say again?"
        reprompt_text = "Please can you repeat?"

    return build_response(session['attributes'], build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))

def handle_session_end_request():
    card_title = "Alexa skill by TCS GTP - Agile Computing CoE"
    speech_output = "Thank you for using the women's safty app See you next time!"
    should_end_session = True

    return build_response({}, build_speechlet_response(card_title, speech_output, None, should_end_session))


def intent_current_issue(intent, session):
    #Provide description of the function here
    
    if "current_multi_action_task" in session['attributes']:
        previous_multi_action_task = session['attributes']['current_multi_action_task']
        previous_step = session['attributes']['current_step']
    current_multi_action_task = "get_infra_health"
    current_step = "current_issue"
    session['attributes']['current_multi_action_task'] = current_multi_action_task
    session['attributes']['current_step'] = current_step
    
    parameters = []
    message = get_message(current_step,parameters, session)
    
    card_title = message['card_title']
    should_end_session = False 
    try:
        #Your code here
        speech_output = message['speech_output']
        reprompt_text = message['reprompt_text']
    except:
        speech_output = "Sorry, please could you say again?"
        reprompt_text = "Please can you repeat?"

    return build_response(session['attributes'], build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))

	###############################



def intent_response_yes(intent,session):
    #Provide description of the function here
    
    if "current_multi_action_task" in session['attributes']:
        previous_multi_action_task = session['attributes']['current_multi_action_task']
        previous_step = session['attributes']['current_step']


    parameters = {}
    try:
        #Your code here
        
        
        message =get_message("help", parameters,session)
        card_title = message['card_title']
        speech_output = message['speech_output']
        reprompt_text = message['reprompt_text']
        should_end_session = False
    except:
        speech_output = "Sorry, please could you say again?"
        reprompt_text = "Please can you repeat?"

    return build_response(session['attributes'], build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def intent_response_no(intent,session):
    #Provide description of the function here
    
    if "current_multi_action_task" in session['attributes']:
        previous_multi_action_task = session['attributes']['current_multi_action_task']
        previous_step = session['attributes']['current_step']
    current_multi_action_task = session['attributes']['current_multi_action_task']
    current_step = "NoIntent"
    session['attributes']['current_multi_action_task'] = current_multi_action_task
    session['attributes']['current_step'] = current_step

    parameters = {}
    try:
        #Your code here
        if previous_step == "get_order_to_delivery_status" or previous_step == "ack_order_status":
            message = get_message(current_step, parameters)
            card_title = message['card_title']
            speech_output = message['speech_output']
            reprompt_text = message['reprompt_text']
            should_end_session = True
            demo_name = session['attributes']['demo_name']
        elif previous_step == "faq":
            current_multi_action_task = "faq"
            current_step = "faq_no"
            session['attributes']['current_multi_action_task'] = current_multi_action_task
            session['attributes']['current_step'] = current_step
            message = get_message(current_step, parameters)
            
            card_title = message['card_title']
            speech_output = message['speech_output']
            reprompt_text = message['reprompt_text']
            should_end_session = True
        else:
            message =get_message("YesNoErrorHandling", parameters)
            card_title = message['card_title']
            speech_output = message['speech_output']
            reprompt_text = message['reprompt_text']
            should_end_session = False
    except:
        speech_output = "Sorry, please could you say again?"
        reprompt_text = "Please can you repeat?"

    return build_response(session['attributes'], build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


	
def unrecognized_intent(session):

    if "current_multi_action_task" in session['attributes']:
        previous_multi_action_task = session['attributes']['current_multi_action_task']
        previous_step = session['attributes']['current_step']
    current_multi_action_task = "unrecognized"
    current_step = "unrecognized"
    session['attributes']['current_multi_action_task'] = current_multi_action_task
    session['attributes']['current_step'] = current_step
    if "unrecognized_retries" in session['attributes']:
        unrecognized_retries = session['attributes']['unrecognized_retries'] + 1
    else:
        unrecognized_retries = 1
        session['attributes']['unrecognized_retries'] = unrecognized_retries

    if unrecognized_retries >= 2:
        should_end_session = True
        speech_output = "Sorry, this feature is not available at the moment. You can try using the skill with the supported features" 
        reprompt_text = ""
    else:
        should_end_session = False
        speech_output = "Sorry, this feature is not available at the moment." 
        reprompt_text = ""
    #parameters = {}
    #message = get_message(current_step,parameters, session)
    card_title = ""

    return build_response(session['attributes'], build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def intent_closing(intent,session):
    #Provide description of the function here
    
    if "current_multi_action_task" in session['attributes']:
        previous_multi_action_task = session['attributes']['current_multi_action_task']
        previous_step = session['attributes']['current_step']
    current_multi_action_task = "closing"
    current_step = "closing"
    session['attributes']['current_multi_action_task'] = current_multi_action_task
    session['attributes']['current_step'] = current_step
    
    parameters = []
    message = get_message(current_step,parameters, session)
    
    card_title = message['card_title']
    should_end_session = True
    try:
        #Your code here
        speech_output = message['speech_output']
        reprompt_text = message['reprompt_text']
    except:
        speech_output = "Sorry, please could you say again?"
        reprompt_text = "Please can you repeat?"

    return build_response(session['attributes'], build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))



	

##################################################################################
#
# Supporting functions
#
##################################################################################

#def lambda_invocation(demo_name):
#    print "Inside Lambda invocation"
#    payload = '{"name": "' + demo_name + '"}'
#    client = boto3.client('lambda')
#    response = client.invoke(

#    InvocationType='Event',
#    Payload = payload
#    #LogType='Tail',
#    )

def current_timestamp():
    #This function returns current timestamp as a string
                    
    currenttime = time.time()
    int_currenttime = int(currenttime)
    string_currenttime = "%.0f" % int_currenttime
    
    return string_currenttime
    
    

def query_dynamodb_item(dytable,dykey,dyvalue):
    #This function takes DynamoDB tablename, key and value and item to query against and returns the count from query response
    keyexpr = dykey + " = :check_key"
    dynamodb_client = boto3.client('dynamodb', region_name=region)
    result = dynamodb_client.query(
    ExpressionAttributeValues={
        ':check_key': {
            'S': dyvalue,
        },
    },
    KeyConditionExpression=keyexpr,
    TableName=dytable,
    )
    #print "printing result"
    #print result
    count = result['Count']
        
    return count
    
    
    
    
def query_dynamodb_get_count():
    #This function takes DynamoDB tablename, key and value and item to query against and returns the count from query response
    dynamodb_client = boto3.client('dynamodb', region_name='us-east-1')
    response = dynamodb_client.scan(
    TableName='S_report',

    AttributesToGet=[
        'appid',
    ],
        Select='SPECIFIC_ATTRIBUTES'
    )
    return response['Count']
    
    
def get_dynamodb_item(dytable,dykey,dyvalue):
    #This function takes DynamoDB tablename, key and value to query against and returns the query response
    dynamodb = boto3.resource('dynamodb', region_name=region)
    table = dynamodb.Table(dytable)

    try:
        response = table.get_item(
            Key={
                dykey: dyvalue
            }
        )
    except ClientError as e:
        print e.response['Error']['Message']
    else:
        #debug info
        print "printing response from dynamodb get item"
        print response
        item = response['Item']
    return item

    
def put_dynamodb_item(dytable,dyitem):
    #This function takes DynamoDB table name, and item value and updates into the specified DynamoDB table
    dynamodb = boto3.resource('dynamodb', region_name=region)
    table = dynamodb.Table(dytable)
    
    response = table.put_item(
        Item=dyitem
    )

    return 'Item updated'
    
def lambda_invocation(demo_name):
    print "Inside Lambda invocation"
    thingname = 'invent5'
    payload = '{"name": "' + demo_name + '"}'
    client = boto3.client('lambda')
    response = client.invoke(
    FunctionName='arn:aws:lambda:us-east-1:xxxxxxxxx',
    InvocationType='Event',
    Payload = payload
    #LogType='Tail',
    )
    
    
def reset_session_attributes(session):
    #This function resets all the session attributes
    
    # WIP
    # Need to revisit this function to see if we have better way to define which attributes to
    # reset or maybe rather reset all attributes

    session['attributes']['current_multi_action_task'] = "nointent"
    session['attributes']['task_inputs'] = {}
                
    return session
    

def save_session(session):
    #This function saves the current intent, session info into DynamoDB
    print "Inside save_session function"
    
    # Function predefined variables
    userid = session["user"]["userId"]
    session_attributes = session['attributes']
    
    #debug info
    print "printing session details as received"
    print session

    count = query_dynamodb_item(session_dynamodb_table_name,"userid",userid)
    if count != 0:
        print "query dynamodb returned non zero count"
        item = get_dynamodb_item(session_dynamodb_table_name,"userid",userid)
        print "printing item returned from dynamodb get item"
        print item
        item['session_attributes'] = session['attributes']
        put_dynamodb_item(session_dynamodb_table_name,item)
    else:
        print "query dynamodb returned count 0"
    
    return 'Updated DynamoDB'


def get_message(label, parameters, session):
    speech_labels = {
 	"use_case": {
 		"userspeech": {
 			"welcome": {
 				"speech_output": "Welcome, How may i help you today.",
 				"reprompt_text": "You can ask for total incident and today's incident.",
 				"card_title": ""
 			
 			
 			
 			"YesIntent": {
 				"description": "yes",
 				"speech_output": "Okay, ",
 				"reprompt_text": "",
 				"card_title": ""
 			},
 			"NoIntent": {
 				"description": "no",
 				"speech_output": "ok, have a nice day ",
 				"reprompt_text": "",
 				"card_title": ""
 			},
 			"faq": {
 				"description": "f a q",
 				"speech_output": "",
 				"reprompt_text": "you can say repeat if you want me to repeat",
 				"card_title": ""
 			},
 			"help": {
 				"description": "help",
 				"speech_output": "I am afraid, I can not access this information. Please can you repeat your end.",
 				"reprompt_text": "",
 				"card_title": ""
 			},

 			"closing": {
 				"description": "closing",
 				"speech_output": "It was my pleasure interacting with you. have a good day ahead!",
 				"reprompt_text": "",
 				"card_title": ""
 			}
 		}
 	}
 }
    
    
    unsupported_speech = {
            				"description": "unsupported",
            				"speech_output": "Sorry I can't understand you",
            				"reprompt_text": "",
            				"card_title": ""
    }
    
    message = speech_labels['use_case']
#    demoType = message.keys()
    
    if label == 'welcome':           
        speech_output = message['userspeech']['welcome']['speech_output']
        reprompt_text = message['userspeech']['welcome']['reprompt_text']
        return_message = { 
							"speech_output": speech_output, 
							"reprompt_text": reprompt_text, 
							"card_title": "", 
							"current_multi_action_task": "", 
							"current_step": "" 
						}
        return return_message
        
    
        
    
    elif label == 'YesIntent':           
        speech_output = message['userspeech']['welcome']['speech_output']
        reprompt_text = message['userspeech']['welcome']['reprompt_text']
        return_message = { 
							"speech_output": speech_output, 
							"reprompt_text": reprompt_text, 
							"card_title": "", 
							"current_multi_action_task": "", 
							"current_step": "" 
						}
        return return_message
    elif label == 'NoIntent':           
        speech_output = message['userspeech']['welcome']['speech_output']
        reprompt_text = message['userspeech']['welcome']['reprompt_text']
        return_message = { 
							"speech_output": speech_output, 
							"reprompt_text": reprompt_text, 
							"card_title": "", 
							"current_multi_action_task": "", 
							"current_step": "" 
						}
        return return_message
    elif label == 'faq':           
        speech_output = message['userspeech']['faq']['speech_output']
        reprompt_text = message['userspeech']['faq']['reprompt_text']
        return_message = { 
							"speech_output": speech_output, 
							"reprompt_text": reprompt_text, 
							"card_title": "", 
							"current_multi_action_task": "", 
							"current_step": "" 
						}
        return return_message
    elif label == 'help':           
        speech_output = message['userspeech']['help']['speech_output']
        reprompt_text = message['userspeech']['help']['reprompt_text']
        return_message = { 
							"speech_output": speech_output, 
							"reprompt_text": reprompt_text, 
							"card_title": "", 
							"current_multi_action_task": "", 
							"current_step": "" 
						}
        return return_message
    elif label == 'closing':
        print "inside closing"
        print message['userspeech']
        speech_output = message['userspeech']['closing']['speech_output']
        reprompt_text = message['userspeech']['closing']['reprompt_text']
        return_message = { 
							"speech_output": speech_output, 
							"reprompt_text": reprompt_text, 
							"card_title": "", 
							"current_multi_action_task": "", 
							"current_step": "" 
						}
        return return_message
    else:
        return_message = unsupported_speech
        return return_message
        
        
        
  
def build_response(session_attributes, speechlet_response):
    #This function returns the response from chatbot to user
    
    return {
        "version": "1.0",
        "sessionAttributes": session_attributes,
        "response": speechlet_response
    }     


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    #This function builds the speech response from chatbot to user
    
    return {
        "outputSpeech": {
            "type": "PlainText",
            "text": output
        },
        "card": {
            "type": "Simple",
            "title": title,
            "content": output
        },
        "reprompt": {
            "outputSpeech": {
                "type": "PlainText",
                "text": reprompt_text
            }
        },
        "shouldEndSession": should_end_session
    }
