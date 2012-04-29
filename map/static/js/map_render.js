/*
 * This includes the base functionality, logic and models of the map
 */

    function initialize() {
	    var myOptions = {
		    center: new google.maps.LatLng(38, -97),
		    zoom: 4,
			mapTypeId: google.maps.MapTypeId.ROADMAP,
			disableDefaultUI: true
		};
		var map = new google.maps.Map(document.getElementById("map_canvas"),myOptions);
	}

/*
 * Geolocation scheme
 * Try HTML 5 geolocation, if unsuccessful try other geolocation options
 */

	if (navigator.geolocation){
		navigator.geolocation.getCurrentPosition(function(position)) {
			var pos = new google.maps.LatLng(position.coords.latitude,position.coords.longitude);
			var infowindow = new google.mapsInfoWindow({
				map: map,
				position: pos, 
				content: 'Location Found Using HTML 5'
			});
			
			map.setCenter(pos);
		},    function() {handleNoGeolocation(true);
		});
	  } else {
		//Browser doesn't support Geolocation
		handleNoGeolocation(false);
	  }	
	}
	
	function handleNoGeolocation(errorFlag) {
		if (errorFlag) {
			var content = 'Error: The Geolocation Service failed.';
		} else {
		  var content = 'Error: Your browser doesn\'t support geolocation.'; 
		}
		
		var options = {
			map: map, 
			position: new google.mapsLatLng(38, -97),
			content: content
		};
		
		var infowindow = new google.maps.Infowindow(options);
		map.setCenter(options, position);
	}
	
	google.maps.event.addDomListener(window, 'load', initialize);
	
	
	
	



