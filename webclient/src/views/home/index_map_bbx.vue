<template>
  <div>
    <!-- <topMenu></topMenu> -->
    <div class="content">
      <div class="col_full col-md-9">
        <centerMap :kind='kind'></centerMap>
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
  data () {
    return {
      // 显示now还是history
      kind: null
    }
  },
  methods: {
    changeKind: function () {
      var params = this.$route;
      // console.log(params);
      this.kind = params.params['kind'];
    }
  },
  components: {
    topMenu,
    centerMap,
    rightCharts
  },
  mounted: function () {
    this.changeKind();
  },
  watch: {
    // 监听路由的变化
    '$route' (to, from) {
      // 判断路由中的参数
      // var params = to;
      // console.log(params);
      this.changeKind();
    }
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
  background-color: rgba(13, 18, 40, 0.831);
}
.col_full {
  height: 100%;
}
</style>
