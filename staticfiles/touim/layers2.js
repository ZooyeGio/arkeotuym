var geojson = {
  "type":"FeatureCollection",
  "features":[
  { "type": "Feature", "properties": { "lieu": "Lattara", "imgy": "{% for carto in cartos.all %}{% if carto.id_map == 1 %}<img src=\"{{ carto.mapfile.url }}\" style=\"height: 220px;\">{% else %}{% endif %}{% endfor %}", "descr":"<p style=\"margin-top:20px;\">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Quis auctor elit sed vulputate. Id porta nibh venenatis cras sed felis. Elementum sagittis vitae et leo duis ut diam. Quam quisque id diam vel. Integer enim neque volutpat ac tincidunt. Platea dictumst vestibulum rhoncus est. Praesent tristique magna sit amet purus gravida quis. Aenean euismod elementum nisi quis eleifend quam adipiscing vitae proin. Vestibulum morbi blandit cursus risus at ultrices mi. Sit amet aliquam id diam maecenas ultricies mi.</p>", "iframe3": "<iframe src=\"tresorerie.html\" style=\"width:100%; height:240px;\">Non<\/iframe>" }, "geometry": { "type": "Point", "coordinates": [ 14440232.880829565227032, 8864868.11990000680089 ] } },
  { "type": "Feature", "properties": { "lieu": "Pasargadae", "imgy": "{% for carto in cartos.all %}{% if carto.id_map == 2 %}<img src=\"{{ carto.mapfile.url }}\" style=\"height: 200px;\">{% else %}{% endif %}{% endfor %}", "descr":"<p style=\"margin-top:20px;\">Nunc vel risus commodo viverra maecenas accumsan. Gravida arcu ac tortor dignissim convallis aenean et. Purus sit amet volutpat consequat mauris nunc congue nisi. Enim nunc faucibus a pellentesque sit amet porttitor. Non consectetur a erat nam at lectus urna duis. Vel eros donec ac odio tempor orci dapibus ultrices. Imperdiet proin fermentum leo vel orci porta non. Ut tristique et egestas quis ipsum suspendisse. Consectetur lorem donec massa sapien faucibus et molestie ac. Fermentum leo vel orci porta non pulvinar neque laoreet suspendisse. Orci porta non pulvinar neque.</p>", "iframe3": "<iframe src=\"gostdvor.html\" style=\"width:100%; height:240px;\">Non<\/iframe>" }, "geometry": { "type": "Point", "coordinates": [ 14441751.499910054728389, 8865568.682187795639038 ] } },
  { "type": "Feature", "properties": { "lieu": "Persépolis", "imgy": "{% for carto in cartos.all %}{% if carto.id_map == 5 %}<img src=\"{{ carto.mapfile.url }}\" style=\"height: 200px;\">{% else %}{% endif %}{% endfor %}", "descr":"<p style=\"margin-top:20px;\">Orci sagittis eu volutpat odio. Nisi quis eleifend quam adipiscing vitae proin sagittis nisl rhoncus. Leo urna molestie at elementum eu facilisis sed odio morbi. Id diam maecenas ultricies mi eget. Pharetra pharetra massa massa ultricies mi quis hendrerit dolor magna. Malesuada bibendum arcu vitae elementum curabitur vitae nunc. Facilisi etiam dignissim diam quis. Magna fringilla urna porttitor rhoncus dolor purus. Gravida neque convallis a cras semper auctor neque vitae. Accumsan sit amet nulla facilisi. Non odio euismod lacinia at quis risus sed vulputate. Convallis tellus id interdum velit laoreet id. Tempus imperdiet nulla malesuada pellentesque elit.</p>", "iframe3": "<iframe src=\"image.html\" style=\"width:100%; height:240px;\">Non<\/iframe>" }, "geometry": { "type": "Point", "coordinates": [ 14440963.808167312294245, 8865148.863544629886746 ] } }
  ]
};

var features = new ol.format.GeoJSON().readFeatures(geojson);

