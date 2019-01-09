<template>
  <div id="main">
  </div>
</template>

<script>
import { loadRealtime } from '../../../api/api.js';
// import {*} from '../../../api/api.js'
export default {
  data () {
    return {
      title: '',
      columns: [],
      values: [],
      mychart: null,
      //y轴刻度的区间
      min: 900,
      max: 1500
    }
  },
  props: {
    factor: String,
    bid: Number
  },
  methods: {
    initCharts: function (factor) {
      var myself = this;
      if (myself.mychart === null) {
        // 基于准备好的dom，初始化echarts图表
        this.myChart = echarts.init(document.getElementById('main'));
        //				var myChartContent=echarts.init(document.getElementById('bar_content'));
        //		var myBar = echarts.init(document.getElementById('mybar'));

        /*
          此处需要加入一个工厂方法，
          根据传入的factor
          若facotr为 ws wd时，option中的series与普通的略有不同


        */
        var option = {
          tooltip: {
            show: true
          },
          legend: {
            data: ['波浪']
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
            // min: 600,
            // max: 1300,
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
                color: 'rgb(189, 196, 56)',
                //注意lineStyle需要卸载normal里面
                //自定义折线颜色
                lineStyle: {
                  color: ''
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
          }]
        };
        if (factor === 'ws' || factor === 'wd') {
          option.series['symbol'] = 'triangle';
          option.series['symbolSize'] = [20, 10];
          option.series['symbol'] = 'image:../../../../../assets/common/arrows.png'
        }




        // 为echarts对象加载数据 
        this.myChart.setOption(option);
      } else {
        this.disposeCharts();
      }
    },
    loadReatimeData: function () {
      var myself = this;
      // 此处注意需要清空
      this.values = [];
      this.columns = [];
      var searchCondition = {
        factor: myself.factor,
        bid: myself.bid
      };
      loadRealtime(searchCondition).then(res => {
        // console.log(res)
        res.data.forEach(obj => {
          // myself.values.push(obj.val);
          // myself.columns.push(obj.timestamp);
          if (obj.val != 9999 && obj.val != 999.9) {
            //如果数据为缺省值那么就改成0
            myself.values.push(obj.val);
            myself.columns.push(obj.timestamp);
          } else {
            myself.values.push(null);
            myself.columns.push(obj.timestamp);
          }
        })

        myself.initCharts();
        // myself.values = res.data.val;
      });
    },
    disposeCharts: function () {
      if (this.mychart != null) {
        this.mychart.dispose();
      }
    }
  },
  watch: {
    factor: function (newVal) {
      // 需要判断是否bid与factor两个均不为null
      if (this.factor != null & this.bid != null) {
        this.loadReatimeData();
      }
    },
    bid: function (newVal) {
      // 需要判断是否bid与factor两个均不为null
      if (this.factor != null & this.bid != null) {
        this.loadReatimeData();
      }
    }
  },
  mounted: function () {

  }
}
</script>

<style scoped>
#main {
  width: 95%;
  height: 800px;
  /* box-shadow: 0 0 3px rgb(229, 238, 238); */
}
</style>
