import fileinput
import sys
import time

####test data######## live data we will be fetching from s3 and dynamodb
a= {
"victim": {
        "lat": 26.878788,
        "log": 75.808685
},
"police": {
        "lat": 26.896623,
        "log": 75.662036
},
"user1": {
        "lat": 26.944209,
        "log": 75.722763
},
"user2": {
        "lat": 26.896623,
        "log": 75.662036
},
"drone1": {
        "lat": 26.896623,
        "log": 75.642036
},
"drone2": {
        "lat": 26.896623,  
        "log": 75.662036
}         
}        
poliaddlat =a['police']['lat']
poliaddlog=a['police']['log'] 
drone1addlat = a['drone1']['lat']
drone1addlog = a['drone1']['log']
drone2addlat = a['drone2']['lat']
drone2addlog = a['drone2']['log']
user1addlat = a['user1']['lat']
user1addlog = a['user1']['log']
user2addlat = a['user2']['lat']
user2addlog = a['user2']['log']

def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line) 
		
		
polilatdiff = (a['victim']['lat']-a['police']['lat'])/10
polilogdiff =(a['victim']['log']-a['police']['log'])/10
drone1latdiff = (a['victim']['lat']-a['drone1']['lat'])/10
drone1logdiff =(a['victim']['log']-a['drone1']['log'])/10
drone2latdiff = (a['victim']['lat']-a['drone2']['lat'])/10
drone2logdiff =(a['victim']['log']-a['drone2']['log'])/10
user1latdiff = (a['victim']['lat']-a['user1']['lat'])/10
user1logdiff =(a['victim']['log']-a['user1']['log'])/10
user2latdiff = (a['victim']['lat']-a['user2']['lat'])/10
user2logdiff =(a['victim']['log']-a['user2']['log'])/10
#for i in range(0,10,1): 
#        #latdiff = (a['victim']['lat']-a['police']['lat'])/10
        #logdiff =(a['victim']['log']-a['police']['log'])/10
        #policelat = a['police']['lat'] 
 #       addlat = addlat+latdiff
  #      addlog=addlog+logdiff
   #     replacestringlat = "policelat: "+str(addlat)+",//"
count = 30
dronecount=0
user1count=0
user2count=0
policecount=0

for i in range(0,count,1): 
	time.sleep(9)
			
		
	if policecount % 3 == 0 and policecount < 30:
			###p data
			polilatdiff = (a['victim']['lat']-a['police']['lat'])/10
			polilogdiff =(a['victim']['log']-a['police']['log'])/10
			#policelat = a['police']['lat'] 
			poliaddlat = poliaddlat+polilatdiff
			poliaddlog=poliaddlog+polilogdiff
			polireplacestringlat = "policelat: "+str(poliaddlat)+",//"
			polireplacestringlog = "policelong: "+str(poliaddlog)+"//"
			replaceAll("/var/www/html/map-script.js","policelat:",polireplacestringlat)
			replaceAll("/var/www/html/map-script.js","policelong:",polireplacestringlog)
	if dronecount < 10:
		
		##drone1 data
		drone1addlat = drone1addlat+drone1latdiff
		drone1addlog=drone1addlog+drone1logdiff
		drone1replacestringlat = "drone1lat: "+str(drone1addlat)+",//"
		drone1replacestringlog = "drone1long: "+str(drone1addlog)+"//"
		replaceAll("/var/www/html/map-script.js","drone1lat:",drone1replacestringlat)
		replaceAll("/var/www/html/map-script.js","drone1long:",drone1replacestringlog)
		## drone2 data
		drone2addlat = drone2addlat+drone2latdiff
		drone2addlog=drone2addlog+drone2logdiff
		drone2replacestringlat = "drone2lat: "+str(drone2addlat)+",//"
		drone2replacestringlog = "drone2long: "+str(drone2addlog)+"//"
		replaceAll("/var/www/html/map-script.js","drone2lat:",drone2replacestringlat)
		replaceAll("/var/www/html/map-script.js","drone2long:",drone2replacestringlog)
	if user1count % 2 == 0 and user1count < 20:
		##user1 data
		user1addlat = user1addlat+user1latdiff
		user1addlog=user1addlog+user1logdiff
		user1replacestringlat = "user1lat: "+str(user1addlat)+",//"
		user1replacestringlog = "user1long: "+str(user1addlog)+"//"
		replaceAll("/var/www/html/map-script.js","user1lat:",user1replacestringlat)
		replaceAll("/var/www/html/map-script.js","user1long:",user1replacestringlog)
## user2 data
#	user2addlat = user2addlat+user2latdiff
#    user2addlog=user2addlog+luser2ogdiff
#    user2replacestringlat = "user2lat: "+str(user2addlat)+",//"
#    user2replacestringlog = "user2long: "+str(user2addlog)+"//"
#	replaceAll("/var/www/html/map-script.js","user2lat:",user2replacestringlat)
#	replaceAll("/var/www/html/map-script.js","user2long:",user2replacestringlog)
	
	dronecount += 1
	user1count += 2
	policecount += 3
		

		
		
