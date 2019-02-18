<template>
  <div
    class="area_pie"
    id='totalpie'
  ></div>
</template>

<script>
// 三个海区通用的饼状图
export default {
  data () {
    return {
      title: '',
      values: []
    }
  },
  props: {
    // values: Array,
    // title: String
  },
  methods: {
    // 初始化pie图表
    initPie: function () {
      var myself = this;
      var myChart = echarts.init(document.getElementById('totalpie'));
      // 之后改为由后端在家后获取
      this.title = '当前船舶数量';
      this.values = [
        {
          value: 15,
          name: '北海分局'
        },
        {
          value: 20,
          name: '东海分局'
        },
        {
          value: 18,
          name: '南海分局'
        }
      ];
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

        visualMap: {
          show: false,
          min: 0,
          max: 30,
          inRange: {
            colorLightness: [0, 1]
          }
        },
        series: [{
          name: '当前船舶数量',
          type: 'pie',
          radius: '55%',
          center: ['50%', '50%'],
          data: myself.values.sort(function (a, b) {
            return a.value - b.value;
          }),
          roseType: 'radius',
          label: {
            normal: {
              textStyle: {
                color: 'rgba(255, 255, 255, 0.3)'
              }
            }
          },
          labelLine: {
            normal: {
              lineStyle: {
                color: 'rgba(255, 255, 255, 0.3)'
              },
              smooth: 0.2,
              length: 10,
              length2: 20
            }
          },
          itemStyle: {
            normal: {
              color: '#3D59AB',
              shadowBlur: 200,
              shadowColor: 'rgba(0, 0, 0, 0.5)'
            }
          },

          animationType: 'scale',
          animationEasing: 'elasticOut',
          animationDelay: function (idx) {
            return Math.random() * 200;
          }
        }]
      };
      myChart.setOption(option);
    }
  },
  mounted: function () {
    this.initPie();
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
