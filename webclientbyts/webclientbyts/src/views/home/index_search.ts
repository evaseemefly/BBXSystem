import { Component, Vue } from 'vue-property-decorator'
import searchbar from '../member/searchbar/search.vue'
import searchEcharts from '../member/charts/bbx_search_chart.vue'
@Component({
  components: { searchbar, searchEcharts }
})
export default class home extends Vue {
  selectedFactor: string = ''
  selectedBBX: any
  mounted() {}

  initParams(factor: string, bbx: any): void {
    this.selectedFactor = factor
    this.selectedBBX = bbx
  }
}
