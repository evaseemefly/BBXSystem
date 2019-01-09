<template>
  <div>
    <!-- <p>{{mytest}}</p> -->
    <div id="main"></div>
  </div>
</template>

<script>

import $ from 'jquery'

// const $ = require('jquery')
// window.$ = $
// require('jquery-confirm')

import { loadRealtime } from '../../../api/api.js';
// var echarts = require('echarts')
export default {
  data () {
    return {
      // title:title,
      // columns:columns,
      // values:values
    }
  },
  props: {
    // title
    title: String,
    // 列数据
    columns: Array,
    // values
    values: Array
  },
  methods: {
    // 初始化echarts表格    
    initCharts: function (params) {
      // 基于准备好的dom，初始化echarts图表
      var myself = this;
      var myChart = echarts.init(document.getElementById('main'));
      // this.values = [];
      // this.columns = [];
      // console.log(params);
      //				var myChartContent=echarts.init(document.getElementById('bar_content'));
      //		var myBar = echarts.init(document.getElementById('mybar'));
      var option = {
        tooltip: {
          show: true
        },
        legend: {
          data: [myself.title]
        },
        xAxis: [{
          type: 'category',
          data: myself.columns,
          //使用以下方式实现显示全部x坐标上的点
          "axisLabel": {
            //interval: 0,
            textStyle: {
              color: '#FFFFFF'
            }
          },

          //                  interval:0   
        }],
        yAxis: [{
          // min: function () {
          //   let min = Math.min(myself.values)
          //   return min;
          // },
          type: 'value',
          "axisLabel": {
            //					interval: 0,
            textStyle: {
              color: '#FFFFFF'
            },
            // formatter: function (value, index) {
            //   return value.toFixed(2);
            // }
          },
        }],
        series: [{
          "name": myself.title, //需要与legend中的data相同
          "type": "line",
          smooth: true, //不是折线，是曲线
          itemStyle: {
            normal: {
              //设置折点的颜色
              color: 'rgb(189, 196, 56)',
              //注意lineStyle需要卸载normal里面
              //自定义折线颜色
              lineStyle: {
                color: '#00FF00'
              },
              //自定义折线下区域的颜色
              areaStyle: {
                color: 'rgb(56, 196, 147)'
              },

              label: {
                show: true //显示每个点的值
              }
            }

          }, //向下填充区域
          "data": myself.values,
          label: {
            normal: {
              show: true
            }
          }
        },]
      };

      // 为echarts对象加载数据 
      myChart.setOption(option);
      this.slideDown();
    },
    //销毁echarts表格
    destroyCharts () {
      this.slideUp();
    },
    // 下拉
    slideDown: function () {
      $('#main').slideDown("slow");
    },
    // 收起
    slideUp: function () {
      $('#main').slideUp("slow");
    }
  },
  mounted: function () {
    this.slideUp();
  }
}

</script>

<style scoped>
#main {
  height: 500px;
  width: 900px;
}
</style>
