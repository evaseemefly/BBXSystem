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
      targetdate: null,
      kind: null
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
      var params = {
        targetdate: now,
        kind: myself.kind
      };
      // 注意每次加载需要清空当前的statics
      this.statistics = [];
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
    }
  },
  mounted: function () {
    var myself = this;
    bus.$on("on-targetDate", function (msg) {
      myself.targetdate = msg['targetdate'];
      myself.kind = msg['kind'];
      myself.loadAreaDetail(myself.targetdate);
    });
  },
  beforeDestroy: function () {
    bus.$off("on-targetDate");
  }
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
