<template>
  <div id="mycontent">
    <div id="basemap"></div>
    <div id="timeline"></div>
    <modalMain ref='modalChild'></modalMain>
    <div
      id="track_btn"
      class="btn-group"
      role="group"
    >
      <button
        type="button"
        class="btn btn-success"
        @click="trackMarkerStart"
      >
        <span
          class="glyphicon glyphicon-play"
          aria-hidden="true"
        >开始</span>
      </button>
      <button
        type="button"
        class="btn btn-warning"
        @click="trackMarkerPause"
      >
        <span
          class="glyphicon glyphicon-pause"
          aria-hidden="true"
        >暂停</span>
      </button>
      <button
        type="button"
        class="btn btn-danger"
        @click="trackMarkerEnd"
      >
        <span
          class="glyphicon glyphicon glyphicon-stop"
          aria-hidden="true"
        >终止</span>
      </button>
    </div>
    <div
      id="date_btn"
      v-show="!isNow"
    >
      <datePicker @loadTracks="loadTracks"></datePicker>
    </div>
  </div>
</template>

<script>
// const baseUrl = process.env.BASE_URL;
// 地图组件
import "leaflet";
import L from "leaflet";

// import '../../components/js/map/trackback/LeafletPlayback.js';
import "../../components/js/map/trackback/LeafletPlayback.js";
import vis from "vis";
// 引入bus
import bus from '../../assets/eventBus.js';

import "leaflet/dist/leaflet.css";
import "leaflet-defaulticon-compatibility/dist/leaflet-defaulticon-compatibility.webpack.css";
import "leaflet-defaulticon-compatibility";

// 加入movingmarker
import "../../components/js/map/moveingmarker/MovingMarker.js";
// import 'leaflet.css';
// import '../../components/css/map/trackplay/control.playback.css'

// 子组件
import modalMain from "../member/modal/modal_main.vue";