features.forEach(function(feature){ feature.setId(undefined) });

var myStyle = new ol.style.Style({
      image: new ol.style.Circle({
        radius: 7,
        fill: new ol.style.Fill({color: 'green'}),
        stroke: new ol.style.Stroke({
          color: 'blue', width: 1
        })
      })
    });

/*for image raster*/
var extent = [14435495.7, 8861886.6, 14447224.9, 8868386.9];   
var projection = new ol.proj.Projection({
  code: 'xkcd-image',
  units: 'pixels',
  extent: extent
  });
(function() {
    var map = new ol.Map({
        target: 'map',
        layers: [
            new ol.layer.Group({
                'title': 'Base maps',
                layers: [
                    new ol.layer.Group({
                        title: 'Stamen WaterColor',
                        type: 'base',
                        combine: true,
                        visible: false,
                        layers: [
                            new ol.layer.Tile({
                                source: new ol.source.Stamen({
                                    layer: 'watercolor'
                                })
                            }),
                            new ol.layer.Tile({
                                source: new ol.source.Stamen({
                                    layer: 'terrain-labels'
                                })
                            })
                        ]
                    }),
                    /*new ol.layer.Tile({
                        title: 'Water color',
                        type: 'base',
                        visible: false,
                        source: new ol.source.Stamen({
                            layer: 'watercolor'
                        })
                    }),*/
                    new ol.layer.Tile({
                      title: 'CartoDB Light',
                      type: 'base',
                      visible: false,
                      source: new ol.source.XYZ({
                        url:'http://{1-4}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png',
                        layer: 'CartoDB Dark'
                      })
                    }),
                    new ol.layer.Tile({
                        title: 'OSM',
                        type: 'base',
                        visible: true,
                        source: new ol.source.OSM()
                    })
                ]
            }),
            new ol.layer.Group({
                title: 'Overlays (à venir)',
                layers: [
                    /*new ol.layer.Image({
                        title: 'Countries',
                        source: new ol.source.ImageArcGISRest({
                            ratio: 1,
                            params: {'LAYERS': 'show:0'},
                            url: "https://ons-inspire.esriuk.com/arcgis/rest/services/Administrative_Boundaries/Countries_December_2016_Boundaries/MapServer"
                        })
                    }),*/
                    /*new ol.layer.Image({
                      title: 'Kernel Density',
                      source: new ol.source.ImageStatic({
                        url: 'kernel5000-EPSG4326.png',
                        projection: projection,
                        imageExtent: extent
                      })
                    })*/
                    ]
                  })
            ],
        view: new ol.View({
            center: [14432232.880829565227032, 8864868.11990000680089],
            zoom: 12
        })
    });

    var layerSwitcher = new ol.control.LayerSwitcher({
        tipLabel: 'Légende' // Optional label for button
    });
    map.addControl(layerSwitcher);

    /*var fullscreen = new ol.control.FullScreen();
    map.addControl(fullscreen);*/

    var scaleline = new ol.control.ScaleLine();
    map.addControl(scaleline);

/*add vector layers = geojson*/
var vectorLayer = new ol.layer.Vector({
  source: new ol.source.Vector({
    features: features,
    format: new ol.format.GeoJSON()
  }),
    style: new ol.style.Style({
      image: new ol.style.Circle({
        radius: 6,
        stroke: new ol.style.Stroke({
          color: 'black',
          radius: 3,
          width: 1
        }),
        fill: new ol.style.Fill({
          color: 'orange'
        })
      })
    })
  });
map.addLayer(vectorLayer);

// information en cliquant sur site archéo
    var infoDiv = document.getElementById("info");
      map.on('click', function(event) {

      var feature = map.forEachFeatureAtPixel(event.pixel, function(feature) {
      return feature;
      });
      if (feature) {
      infoDiv.innerHTML = "<h3><b>" + feature.get("lieu") + "</b></h3>" + "<br>" +
            feature.get("imgy") + "<br>" + 
            feature.get("descr") ; 
      }
      });

})();
