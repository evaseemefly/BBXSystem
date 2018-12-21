<template>
  <div>
    <topMenu></topMenu>
    <div class="content">
      <div class="col_full col-md-9">
        <centerMap></centerMap>
      </div>
      <div class="col_full col-md-3">
        <rightCharts></rightCharts>
      </div>
    </div>
    <!-- <centerMap></centerMap>
    <rightCharts></rightCharts> -->
  </div>
</template>

<script>
import topMenu from '../head/top_main_menu.vue'
import centerMap from '../content/center_map_base.vue'
import rightCharts from '../member/sidebar/right_map_charts.vue'
export default {
  components: {
    topMenu,
    centerMap,
    rightCharts
  }
}
</script>

<style scoped>
.content {
  width: 100%;
  top: 50px;
  bottom: 0px;
  position: absolute;
  margin: 0 auto;
}
.col_full {
  height: 100%;
}
</style>
