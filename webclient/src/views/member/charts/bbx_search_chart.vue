<template>
  <div id="main"></div>
</template>

<script>

import { loadRealtime } from '../../../api/api.js';

// 使用策略模式
var strategies = {
  'w': function (list) {
    var columns = [];
    var values = [];
    list.forEach(obj => {
      /*
      后端返回的结果
      1- 存在时
      {
         "timestamp": "2018-12-30 16:00:00",
         "val": {
                  "ws": 0,
                  "wd": 60
                }
      }

      2- 不存在时：
      {
        "timestamp": "2018-12-01 00:00:00",
        "val": {}
      }
      */
      // 1- 先判断val是否包含ws与wd
      if (obj.val['ws'] != null && obj.val['wd'] != null) {
        if ((obj.val.ws != 9999 && obj.val.ws != 999.9) || (obj.val.wd != 9999 && obj.val.wd != 999.9)) {
          //如果数据为缺省值那么就改成0
          values.push({
            value: obj.val.ws,
            symbolRotate: obj.val.wd
          });
          columns.push(obj.timestamp);
        } else {
          values.push(null);
          columns.push(obj.timestamp);
        }
      }

    })
    return {
      columns: columns,
      values: values
    }
  },
  'default': function (list) {
    var columns = [];
    var values = [];
    list.forEach(obj => {
      // myself.values.push(obj.val);
      // myself.columns.push(obj.timestamp);
      if (obj.val != 9999 && obj.val != 999.9) {
        //如果数据为缺省值那么就改成0
        values.push(obj.val);
        columns.push(obj.timestamp);
      } else {
        values.push(null);
        columns.push(obj.timestamp);
      }
    })
    return {
      columns: columns,
      values: values
    }
  }
}
var strategyAppendRealtimeData = function (factor, list) {
  return strategies[factor](list)
}

// import {*} from '../../../api/api.js'
export default {
  data () {
    return {
      title: "",
      columns: [],
      values: [],
      mychart: null,
      //y轴刻度的区间
      min: 900,
      max: 1500
    };
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
        myself.myChart = echarts.init(document.getElementById('main'));
        //				var myChartContent=echarts.init(document.getElementById('bar_content'));
        //		var myBar = echarts.init(document.getElementById('mybar'));
        // this.disposeCharts();
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
            data: ["波浪"]
          },
          xAxis: [
            {
              type: "category",
              data: myself.columns,
              //使用以下方式实现显示全部x坐标上的点
              axisLabel: {
                //interval: 0,
                textStyle: {
                  color: "#FFFFFF"
                }
              }

              //                  interval:0
            }
          ],
          yAxis: [
            {
              // min: 600,
              // max: 1300,
              type: "value",
              axisLabel: {
                //					interval: 0,
                textStyle: {
                  color: "#FFFFFF"
                }
              }
            }
          ],
          series: [
            {
              name: "波浪", //需要与legend中的data相同
              type: "line",
              smooth: true, //不是折线，是曲线
              itemStyle: {
                normal: {
                  //设置折点的颜色
                  color: "rgb(189, 196, 56)",
                  //注意lineStyle需要卸载normal里面
                  //自定义折线颜色
                  lineStyle: {
                    color: ""
                  },
                  //自定义折线下区域的颜色
                  areaStyle: {
                    color: "rgb(56, 196, 147)"
                  },

                  label: {
                    show: true //显示每个点的值
                  }
                }
              }, //向下填充区域
              data: myself.values,
              label: {
                normal: {
                  show: true
                }
              }
            }

          ]
        };
        if (factor === 'ws' || factor === 'wd') {
          // option.series['symbol'] = 'triangle';
          option.series[0]['symbolSize'] = [40, 20];
          // option.series['symbol'] = 'image:../../../../../assets/common/arrows.png'
          option.series[0]['symbol'] = 'image://common/arrows.png'
        } else {
          option.series[0]['symbol'] = 'circle';
          option.series[0]['symbolSize'] = 8;
        }
        // 为echarts对象加载数据 
        myself.myChart.setOption(option);
      } else {
        this.disposeCharts();
      }
    },

    // 
    strategyAppendRealtimeData: function (facotr, list) {
      var myself = this;
      var strategies = {
        'w': function (list) {
          list.forEach(obj => {
            /*
            后端返回的结果
            1- 存在时
            {
               "timestamp": "2018-12-30 16:00:00",
               "val": {
                        "ws": 0,
                        "wd": 60
                      }
            }

            2- 不存在时：
            {
              "timestamp": "2018-12-01 00:00:00",
              "val": {}
            }
            */
            // 1- 先判断val是否包含ws与wd
            if (obj.val['ws'] != null && obj.val['wd'] != null) {
              if ((obj.val.ws != 9999 && obj.val.ws != 999.9) || (obj.val.wd != 9999 && obj.val.wd != 999.9)) {
                //如果数据为缺省值那么就改成0
                myself.values.push({
                  value: obj.val.ws,
                  symbolRotate: obj.val.wd
                });
                myself.columns.push(obj.timestamp);
              } else {
                myself.values.push(null);
                myself.columns.push(obj.timestamp);
              }
            }

          })
        },
        'default': function (list) {
          list.forEach(obj => {
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
        }
      };
      return strategies[facotr](list);
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
        var factor = (myself.factor == 'ws' || myself.factor == 'wd') ? 'w' : 'default';
        var obj = strategyAppendRealtimeData(factor, res.data);
        myself.values = obj['values'];
        myself.columns = obj['columns'];
        // myself.strategyAppendRealtimeData(factor, res.data);
        // strategyTemp(factor, res.data);
        // console.log(res)

        // 19-01-10
        // res.data.forEach(obj => {
        //   // myself.values.push(obj.val);
        //   // myself.columns.push(obj.timestamp);
        //   if (obj.val != 9999 && obj.val != 999.9) {
        //     //如果数据为缺省值那么就改成0
        //     myself.values.push(obj.val);
        //     myself.columns.push(obj.timestamp);
        //   } else {
        //     myself.values.push(null);
        //     myself.columns.push(obj.timestamp);
        //   }
        // })

        myself.initCharts(myself.factor);
        // myself.values = res.data.val;
      });
    },
    // 销毁echarts
    disposeCharts: function () {
      if (this.mychart != null) {
        this.mychart.dispose();
      }
    }
  },
  watch: {
    factor: function (newVal) {
      // 需要判断是否bid与factor两个均不为null
      if ((this.factor != null) & (this.bid != null)) {
        this.loadReatimeData();
      }
    },
    bid: function (newVal) {
      // 需要判断是否bid与factor两个均不为null
      if ((this.factor != null) & (this.bid != null)) {
        this.loadReatimeData();
      }
    }
  },
  mounted: function () { }
};
</script>

<style scoped>
#main {
  width: 95%;
  height: 800px;
  /* box-shadow: 0 0 3px rgb(229, 238, 238); */
}
</style>
