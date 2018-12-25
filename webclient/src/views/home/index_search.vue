<template>
  <div class="top_dis">
    <searchbar @initParams="initParams"></searchbar>
    <searchEcharts
      :factor='selectedFactor'
      :bid='selectedBBX'
    ></searchEcharts>
  </div>
</template>

<script>
import searchbar from '../member/searchbar/search.vue';
import searchEcharts from '../member/charts/bbx_search_chart.vue';
export default {
  data () {
    return {
      selectedFactor: null,
      selectedBBX: null
    }
  },
  methods: {
    initParams: function (factor, bbx) {
      this.selectedFactor = factor;
      this.selectedBBX = bbx;
    }
  },
  components: {
    searchbar,
    searchEcharts
  }
}
</script>

<style>
.top_dis {
  position: absolute;
  top: 50px;
  bottom: 0px;
  width: 100%;
}
</style>
