import boto3
import json
#import urllib.request
from urllib2 import Request, urlopen, URLError, HTTPError
import string

def lambda_handler(event, context):
    # TODO implement
    #print "Printing event information"
    #print event
    GOOGLE_MAPS_KEY = ""
    if event['Records'][0]['eventName'] == 'INSERT':
        record = event['Records'][0]['dynamodb']['NewImage']
        location = get_location(record)
        print "appid is " +location['appid']
        print "latitude is " +location['latitude']
        print "longitude is " +location['longitude']
        #print "App id " +location['appid']+ " requested for help. The victim is located at latitude " +location['latitude']+ " and longitude " +location['longitude']
        get_dynamodb_entries(location)
    
    return 'Hello from Lambda'


def get_location(record):
        appid = record['appid']['S']
        latitude = record['latitude']['S']
        longitude = record['longitude']['S']
        
        #print "appid is " +appid
        #print "latitude is " +latitude
        #print "longitude is " +longitude
        
        location = {
            "appid" : appid,
            "latitude" : latitude,
            "longitude" : longitude
        }
        
        return location


def get_dynamodb_entries(location):
    region = 'us-east-1'
    victim_appid = location['appid']
    victim_latitude = location['latitude']
    victim_longitude = location['longitude']
    dynamodb_client = boto3.client('dynamodb', region_name=region)
    result = dynamodb_client.scan(
            TableName = 'S_registration_data',
            Select = 'ALL_ATTRIBUTES'
        )
    
    sns_client = boto3.client('sns')
    resp = sns_client.set_sms_attributes(attributes={'DefaultSMSType': 'Transactional'})
    
        
    
    print "Checking " +str(len(result['Items']))+ " entries"
    for i in range(0,len(result['Items']),1):
        #print "printing next entry"
        #print result['Items']
        user_appid = result['Items'][i]['appid']['S']
        user_latitude = result['Items'][i]['latitude']['S']
        user_longitude = result['Items'][i]['longitude']['S']
        
        #print user_appid
        #print user_latitude
        #print user_longitude
        
        url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=' +victim_latitude+ ',' +victim_longitude+ '&destinations=' +user_latitude+ ',' +user_longitude+ '&key='+GOOGLE_MAPS_KEY
        req = Request(url)
        response1 = urlopen(req)
        response2 = response1.read()
        response3 = json.loads(response2)
        distance = response3['rows'][0]['elements'][0]['distance']['text'] #['destination_addresses'][0]
        #print distance
        victim_google_map_url = "http://maps.google.com/maps?q="+victim_latitude+","+victim_longitude
        msg = "Alert!!! There is an SOS help request from a person at location " +victim_google_map_url+ ". You had registered to be notified"

        if "km" in distance:
            distance_number = float(string.replace(distance," km",""))
            if distance_number < 2.0:
                print "The distance in kilometers is " +str(distance_number)
                print "send message to " +user_appid
                user_mobile = result['Items'][i]['user_mobile']['S']
                print "Sending message to " +user_appid+ " on number " +user_mobile
                sns_client.publish(PhoneNumber=user_mobile,Message=msg)
        else:
            print "The distance in meters is " +distance
            print "send message to " +user_appid
            user_mobile = result['Items'][i]['user_mobile']['S']
            print "Sending message to " +user_appid+ " on number " +user_mobile
            sns_client.publish(PhoneNumber=user_mobile,Message=msg)
