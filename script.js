// This example adds a search box to a map, using the Google Place Autocomplete
// feature. People can enter geographical searches. The search box will return a
// pick list containing a mix of places and predicted search terms.

// This example requires the Places library. Include the libraries=places
// parameter when you first load the API. For example:
// <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">

function initAutocomplete() {
    var map = new google.maps.Map(document.getElementById('map'), {
      center: {lat: 34.23833238, lng: -118.523664572},
      zoom: 13,
      mapTypeId: 'roadmap'
    });
  
    // Create the search box and link it to the UI element.
    var input = document.getElementById('pac-input');
    var searchBox = new google.maps.places.SearchBox(input);
  
    // Bias the SearchBox results towards current map's viewport.
    map.addListener('bounds_changed', function() {
      searchBox.setBounds(map.getBounds());
    });
  
    var markers = [];
    // Listen for the event fired when the user selects a prediction and retrieve
    // more details for that place.
    searchBox.addListener('places_changed', function() {
      var places = searchBox.getPlaces();
  
      if (places.length == 0) {
        return;
      }
  
      // Clear out the old markers.
      markers.forEach(function(marker) {
        marker.setMap(null);
      });
      markers = [];
  
      // For each place, get the icon, name and location.
      var bounds = new google.maps.LatLngBounds();
      places.forEach(function(place) {
        if (!place.geometry) {
          console.log("Returned place contains no geometry");
          return;
        }
        var icon = {
          url: place.icon,
          size: new google.maps.Size(71, 71),
          origin: new google.maps.Point(0, 0),
          anchor: new google.maps.Point(17, 34),
          scaledSize: new google.maps.Size(25, 25)
        };
  
        // Create a marker for each place.
        markers.push(new google.maps.Marker({
          map: map,
          icon: icon,
          title: place.name,
          position: place.geometry.location
        }));
  
        if (place.geometry.viewport) {
          // Only geocodes have viewport.
          bounds.union(place.geometry.viewport);
        } else {
          bounds.extend(place.geometry.location);
        }
      });
      map.fitBounds(bounds);
    });
  }

  $(document).ready(function(){
    // Add smooth scrolling to all links
    $("a").on('click', function(event) {
  
      // Make sure this.hash has a value before overriding default behavior
      if (this.hash !== "") {
        // Prevent default anchor click behavior
        event.preventDefault();
  
        // Store hash
        var hash = this.hash;
  
        // Using jQuery's animate() method to add smooth page scroll
        // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
        $('html, body').animate({
          scrollTop: $(hash).offset().top
        }, 800, function(){
     
          // Add hash (#) to URL when done scrolling (default click behavior)
          window.location.hash = hash;
        });
      } // End if
    });
  });

    
  function drawStuff() {
    var data = new google.visualization.arrayToDataTable([
      ['Move', 'Percentage'],
      ["12 am", 100],
      ["1 am", 31],
      ["2 am", 12],
      ["3 am", 10],
      ["4 am", 3],
      ["3 am", 10],
      ["4 am", 44],
      ["5 am", 31],
      ["6 am", 12],
      ["7 am", 10],
      ["8 am", 3],
      ["9 am", 10],
      ["10 am", 44],
      ["11 am", 31],
      ["12 pm", 12],
      ["1 pm", 10],
      ["2 pm", 3],
      ["3 pm", 10],
      ["4 pm", 44],
      ["5 pm", 31],
      ["6 pm", 12],
      ["7 pm", 10],
      ["8 pm", 3],
      ["9 pm", 10],
      ["10 pm", 3],
      ["11 pm", 10]
    ]);

    var options = {
      width: 600,
      legend: { position: 'none' },
      chart: {
        title: 'Chess opening moves',
        subtitle: 'popularity by percentage' },
      axes: {
        x: {
          0: { side: 'top', label: 'White to move'} // Top x-axis.
        }
      },
      bar: { groupWidth: "50%" }
    };

    var chart = new google.charts.Bar(document.getElementById('top_x_div'));
    // Convert the Classic options to Material options.
    chart.draw(data, google.charts.Bar.convertOptions(options));
  };
 