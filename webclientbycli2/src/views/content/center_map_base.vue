<template>
  <div id="mycontent">
    <div id="basemap"></div>
    <div id="timeline"></div>
  </div>
</template>

<script>
// const baseUrl = process.env.BASE_URL;
// 地图组件
// import L from '../../components/js/leaflet/leaflet.js'
// import L from '../../../node_modules/leaflet/dist/leaflet.js'
import L from 'leaflet'
// import L from 'leaflet'
// import '../../components/js/map/trackback/LeafletPlayback.js';
import vis from 'vis'

// import 'leaflet-plugin-trackplayback'
// import shp from 'shpjs';
// import '../../components/js/map/trackplay/control.trackplayback.js'
// import `${baseUrl}/components/js/vis.min.js`;
// require('/components/js/vis.min.js')
// import "/vis.min.js";
// import '../../components/js/map/trackback/LeafletPlayback.js'

// import 'vis/dist/vis.js'
// import '../../components/js/map/trackback/vis.js'
// import '../../components/js/map/trackback/vis.min.js';
// import jQuery from 'jquery';
// import 'jquery';
// import '../../components/css/map/leaflet.css';
import 'leaflet/dist/leaflet.css'
// import 'leaflet.css';
// import '../../components/css/map/trackplay/control.playback.css'

