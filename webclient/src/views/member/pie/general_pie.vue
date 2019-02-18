<template>
  <div
    class="area_pie"
    :id="id"
    :state="state"
    :title="title"
    :name="name"
  ></div>
</template>

<script>
// 汇总的饼状图
export default {
  data () {
    return {
      dict: {
        "normal": "正常",
        "late": "迟到",
        "noarrival": "未到",
        "invalid": "缺失",
      }
    }
  },
  props: {
    // 加载echarts的id
    id: String,
    //加载series数组
    state: Object,
    // 
    title: String,
    name: String
  },
  methods: {
    initPie: function () {
      var myself = this;
      var myChart_n = echarts.init(document.getElementById(myself.id));
      var temp = this.values;
      if (myself.values.length > 0) {
        var option = {
          backgroundColor: '#2c343c',

          title: {
            text: myself.title,
            left: 'center',
            top: 20,
            textStyle: {
              color: '#ccc'
            }
          },

          tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
          },
          // 图例组件
          legend: {
            orient: 'vertical',
            x: 'left',
            data: ['正常', '迟到', '未到', '缺失'],
            textStyle: {
              color: '#B0E0E6'
            }
          },
          visualMap: {
            show: false,
            min: 0,
            max: 30,
            inRange: {
              colorLightness: [0, 1]
            }
          },

          series: [
            {
              name: myself.name,
              type: 'pie',
              radius: '55%',
              center: ['50%', '60%'], // 注意此处需要下调圆心的位置，不然会对顶部的title有遮挡
              minAngle: 2, //最小的扇区角度（0 ~ 360）
              color: ['#40E0D0', '#87CEEB', '#B0E0E6', '#33A1C9'],
              // data: myself.values.sort(function (a, b) { return a.value - b.value; }),
              // data: myself.values.sort(function (a, b) { return a.value - b.value; }),
              data: myself.values,
              // data: [{
              //   value: 10,
              //   name: '正常'
              // },
              // {
              //   value: 1,
              //   name: '迟到'
              // },
              // {
              //   value: 2,
              //   name: '未到'
              // },
              // {
              //   value: 2,
              //   name: '缺失'
              // }
              // ],
              roseType: 'radius',
              label: {
                // position: 'outside',
                normal: {
                  textStyle: {
                    // color: 'rgba(255, 255, 255, 0.3)'
                    color: '#B0E0E6'
                  },
                  position: 'outside',
                }
              },
              labelLine: {
                normal: {
                  lineStyle: {
                    color: 'rgba(255, 255, 255, 0.3)'
                    // color: '#FFFAFA'
                  },
                  smooth: 0.2,
                  length: 10,
                  length2: 20
                }
              },
              // itemStyle: {
              //   normal: {
              //     color: '#40E0D0',
              //     shadowBlur: 200,
              //     shadowColor: 'rgba(0, 0, 0, 0.5)'
              //   }
              // },

              animationType: 'scale',
              animationEasing: 'elasticOut',
              // 动画延迟
              animationDelay: function (idx) {
                return Math.random() * 200;
              }
            }
          ]
        };
        myChart_n.setOption(option);
      }

    }
  },
  mounted: function () {
    this.initPie();
  },
  computed: {
    values: function () {
      var valuesByState = [];
      var myself = this;
      for (let v in myself.state) {
        let tempObj = {};
        let keyval = {};
        // console.log(v);
        // console.log(myself.state[v]);
        tempObj[v] = myself.state[v];
        keyval.name = myself.dict[v];
        keyval.value = myself.state[v];
        // keyval.name = myself.state[v];
        // tempObj.v = myself.state[v];
        valuesByState.push(keyval);
      }
      return valuesByState;
    }
  },
  watch: {
    values: function () {
      this.initPie();
    }
  }
}
</script>

<style scoped>
.area_pie {
  height: 23%;
  /*width: 500px;*/
  margin-bottom: 20px;
}
</style>
