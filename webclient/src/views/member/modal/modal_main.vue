<template>
  <div
    id="mymodal"
    class="modal fade"
    tabindex="-1"
    role="dialog"
  >
    <div
      id="modal_content"
      class="modal-dialog"
      role="document"
    >
      <div class="modal-content">
        <div class="modal-header">
          <button
            type="button"
            class="close"
            data-dismiss="modal"
            aria-label="Close"
          ><span aria-hidden="true">&times;</span></button>
          <h4 class="modal-title">船舶编号</h4>
        </div>
        <div class="modal-body">
          <div>
            <ul
              id="mytabs"
              class="nav nav-tabs"
            >
              <li
                v-for="(item,index) in menulist"
                role="presentation"
                :class="{actiove:index===indexMenu}"
              >
                <a
                  href="#"
                  @click="active(index)"
                >{{item.name}}</a>
              </li>
            </ul>
            <!-- <div
              id="main"
              style=""
            ></div> -->
            <bbxObservation
              :columns="childColumns"
              :values="childVals"
              :title="childTitle"
              ref="bbxObs"
            ></bbxObservation>
          </div>
        </div>
        <div class="modal-footer">
          <button
            type="button"
            class="btn btn-default"
            data-dismiss="modal"
          >关闭</button>
          <button
            type="button"
            class="btn btn-primary"
          >确定</button>
        </div>
      </div>
      <!-- /.modal-content -->
    </div>
    <!-- /.modal-dialog -->
  </div>
</template>

<script>
import bbxObservation from '../../member/charts/bbx_observation_charts.vue'

//前后端api
import { loadObservationData } from '../../../api/api.js'
export default {
  //modal框主体部分
  data () {
    return {
      menulist: [
        {
          name: '降水',
          code: 'rain',
          url: ''
        },
        {
          name: '能见度',
          code: 'vis',
          url: ''
        },
        {
          name: '风速',
          code: 'ws',
          url: ''
        }, {
          name: '气温',
          code: 'at',
          url: ''
        }, {
          name: '气压',
          code: 'bp',
          url: ''
        }, {
          name: '水温',
          code: 'wt',
          url: ''
        }, {
          name: '水温',
          code: 'wv',
          url: ''
        }

      ],
      indexMenu: 0,
      targetDate: '2018-12-18 00:00',
      childVals: ['sss', 'ssss'],
      childColumns: ['123', '123'],
      childTitle: '测试测试'
    }
  },
  components: {
    bbxObservation
  },
  methods: {
    showModal: function () {
      console.log('显示modal窗');
      $("#mymodal").modal();
    },
    initCharts: function () {
      // 父组件调用子组件的初始化方法
      this.$refs.bbxObs.initCharts();
      console.log('调用成功');
    },
    // 切换导航栏
    active: function (index) {
      console.log(index);
      this.indexMenu = index;
    },

    // 加载指定code以及指定datetime的观测值
    loadDetailData: function (code, date) {
      let params = {
        code: code,
        targetdate: date
      }
      // 暂时注释掉真正读取的操作
      // 父组件将由后台返回的vals与columns赋值为要传递给子组件的data中
      this.childVals = [0.37, 0.34, 0.32, 0.30, 0.29, 0.28, 0.27, 0.26, 0.25, 0.24, 0.23, 0.22];
      this.childColumns = ["2018-2-1 15:00", "2018-2-1 16:00", "2018-2-1 17:00", "2018-2-1 18:00", "2018-2-1 19:00", "2018-2-1 20:00", "2018-2-1 21:00", "2018-2-1 22:00", "2018-2-1 23:00", "2018-2-2 00:00", "2018-2-2 01:00", "2018-2-2 02:00"];

      // 初始化echarts
      this.initCharts();

      // loadObservationData(params).then(res=>{
      //     //模拟数据请求操作
      //     /*
      //       res.data中返回的主要包含两样：
      //         columns:
      //         values:
      //     */
      // })
    }
  },
  watch: {
    // 监听menu index，当发生变化时，向后台请求并获取指定类型
    indexMenu: function (newVal, oldVal) {
      // 获取当前选中的菜单中对应的code
      var nowCode = this.menulist[newVal].code;
      console.log(nowCode);
      // 
      this.loadDetailData(nowCode, this.targetDate)
    }
  }

}
</script>

<style scoped>
#modal_content {
  width: 850px;
}
</style>