// 前后端交互api
import { loadBBXNowList, loadBBXGPS } from '../../api/api.js'
export default {
  data () {
    return {
      mymap: null,
      trackplay: null,
      trackplaycontrol: null,
      baseUrl: process.env.BASE_URL
    }
  },
  methods: {
    // 初始化地图
    initMap: function () {
      var myself = this
      if (myself.mymap == null) {
        myself.mymap = L.map('basemap').setView([44.61131534, -123.4726739], 5)
        // var mymap = L.map('basemap').setView([51.505, -0.09], 13)
        // mapLink = "../static/mapfiles/";

        var mapfilesPath = '../../../mapfiles/{z}/{x}/{y}.jpg'
        // var mapfilesPath = 'static/img/mapfiles/{z}/{x}/{y}.jpg'
        L.tileLayer(mapfilesPath, {
          attribution: '',
          maxZoom: 8,
          minZoom: 2
        }).addTo(myself.mymap)
        // var status = 0
        // var popup = L.popup()

        // var rectangleMeasure = {
        //   startPoint: null,
        //   endPoint: null,
        //   rectangle: null,
        //   tips: null,
        //   layer: L.layerGroup(),
        //   color: '#0D82D7',
        //   addRectangle: function () {
        //     rectangleMeasure.destory()
        //     var bounds = []
        //     bounds.push(rectangleMeasure.startPoint)
        //     bounds.push(rectangleMeasure.endPoint)
        //     rectangleMeasure.rectangle = L.rectangle(bounds, {
        //       color: rectangleMeasure.color,
        //       weight: 1
        //     })
        //     rectangleMeasure.rectangle.addTo(rectangleMeasure.layer)

        //     var northWestPoint = rectangleMeasure.rectangle
        //       .getBounds()
        //       .getNorthWest(),
        //       southEastPoint = rectangleMeasure.rectangle
        //         .getBounds()
        //         .getSouthEast()
        //     rectangleMeasure.layer.addTo(map)
        //   },
        //   mousedown: function (e) {
        //     rectangleMeasure.rectangle = null
        //     rectangleMeasure.tips = null
        //     map.dragging.disable()
        //     rectangleMeasure.startPoint = e.latlng
        //     map.on('mousemove', rectangleMeasure.mousemove)
        //   },
        //   mousemove: function (e) {
        //     rectangleMeasure.endPoint = e.latlng
        //     rectangleMeasure.addRectangle()
        //     map
        //       .off('mousedown ', rectangleMeasure.mousedown)
        //       .on('mouseup', rectangleMeasure.mouseup)
        //   },
        //   mouseup: function (e) {
        //     map.dragging.enable()
        //     map
        //       .off('mousemove', rectangleMeasure.mousemove)
        //       .off('mouseup', rectangleMeasure.mouseup)
        //       .off('mousedown', rectangleMeasure.mousedown)
        //   },
        //   destory: function () {
        //     if (rectangleMeasure.rectangle) {
        //       rectangleMeasure.layer.removeLayer(rectangleMeasure.rectangle)
        //     }
        //     if (rectangleMeasure.tips) {
        //       rectangleMeasure.layer.removeLayer(rectangleMeasure.tips)
        //     }
        //   }
        // }

        this.$emit('update:basemap', myself.mymap)
      }
    },
    loadShip: function () {
      var myself = this
      // var data = myself.loadTestJson()
      loadBBXNowList().then(res => {
        var tracks = []
        for (let temp of res.data) {
          tracks.push({
            lat: temp.lat,
            lng: temp.lng,
            time: 1502529980,
            dir: temp.heading,
            info: []
          })
        }

        const trackplayback = L.trackplayback(tracks, myself.mymap, {
          targetOptions: {
            useImg: true,
            imgUrl: '../../../ship.png'
          }
        })
        myself.trackplay = trackplayback
        const trackplaybackControl = L.trackplaybackcontrol(trackplayback)
        myself.trackplaycontrol = trackplaybackControl
        trackplaybackControl.addTo(myself.mymap)
        myself.trackplay.start()
      })
      // const trackplayback = L.trackplayback(data, myself.mymap);
    },
    play: function () {
      // this.trackplay.play();
      // this.trackplaycontrol.play();
    },
    loadMarker: function () {
      var myself = this
      var base64icon = 'data:image/png;base64,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'
      var base64shadow = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACkAAAApCAYAAACoYAD2AAAC5ElEQVRYw+2YW4/TMBCF45S0S1luXZCABy5CgLQgwf//S4BYBLTdJLax0fFqmB07nnQfEGqkIydpVH85M+NLjPe++dcPc4Q8Qh4hj5D/AaQJx6H/4TMwB0PeBNwU7EGQAmAtsNfAzoZkgIa0ZgLMa4Aj6CxIAsjhjOCoL5z7Glg1JAOkaicgvQBXuncwJAWjksLtBTWZe04CnYRktUGdilALppZBOgHGZcBzL6OClABvMSVIzyBjazOgrvACf1ydC5mguqAVg6RhdkSWQFj2uxfaq/BrIZOLEWgZdALIDvcMcZLD8ZbLC9de4yR1sYMi4G20S4Q/PWeJYxTOZn5zJXANZHIxAd4JWhPIloTJZhzMQduM89WQ3MUVAE/RnhAXpTycqys3NZALOBbB7kFrgLesQl2h45Fcj8L1tTSohUwuxhy8H/Qg6K7gIs+3kkaigQCOcyEXCHN07wyQazhrmIulvKMQAwMcmLNqyCVyMAI+BuxSMeTk3OPikLY2J1uE+VHQk6ANrhds+tNARqBeaGc72cK550FP4WhXmFmcMGhTwAR1ifOe3EvPqIegFmF+C8gVy0OfAaWQPMR7gF1OQKqGoBjq90HPMP01BUjPOqGFksC4emE48tWQAH0YmvOgF3DST6xieJgHAWxPAHMuNhrImIdvoNOKNWIOcE+UXE0pYAnkX6uhWsgVXDxHdTfCmrEEmMB2zMFimLVOtiiajxiGWrbU52EeCdyOwPEQD8LqyPH9Ti2kgYMf4OhSKB7qYILbBv3CuVTJ11Y80oaseiMWOONc/Y7kJYe0xL2f0BaiFTxknHO5HaMGMublKwxFGzYdWsBF174H/QDknhTHmHHN39iWFnkZx8lPyM8WHfYELmlLKtgWNmFNzQcC1b47gJ4hL19i7o65dhH0Negbca8vONZoP7doIeOC9zXm8RjuL0Gf4d4OYaU5ljo3GYiqzrWQHfJxA6ALhDpVKv9qYeZA8eM3EhfPSCmpuD0AAAAASUVORK5CYII='
      var greenIcon = L.icon({
        iconUrl: base64icon,
        shadowUrl: base64shadow

        // iconSize: [38, 95], // size of the icon
        // shadowSize: [50, 64], // size of the shadow
        // iconAnchor: [22, 94], // point of the icon which will correspond to marker's location
        // shadowAnchor: [4, 62],  // the same for the shadow
        // popupAnchor: [-3, -76] // point from which the popup should open relative to the iconAnchor
      })
      L.marker([44.61131534, -123.4726739], { icon: greenIcon }).addTo(myself.mymap)
      // L.marker([44.61131534, -123.4726739]).addTo(myself.mymap)
    },
    loadGPS: function () {
      var myself = this
      loadBBXGPS().then(res => {
        console.log(res)
        // var myself = this;
        // Setup leaflet map
        // var map = new L.Map('map');

        // var basemapLayer = new L.TileLayer('http://{s}.tiles.mapbox.com/v3/github.map-xgq2svrz/{z}/{x}/{y}.png');

        // Center map and default zoom level
        // myself.map.setView([44.61131534, -123.4726739], 6);

        // Adds the background layer to the map
        // map.addLayer(basemapLayer);

        // =====================================================
        // =============== Playback ============================
        // =====================================================

        // Playback options
        var playbackOptions = {
          playControl: true,
          dateControl: true,
          sliderControl: true
        }
        // Initialize playback
        /* eslint-disable no-new */
        new L.Playback(myself.mymap, res.data, null, playbackOptions)
      })
    },
    loadGPS1: function () {
      var myself = this
      loadBBXGPS().then(res => {
        console.log(res)
        var startTime = new Date(res.data.properties.time[0])
        // var endTime = new Date(demoTracks[0].properties.time[demoTracks[0].properties.time.length - 1]);
        var endTime = new Date(res.data.properties.time[res.data.properties.time.length - 1])

        // Create a DataSet with data
        var timelineData = new vis.DataSet([{ start: startTime, end: endTime, content: 'Demo GPS Tracks' }])
        // Set timeline options
        var timelineOptions = {
          'width': '100%',
          'height': '120px',
          'style': 'box',
          'axisOnTop': true,
          'showCustomTime': true
        }
        // Setup timeline
        var timeline = new vis.Timeline(document.getElementById('timeline'), timelineData, timelineOptions)

        // Playback options
        var playbackOptions = {

          playControl: true,
          dateControl: true,

          // layer and marker options
          layer: {
            pointToLayer: function (featureData, latlng) {
              var result = {}

              if (featureData && featureData.properties && featureData.properties.path_options) {
                result = featureData.properties.path_options
              }

              if (!result.radius) {
                result.radius = 5
              }

              return new L.CircleMarker(latlng, result)
            }
          },

          marker: {
            getPopup: function (featureData) {
              var result = ''

              if (featureData && featureData.properties && featureData.properties.title) {
                result = featureData.properties.title
              }

              return result
            }
          }

        }
        // timeline.setCustomTime(new Date(ms));

        // A callback so timeline is set after changing playback time
        function onPlaybackTimeChange (ms) {
          timeline.setCustomTime(new Date(ms))
        };
        // Initialize playback
        var playback = new L.Playback(myself.mymap, null, onPlaybackTimeChange, playbackOptions)
        playback.setData(res.data)
        // playback.addData(blueMountain);
      })
    },
    // 加载船舶的测试数据（暂时弃用）
    loadTestJson: function () {
      // const xhr = new XMLHttpRequest();
      // var data = null;
      // xhr.open('GET', '../../data/test.json', false);
      // var jsonUrl = '../../../test.json';

      // var jsonUrl = '<%= BASE_URL %>/test.json';
      // var jsonUrl = '../../data/test.json';
      // $.getJSON(jsonUrl, function (res) {
      //   data = res;
      // });
      // xhr.open('GET', './test.json', false);
      // xhr.send(null);
      // const data = JSON.parse(xhr.responseText);
      // return data;
    }
  },
  mounted: function () {
    this.initMap()
    this.loadMarker()
    // this.loadShip();
    // this.loadGPS();
    // this.play();
  }
}
</script>

<style>
#mycontent {
  position: absolute;
  top: 188px;
  height: 600px;
  bottom: 0px;
  width: 100%;
  overflow: hidden;
}
#basemap {
  height: 600px;
}
</style>
