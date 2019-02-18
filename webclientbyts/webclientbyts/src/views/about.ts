import { Component, Vue } from 'vue-property-decorator'

// @Component({
//   components: {
//     'main-layout': MainLayout
//   }
// })
@Component
export default class home extends Vue {
  msg: number = 123
  index: number = 0
  mounted() {
    // this.greet()
    alert(this.add(5))
  }

  get computedMsg() {
    return 'computed' + this.msg
  }

  // 加法方法
  add(index: number): number {
    return this.index + index
  }

  greet() {
    alert('greeting:' + this.msg)
  }
}
