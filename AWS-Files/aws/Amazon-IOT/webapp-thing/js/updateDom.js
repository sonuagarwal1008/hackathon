// Customize how the browser will display the contents of Thing update messages received
//

function handleMessage(msg) {  // called from within connectAsThing.js
     // display the JSON message in a panel
    document.getElementById('panel').innerHTML = msg;

    // unpack the message and find the city value.  Pop a child browser window to display images.
    var valuefromendpoint = JSON.parse(msg).topic;
   
    
    var ImgUrl = "http://127.0.0.1/help.html";
    pop(ImgUrl);

   
    

}
function reloader() {
    location.reload(true);  // hard reload including .js and .css files

}

var childWindow;

function pop(url) {
    console.log('Opening child url ' + url);

    if (childWindow) {
        childWindow.location = url;
    } else {

        childWindow = window.open(
            url,
            'mychild',
            'height=1300,width=1500,titlebar=yes,toolbar=no,menubar=no,directories=no,status=no,location=yes,title=new'
        );
    }
}   
