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
          <h4 class="modal-title">船舶编号{{bbxCode}}</h4>
        </div>
        <div class="modal-body my-content-primary">
          <div>
            <form class="form-horizontal">
              <div class="col-sm-12">
                <div class="panel panel-default">
                  <div class="panel-heading">船舶基础信息</div>
                  <div class="panel-body table-responsive">
                    <table class="table table-striped table-hover table-bordered">
                      <thead>
                        <th>呼号</th>
                        <th>船舶名称</th>
                        <th>所属海区</th>
                        <th>吨位</th>
                      </thead>
                      <tbody>
                        <tr>
                          <td>BBX_A</td>
                          <td>雪龙号</td>
                          <td>东海</td>
                          <td>5000</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </form>

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
import { loadRealtime } from '../../../api/api.js'
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
      childVals: [],
      childColumns: [],
      childTitle: '测试测试',
      bbxCode: '',
      bid: 0
    }
  },
  components: {
    bbxObservation
  },
  methods: {
    showModal: function (par) {
      // console.log(par);
      this.bbxCode = par.code;
      this.bid = par.bid;
      $("#mymodal").modal();
    },
    initCharts: function (params) {
      // 父组件调用子组件的初始化方法
      this.$refs.bbxObs.initCharts();
      // console.log('调用成功');
    },
    // 切换导航栏
    active: function (index) {
      console.log(index);
      this.indexMenu = index;
    },

    // 加载指定code以及指定datetime的观测值
    loadDetailData: function (code, bid, factor, date) {
      var myself = this;
      let params = {
        code: code,
        targetdate: date,
        factor: factor,
        bid: bid
      };
      this.childVals = [];
      this.childColumns = [];
      loadRealtime(params).then(res => {
        // 暂时注释掉真正读取的操作
        // 父组件将由后台返回的vals与columns赋值为要传递给子组件的data中
        res.data.forEach(obj => {
          myself.childVals.push(obj.val);
          myself.childColumns.push(obj.timestamp);
        });
        // 初始化echarts
        this.initCharts(params);
      });

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
      var factor = this.menulist[newVal].code;
      // console.log(nowCode);
      var code = this.bbxCode;
      var bid = this.bid;
      // 
      this.loadDetailData(code, bid, factor, this.targetDate);
    }
  }

}
</script>

<style scoped>
#modal_content {
  width: 850px;
}
.my-content-primary {
  background: #143b4d;
}
</style>
