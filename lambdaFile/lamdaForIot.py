
const config = {};
config.IOT_BROKER_ENDPOINT      = "xxxxxxxx";  
config.IOT_BROKER_REGION        = "us-east-1"; 
config.IOT_THING_NAME           = "name";

const SkillMessagesUS = {
    'welcome'       :'welcome.  you can say please start my demo',
    'topicresponse'  :'you asked for',
    'help'          :'you can open demos of devOps, I A C , Scalr, Serverless.',
    'cancel'        :'goodbye',
    'stop'          :'goodbye'
};

const SkillMessagesDE = {
    'welcome'       :'hallo.  sagen so was, reisen nach london oder reisen nach berlin',
    'topicresponse'  :'sie haben gefragt',
    'help'          :'sagen so was, reisen nach london oder reisen nach berlin',
    'cancel'        :'auf wiedersehen',
    'stop'          :'auf wiedersehen'
};

// 2. Skill Code =======================================================================================================


const Alexa = require('alexa-sdk');
var SkillMessages = {};

exports.handler = function(event, context, callback) {
    



       //config.IOT_THING_NAME           = event.inventname;

        newState = {'topic':event.name};

        updateShadow(newState, status => {
            
            console.log("success");
        });

    
};  
//    END of Intent Handlers {} ========================================================================================
// 3. Helper Function  =================================================================================================


function updateShadow(desiredState, callback) {
    // update AWS IOT thing shadow
    var AWS = require('aws-sdk');
    AWS.config.region = config.IOT_BROKER_REGION;

    //Prepare the parameters of the update call

    var paramsUpdate = {
        "thingName" : config.IOT_THING_NAME,
        "payload" : JSON.stringify(
            { "state":
                { "desired": desiredState          // {"pump":1}
                }
            }
        )
    };

    var iotData = new AWS.IotData({endpoint: config.IOT_BROKER_ENDPOINT});

    iotData.updateThingShadow(paramsUpdate, function(err, data)  {
        if (err){
            console.log(err);

            callback("not ok");
        }
        else {
            console.log("updated thing shadow " + config.IOT_THING_NAME + ' to state ' + paramsUpdate.payload);
            callback("ok");
        }

    });

}

