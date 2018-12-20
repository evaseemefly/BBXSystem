<template>
  <div>
    <topMenu></topMenu>
    <div class="content">
      <div class="col-md-9">
        <centerMap></centerMap>
      </div>
      <div class="col-md-3">
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

<style>
</style>
