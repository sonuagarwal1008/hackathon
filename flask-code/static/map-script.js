function initMap() {
	
	var broadway = {
		info: '<strong>victim</strong><br>\
					5224 N Broadway St<br> Chicago, IL 60640<br>\
					<a href="https://goo.gl/maps/jKNEDz4SyyH2">Get Directions</a>',
		lat: 26.878788,
		long: 75.808685
	};

	var belmont = {
		info: '<strong>user1</strong><br>\
					1025 W Belmont Ave<br> Chicago, IL 60657<br>\
					<a href="https://goo.gl/maps/PHfsWTvgKa92">Get Directions</a>',
		lat: 26.944209,
		long: 75.722763
	};

	var sheridan = {
		info: '<strong>police van</strong><br>\r\
					6600 N Sheridan Rd<br> Chicago, IL 60626<br>\
					<a href="https://goo.gl/maps/QGUrqZPsYp92">Get Directions</a>',
		lat: 26.896623,
		long: 75.662036
	};
	var drone1 = {
		info: '<strong>police van</strong><br>\r\
					6600 N Sheridan Rd<br> Chicago, IL 60626<br>\
					<a href="https://goo.gl/maps/QGUrqZPsYp92">Get Directions</a>',
		lat: 26.896623,
		long: 75.642036
	};
	var drone2 = {
		info: '<strong>police van</strong><br>\r\
					6600 N Sheridan Rd<br> Chicago, IL 60626<br>\
					<a href="https://goo.gl/maps/QGUrqZPsYp92">Get Directions</a>',
		lat: 26.896623,
		long: 75.682036
	};

	var locations = [
      [broadway.info, broadway.lat, broadway.long, 0],
      [belmont.info, belmont.lat, belmont.long, 1],
      [sheridan.info, sheridan.lat, sheridan.long, 2],
	  [drone2.info, drone2.lat, drone2.long, 3],
	  [drone1.info, drone1.lat, drone1.long, 4],
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
