<template>
  <div>
    <!-- <p>{{mytest}}</p> -->
    <div id="main"></div>
  </div>
</template>

<script>
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
    initCharts1: function () {
      var myself = this;
      console.log(myself.title);
      // 基于准备好的dom，初始化echarts图表
      var myChart = echarts.init(document.getElementById('main'));
      // var myChartContent = echarts.init(document.getElementById('bar_content'));
      //		var myBar = echarts.init(document.getElementById('mybar'));
      var option = {
        tooltip: {
          show: true
        },
        legend: {
          data: ['波浪']
        },
        xAxis: [{
          type: 'category',
          //此处测试数据修改为由父组件传入
          data: ["2018-2-1 15:00", "2018-2-1 16:00", "2018-2-1 17:00", "2018-2-1 18:00", "2018-2-1 19:00", "2018-2-1 20:00", "2018-2-1 21:00", "2018-2-1 22:00", "2018-2-1 23:00", "2018-2-2 00:00", "2018-2-2 01:00", "2018-2-2 02:00"],
          // data: myself.columns,
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
          type: 'value',
          "axisLabel": {
            //					interval: 0,
            textStyle: {
              color: '#FFFFFF'
            }
          },
        }],
        series: [{
          "name": "波浪", //需要与legend中的data相同
          "type": "line",
          smooth: true, //不是折线，是曲线
          itemStyle: {
            normal: {
              //设置折点的颜色
              color: '#4169E1',
              //注意lineStyle需要卸载normal里面
              //自定义折线颜色
              lineStyle: {
                color: '#00FF00'
              },
              //自定义折线下区域的颜色
              areaStyle: {
                color: '#B0E0E6'
              },

              label: {
                show: true //显示每个点的值
              }
            }

          }, //向下填充区域
          // 子组件的测试数据改为由父组件传入
          "data": [0.37, 0.34, 0.32, 0.30, 0.29, 0.28, 0.27, 0.26, 0.25, 0.24, 0.23, 0.22],
          // "data": myself.values,
          label: {
            normal: {
              show: true
            }
          }
        },]
      };
      $('#mytabs a').click(function (e) {
        e.preventDefault();
        $(this).tab('show');
      })
      // 为echarts对象加载数据 
      myChart.setOption(option);
      // myChartContent.setOption(option);
    },
    initCharts: function () {
      // 基于准备好的dom，初始化echarts图表
      var myChart = echarts.init(document.getElementById('main'));
      //				var myChartContent=echarts.init(document.getElementById('bar_content'));
      //		var myBar = echarts.init(document.getElementById('mybar'));
      var option = {
        tooltip: {
          show: true
        },
        legend: {
          data: ['波浪', '周期']
        },
        xAxis: [{
          type: 'category',
          data: ["2018-2-1 15:00", "2018-2-1 16:00", "2018-2-1 17:00", "2018-2-1 18:00", "2018-2-1 19:00", "2018-2-1 20:00", "2018-2-1 21:00", "2018-2-1 22:00", "2018-2-1 23:00", "2018-2-2 00:00", "2018-2-2 01:00", "2018-2-2 02:00"],
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
          type: 'value',
          "axisLabel": {
            //					interval: 0,
            textStyle: {
              color: '#FFFFFF'
            }
          },
        }],
        series: [{
          "name": "波浪", //需要与legend中的data相同
          "type": "line",
          smooth: true, //不是折线，是曲线
          itemStyle: {
            normal: {
              //设置折点的颜色
              color: '#4169E1',
              //注意lineStyle需要卸载normal里面
              //自定义折线颜色
              lineStyle: {
                color: '#00FF00'
              },
              //自定义折线下区域的颜色
              areaStyle: {
                color: '#B0E0E6'
              },

              label: {
                show: true //显示每个点的值
              }
            }

          }, //向下填充区域
          "data": [0.37, 0.34, 0.32, 0.30, 0.29, 0.28, 0.27, 0.26, 0.25, 0.24, 0.23, 0.22],
          label: {
            normal: {
              show: true
            }
          }
        },]
      };

      // 为echarts对象加载数据 
      myChart.setOption(option);
    },

  }
}
</script>

<style scoped>
#main {
  height: 500px;
  width: 900px;
}
</style>
