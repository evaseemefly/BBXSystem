<template>
  <div>
    <div v-for='item of arealist'>
      <AreaState :area=item></AreaState>
    </div>
    <StateLegend></StateLegend>
  </div>
</template>

<script>
import AreaState from '../member/area_state.vue'
import StateLegend from '../member/common/state_ legend.vue'
export default {
  data () {
    return {
      // 海区列表
      arealist: [
        { id: 'n', name: '北海分局' },
        { id: 'e', name: '东海分局' },
        { id: 's', name: '南海分局' }],

    }
  },
  components: {
    AreaState,
    StateLegend
  }

}
</script>

<style>
</style>