import { BBXTrackInfo } from "../../models/bbx.js";
// 时间组件
import datePicker from "../member/date/datepicker.vue";
// 前后端交互api
import { loadBBXNowList, loadBBXGPS, loadBBXTrack } from "../../api/api.js";
// 引入dateformat
var dateFormat = require('dateformat');
// import func from './vue-temp/vue-editor-bridge.js';
export default {
  data () {
    return {
      mymap: null,
      trackplay: null,
      trackplaycontrol: null,
      baseUrl: process.env.BASE_URL,
      trackMarkers: [],
      bbxs: [],
      //polyline对象数组
      polylines: [],
      // 当前时间
      targetDate: null,
      // isNow: false
    };
  },
  props: {
    // 时间的种类
    kind: String
  },
  components: {
    modalMain,
    datePicker
  },
  methods: {
    //开始，暂停，终止事件
    trackMarkerStart: function () {
      // console.log("开始");
      var myself = this;
      var index = 0;
      for (let obj of myself.trackMarkers) {
        if (obj._latlngs.length > 1) {
          obj.start();
        }

        // index += 1;
        // console.log(index);
        // console.log(obj._leaflet_id);
        // console.log(obj._latlng);
      }
      // this.trackMarkers.forEach(obj => {
      //   obj.start();
      //   index += 1;
      //   console.log(index);
      //   console.log(obj._leaflet_id);
      //   console.log(obj._latlng);
      // });
    },
    // 暂停
    trackMarkerPause: function () {
      // console.log("暂停");
      var myself = this;
      for (let obj of myself.trackMarkers) {
        if (obj._latlngs.length > 1) {
          obj.pause();
        }

      }
      // this.trackMarkers.forEach(obj => {
      //   obj.pause();
      // });
    },
    //终止
    trackMarkerEnd: function () {
      // console.log("终止");
      var myself = this;
      for (let obj of myself.trackMarkers) {
        if (obj._latlngs.length > 1) {
          obj.stop();
        }

      }
      // this.trackMarkers.forEach(obj => {
      //   obj.stop();
      // });
    },
    // 设置当前日期，传入date（格式为：yyyy-mm-dd）
    initTargetDate: function (now) {
      this.targetDate = now;
    },
    // 根据传入的日期获取该日期的轨迹列表，传入的date（格式为：yyyy-mm-dd）
    loadTracks: function (now) {
      var myself = this;
      // 每次调用前需要先清空data
      this.clearMarkers();
      this.initTargetDate(now);
      var targetdate = {
        targetdate: now,
        kind: myself.kind
      };
      loadBBXTrack(targetdate).then(res => {
        var myself = this;
        var start = "";
        var end = "";
        var tracks = [];
        //
        var index = 0;
        for (let temp of res.data) {
          index += 1;
          if (temp.latlngs.length != 0) {
            var trackTemp = new BBXTrackInfo(
              temp.bid,
              temp.code,
              start,
              end,
              temp.latlngs,
              null
            );
            tracks.push(trackTemp);
            var track = myself.loadMovingMarker(trackTemp);
            myself.trackMarkers.push(track);
            // 注意此处需要重新向bbxs中推送这个track对象的id（_leaflet_id)!!
            myself.bbxs.push({
              bid: temp.bid,
              code: temp.code,
              id: track._leaflet_id
            });
          }
        }
        // console.log('获取tarck完成');
      })
    },
    // 清除当前markers以及折线
    clearMarkers: function () {
      // 每次调用前需要先清空data
      for (let temp of this.trackMarkers) {
        this.mymap.removeLayer(temp);
      }
      for (let temp of this.polylines) {
        this.mymap.removeLayer(temp);
      }
      this.trackMarkers = [];
      this.bbxs = [];
      this.polylines = [];
      // console.log(this.mymap);
    },
    // 初始化地图
    initMap: function () {
      var myself = this;
      if (myself.mymap == null) {
        myself.mymap = L.map("basemap").setView([30.09, 127.75], 4);
        // var mymap = L.map('basemap').setView([51.505, -0.09], 13)
        // mapLink = "../static/mapfiles/";

        // var mapfilesPath = '../../../mapfiles/{z}/{x}/{y}.jpg'
        var mapfilesPath = "/mapfiles/{z}/{x}/{y}.jpg";
        L.tileLayer(mapfilesPath, {
          attribution: "",
          maxZoom: 8,
          minZoom: 2
        }).addTo(myself.mymap);
        this.$emit("update:basemap", myself.mymap);
      }
    },
    // 暂时不使用了
    loadShip: function () {
      var myself = this;
      // var data = myself.loadTestJson()
      loadBBXNowList().then(res => {
        var tracks = [];
        for (let temp of res.data) {
          tracks.push({
            lat: temp.lat,
            lng: temp.lng,
            time: 1502529980,
            dir: temp.heading,
            info: []
          });
        }

        const trackplayback = L.trackplayback(tracks, myself.mymap, {
          targetOptions: {
            useImg: true,
            imgUrl: "../../../ship.png"
          }
        });
        myself.trackplay = trackplayback;
        const trackplaybackControl = L.trackplaybackcontrol(trackplayback);
        myself.trackplaycontrol = trackplaybackControl;
        trackplaybackControl.addTo(myself.mymap);
        myself.trackplay.start();
      });
      // const trackplayback = L.trackplayback(data, myself.mymap);
    },
    // 加载marker
    loadMarker: function () {
      var myself = this;
      // 使用非base64位图的方式
      var greenIcon = L.icon({
        iconUrl: "/leaflet/images/marker-icon.png",
        shadowUrl: "/leaflet/images/maker-shadow.png",
        // iconSize: [38, 95], // size of the icon
        // shadowSize: [50, 64], // size of the shadow
        iconAnchor: [12, 41] // point of the icon which will correspond to marker's location
        // shadowAnchor: [4, 62],  // the same for the shadow
        // popupAnchor: [-3, -76] // point from which the popup should open relative to the iconAnchor
      });
      // L.marker([44.61131534, -123.4726739], { icon: greenIcon }).addTo(myself.mymap);
      L.marker([44.63, -123.47]).addTo(myself.mymap);
      // L.marker([44.61131534, -123.4726739]).addTo(myself.mymap);
    },
    // 测试：加载移动marker
    loadMovingMarkerTest: function () {
      var myself = this;
      var latlngs = [[44.63, -123.47], [46.63, -123.47], [46.63, -119.47]];
      var times = [2000, 2000];
      //1- 添加折线
      var polyline = L.polyline(latlngs, { color: "red" }).addTo(myself.mymap);
      // 缩放地图到折线所在区域
      // myself.mymap.fitBounds(polyline.getBounds());

      //2- 点移动起来
      var myMovingMarker = L.Marker.movingMarker(latlngs, times).addTo(
        myself.mymap
      );
      myMovingMarker.start();
    },

    //根据track信息，在地图上加入marker，并绘制折线
    loadMovingMarker: function (trackInfo) {
      var myself = this;
      //1- 添加折线
      var polyline = L.polyline(trackInfo.latlngs, { color: "red" }).addTo(
        myself.mymap
      );
      this.polylines.push(polyline);
      // 缩放地图到折线所在区域
      // myself.mymap.fitBounds(polyline.getBounds());
      var times = [5000, 5000, 5000];
      //2- 点移动起来
      var myMovingMarker = L.Marker.movingMarker(
        trackInfo.latlngs,
        times
      ).addTo(myself.mymap);

      // 添加至数组中
      // this.trackMarkers.push(myMovingMarker);
      //3- 添加事件
      // 业务逻辑-1：点击暂停，再次点击再移动（暂时不需要）
      // myMovingMarker.once('click', function () {
      //   console.log(this);
      //   myMovingMarker.start();
      //   myself.showModalFrame();
      //   myMovingMarker.on('click', function () {
      //     if (myMovingMarker.isRunning()) {
      //       myMovingMarker.pause()
      //     } else {
      //       myMovingMarker.start()
      //     }
      //   })
      // })
      // 业务逻辑-2：点击获取该marker的id，并获取该marker的信息，加载指定船舶的数据
      myMovingMarker.once("click", function () {
        var that = this;
        // var bbxInfo = myself.bbxs.filter(obj => {
        //   obj.id === that._animId;
        // });

        var bbxInfo = myself.bbxs.find(obj => {
          return obj.id === that._leaflet_id;
        });
        bbxInfo.targetdate = myself.targetDate;
        // console.log(this);
        // myMovingMarker.start();
        myself.showModalFrame(bbxInfo);
        myMovingMarker.on("click", function () {
          myself.showModalFrame(bbxInfo);
        });
      });
      // myMovingMarker.start();
      return myMovingMarker;
    },
    // 调用加载子组件modal框
    showModalFrame: function (params) {
      // 调用modal子组件的showModal方法，显示modal窗口，并加载echarts数据
      this.$refs.modalChild.showModal(params);
    },
    // 获取后台的trak数据 （弃用，使用loadTracks）
    loadBBXsTrack: function () {
      loadBBXTrack().then(res => {
        var myself = this;
        // console.log(res)
        // 获取后端传过来的数据的长度

        // 将解析，并创建times数组
        // var lenList = res.data[0].speeds.length;
        // var times = [];
        // var timeTemp = 2000;
        var start = "";
        var end = "";
        // for (var i = 0; i <= lenList; i++) {
        //   times.push(timeTemp)
        // }
        var tracks = [];
        //
        for (let temp of res.data) {
          if (temp.latlngs.length != 0) {
            var trackTemp = new BBXTrackInfo(
              temp.bid,
              temp.code,
              start,
              end,
              temp.latlngs,
              null
            );
            tracks.push(trackTemp);
            var track = myself.loadMovingMarker(trackTemp);
            myself.trackMarkers.push(track);
            // 注意此处需要重新向bbxs中推送这个track对象的id（_leaflet_id)!!
            myself.bbxs.push({
              bid: temp.bid,
              code: temp.code,
              id: track._leaflet_id
            });
          }
        }
        // console.log(myself.trackMarkers);
      });
    },
    // 弃用
    loadGPS: function () {
      var myself = this;
      loadBBXGPS().then(res => {
        console.log(res);
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
        };
        // Setup timeline
        // var timeline = new vis.Timeline(document.getElementById('timeline'), timelineData, timelineOptions);
        // // A callback so timeline is set after changing playback time
        // function onPlaybackTimeChange (ms) {
        //   timeline.setCustomTime(new Date(ms));
        // };
        // Initialize playback
        var playback = new L.Playback(
          myself.mymap,
          res.data,
          null,
          playbackOptions
        );
      });
    },
    // 备份使用，无实际作用
    loadGPS1: function () {
      var myself = this;
      loadBBXGPS().then(res => {
        console.log(res);
        var startTime = new Date(res.data.properties.time[0]);
        // var endTime = new Date(demoTracks[0].properties.time[demoTracks[0].properties.time.length - 1]);
        var endTime = new Date(
          res.data.properties.time[res.data.properties.time.length - 1]
        );

        // Create a DataSet with data
        var timelineData = new vis.DataSet([
          { start: startTime, end: endTime, content: "Demo GPS Tracks" }
        ]);
        // Set timeline options
        var timelineOptions = {
          width: "100%",
          height: "120px",
          style: "box",
          axisOnTop: true,
          showCustomTime: true
        };
        // Setup timeline
        var timeline = new vis.Timeline(
          document.getElementById("timeline"),
          timelineData,
          timelineOptions
        );

        // Playback options
        var playbackOptions = {
          playControl: true,
          dateControl: true,

          // layer and marker options
          layer: {
            pointToLayer: function (featureData, latlng) {
              var result = {};

              if (
                featureData &&
                featureData.properties &&
                featureData.properties.path_options
              ) {
                result = featureData.properties.path_options;
              }

              if (!result.radius) {
                result.radius = 5;
              }

              return new L.CircleMarker(latlng, result);
            }
          },

          marker: {
            getPopup: function (featureData) {
              var result = "";

              if (
                featureData &&
                featureData.properties &&
                featureData.properties.title
              ) {
                result = featureData.properties.title;
              }

              return result;
            }
          }
        };
        // timeline.setCustomTime(new Date(ms));

        // A callback so timeline is set after changing playback time
        function onPlaybackTimeChange (ms) {
          timeline.setCustomTime(new Date(ms));
        }
        // Initialize playback
        var playback = new L.Playback(
          myself.mymap,
          null,
          onPlaybackTimeChange,
          playbackOptions
        );

        playback.setData(res.data);
        // playback.addData(blueMountain);
      });
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
    // 1-初始化地图引擎
    this.initMap();
    // this.loadMarker();
    // this.loadMovingMarker();
    // 2-获取后台返回的船舶轨迹信息
    // this.loadBBXsTrack();
    // this.loadShip();
    // this.loadGPS();
    // this.play();
  },
  computed: {
    isNow: function () {
      return this.kind === 'now';
    }
  },
  watch: {
    targetDate: function (newVal) {
      var myself = this;
      // console.log(newVal+oldVal);
      // 此处修改还需要传入kind
      var params = {
        targetdate: newVal,
        kind: myself.kind
      }
      // 通过事件总线通知别的兄弟组件更新targetdate的值
      bus.$emit('on-targetDate', params);
    },
    kind: function (newVal) {
      if (newVal === 'now') {
        // 1-初始化地图引擎
        // this.initMap();
        this.targetDate = dateFormat(new Date(), 'yyyy-mm-dd');
        // 2-获取后台返回的船舶轨迹信息
        // this.loadBBXsTrack();
        this.loadTracks(this.targetDate);
      }
    }
  },
};
</script>

<style scoped>
#mycontent {
  /* position: absolute; */
  /* top: 188px; */
  /* height: 600px; */

  /* bottom: 0px; */
  height: 100%;
  width: 100%;
  overflow: hidden;
}
#basemap {
  height: 100%;
  width: 100%;
  position: absolute;
}
#track_btn {
  position: absolute;
  left: 80px;
  bottom: 65px;
  z-index: 1000;
}
#date_btn {
  position: absolute;
  left: 300px;
  bottom: 65px;
  z-index: 1000;
}
</style>
