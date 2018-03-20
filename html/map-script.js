function initMap() {
	
	var broadway = {
		info: '<strong>victim</strong><br>\
					5224 N Broadway St<br> Chicago, IL 60640<br>\
					<a href="https://goo.gl/maps/jKNEDz4SyyH2">Get Directions</a>',
		victimlat: 26.878788,
		victimlong: 75.808685
	};

	var belmont = {
		info: '<strong>user1</strong><br>\
					1025 W Belmont Ave<br> Chicago, IL 60657<br>\
					<a href="https://goo.gl/maps/PHfsWTvgKa92">Get Directions</a>',
		user1lat: 26.878788,// 26.8853301,// 26.8918722,// 26.8984143,// 26.9049564,// 26.9114985,// 26.9180406,// 26.9245827,// 26.9311248,// 26.9376669,//  26.944209,
		user1long: 75.808685// 75.8000928// 75.7915006// 75.7829084// 75.7743162// 75.765724// 75.7571318// 75.7485396// 75.7399474// 75.7313552// 75.722763
	};

	var sheridan = {
		info: '<strong>police van</strong><br>\r\
					6600 N Sheridan Rd<br> Chicago, IL 60626<br>\
					<a href="https://goo.gl/maps/QGUrqZPsYp92">Get Directions</a>',
		policelat: 26.878788,// 26.8805715,// 26.882355,// 26.8841385,// 26.885922,// 26.8877055,// 26.889489,// 26.8912725,// 26.893056,// 26.8948395,// 26.896623,
		policelong: 75.808685// 75.7940201// 75.7793552// 75.7646903// 75.7500254// 75.7353605// 75.7206956// 75.7060307// 75.6913658// 75.6767009// 75.662036
	};
	var drone1 = {
		info: '<strong>police van</strong><br>\r\
					6600 N Sheridan Rd<br> Chicago, IL 60626<br>\
					<a href="https://goo.gl/maps/QGUrqZPsYp92">Get Directions</a>',
		drone1lat: 26.878788,// 26.8805715,// 26.882355,// 26.8841385,// 26.885922,// 26.8877055,// 26.889489,// 26.8912725,// 26.893056,// 26.8948395,// 26.896623,
		drone1long: 75.808685// 75.7920201// 75.7753552// 75.7586903// 75.7420254// 75.7253605// 75.7086956// 75.6920307// 75.6753658// 75.6587009// 75.642036
	};
	var drone2 = {
		info: '<strong>police van</strong><br>\r\
					6600 N Sheridan Rd<br> Chicago, IL 60626<br>\
					<a href="https://goo.gl/maps/QGUrqZPsYp92">Get Directions</a>',
		drone2lat: 26.878788,// 26.8805715,// 26.882355,// 26.8841385,// 26.885922,// 26.8877055,// 26.889489,// 26.8912725,// 26.893056,// 26.8948395,// 26.896623,
		drone2long: 75.808685// 75.7940201// 75.7793552// 75.7646903// 75.7500254// 75.7353605// 75.7206956// 75.7060307// 75.6913658// 75.6767009// 75.662036
	};
	var user2 = {
		info: '<strong>police van</strong><br>\r\
					6600 N Sheridan Rd<br> Chicago, IL 60626<br>\
					<a href="https://goo.gl/maps/QGUrqZPsYp92">Get Directions</a>',
		user2lat: 26.896623,
		user2long: 75.662036
	};

	var locations = [
      [broadway.info, broadway.victimlat, broadway.victimlong, 0],
      [belmont.info, belmont.user1lat, belmont.user1long, 1],
      [sheridan.info, sheridan.policelat, sheridan.policelong, 2],
	  [drone2.info, drone2.drone2lat, drone2.drone2long, 3],
	  [drone1.info, drone1.drone1lat, drone1.drone1long, 4],
	  [user2.info, user2.user2lat, user2.user2long, 5],
    ];

	var map = new google.maps.Map(document.getElementById('map'), {
		zoom: 13,
		center: new google.maps.LatLng(26.878788, 75.808685),
		mapTypeId: google.maps.MapTypeId.ROADMAP
	});
	
	
	var myCity = new google.maps.Circle({
    center: new google.maps.LatLng(26.878788, 75.808685),
    radius: 400,
    strokeColor: "#0000FF",
    strokeOpacity: 0.8,
    strokeWeight: 2,
    fillColor: "#0000FF",
    fillOpacity: 0.4
  });
  myCity.setMap(map);
  
	
	

	//var infowindow = new google.maps.InfoWindow({});
	

	var marker, i;
	var labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    var labelIndex = 0;
	for (i = 0; i < locations.length; i++) {
		marker = new google.maps.Marker({
			position: new google.maps.LatLng(locations[i][1], locations[i][2]),
			label: labels[labelIndex++ % labels.length],
			map: map
		});

		google.maps.event.addListener(marker, 'click', (function (marker, i) {
			return function () {
				infowindow.setContent(locations[i][0]);
				infowindow.open(map, marker);
				
			}
		})(marker, i));
	}
}
