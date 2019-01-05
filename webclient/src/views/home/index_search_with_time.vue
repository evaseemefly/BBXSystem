<template>
  <div class="content">
    <div class="container">
      <searchCondition @initParams="initParams"></searchCondition>
      <!-- <searchResult></searchResult> -->
      <searchEchartsWithTime :factor="selectedFactor" :bid="selectedBBX" :dateRange="dateRange"></searchEchartsWithTime>
    </div>
  </div>
</template>
<script>
import searchCondition from "../member/searchbar/searchCondition";
import searchEchartsWithTime from "../member/charts/bbx_search_chart_with_time.vue";
export default {
  data() {
    return {
      selectedFactor: null,
      selectedBBX: null,
      dateRange: ""
    };
  },
  methods: {
    initParams: function(factor, bbx, dateRange) {
      this.selectedFactor = factor;
      this.selectedBBX = bbx;
      //解析时间
      if (
        dateRange instanceof Array &&
        dateRange.length >= 2 &&
        dateRange[0] instanceof Date
      ) {
        let time1 = dateRange[0];
        let time2 = dateRange[1];
        this.dateRange = `${time1.getFullYear()}-${time1.getMonth() +
          1}-${time1.getDate()} ${time2.getFullYear()}-${time2.getMonth() +
          1}-${time2.getDate()}`;
      } else {
        this.dateRange = "";
      }
    }
  },
  components: {
    searchCondition,
    searchEchartsWithTime
  }
};
</script>
<style>
.content {
  position: absolute;
  width: 100%;
  top: 50px;
  padding-top: 10px;
  background-color: rgba(13, 18, 40, 0.831);
}
</style>

