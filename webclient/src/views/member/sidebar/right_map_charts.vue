<template>
  <div class="right_charts">
    <totalPie></totalPie>

    <!-- <genPie
      v-for="item in statistics"
      id="item.id"
      title="item.name"
      name="item.name"
      states="item.state"
    ></genPie> -->
    <!-- <div v-for="item in statistics">
      <genPie
        v-if="item.state"
        :id="item.id"
        :title="item.name"
        :name="item.name"
        :state="item.state"
      ></genPie>
    </div> -->
    <genPie
      v-for="item in statistics"
      :id="item.id"
      :title="item.name"
      :name="item.name"
      :state="item.state"
    ></genPie>
  </div>
</template>

<script>
// 引入bus
import bus from '../../../assets/eventBus.js';

import { AreaStatisticsInfo, StatesInfo } from '../../../models/bbx.js'
import totalPie from '../pie/total_pie.vue';
import genPie from '../pie/general_pie.vue';
import { loadAllAreaStatistic } from '../../../api/api.js'
export default {
  data () {
    return {
      statistics: [],
      areaDict: {
        'n': '北海',
        'e': '东海',
        's': '南海'
      },
      targetdate:null
    }
  },
  components: {
    totalPie,
    genPie
  },
  methods: {
    // 读取指定海区的统计结果
    loadAreaDetail: function (now) {
      var myself = this;
      var params={
        targetdate:now
      };
      // 与后端实际交互暂时先不写
      loadAllAreaStatistic(params).then(res => {
        for (let temp of res.data) {
          // 获取到area 的str 标识符
          var area_str = temp.area;

          // 获取标识符
          var stateTemp = {}
          for (let temp_static of temp.static) {

            var key = temp_static.state;
            var val = temp_static.count;
            stateTemp[key] = val;
          }
          var statisticTemp = new AreaStatisticsInfo(area_str + '_area', 'area_str', myself.areaDict[area_str] + '船舶到报情况', stateTemp);
          myself.statistics.push(statisticTemp);
        }
      })
      // 生成的 正常、迟到、未到、缺失的该海区的model
      // var stateTemp = new StatesInfo(10, 2, 2, 1);
      // var stateTemp = {
      //   normal: 10,
      //   late: 2,
      //   noarrival: 3,
      //   invalid: 1
      // };
      // var statisticTempE = new AreaStatisticsInfo('e_area', 'e', '东海船舶到报情况', stateTemp);

      // var stateTemp = {
      //   normal: 12,
      //   late: 4,
      //   noarrival: 3,
      //   invalid: 1
      // };
      // var statisticTempN = new AreaStatisticsInfo('n_area', 'n', '北海船舶到报情况', stateTemp);

      // var stateTemp = {
      //   normal: 11,
      //   late: 5,
      //   noarrival: 1,
      //   invalid: 4
      // };
      // var statisticTempS = new AreaStatisticsInfo('s_area', 's', '南海船舶到报情况', stateTemp);
      // this.statistics.push(statisticTempN);
      // this.statistics.push(statisticTempE);
      // this.statistics.push(statisticTempS);
    }
  },
  mounted: function () {
    var myself=this;
    bus.$on("on-targetDate",function(msg){     
      myself.targetdate=msg;    
      myself.loadAreaDetail(msg);  
    });   
  },
  // watch: {
  //   targetDate:function(newVal) {

  //     this.loadAreaDetail(newVal);
  //     console.log(newVal);
  //   }
  // }
}
</script>
<style scoped>
.right_charts {
  height: 100%;
  /* color: rgba(57, 50, 104, 0.694); */
}
</style>
