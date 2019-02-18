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
            <!-- <form class="form-horizontal">
              <div class="col-sm-12">
                <div class="panel panel-default boxshadow">
                  <div class="panel-heading">船舶基础信息</div>
                  <div class="panel-body table-responsive ">
                    <table class=" table table-striped table-hover table-bordered">
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
                          <td class="my-th-normal">东海</td>
                          <td class="my-th-warm">5000</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </form> -->
            <bbxDetailTable :bid="bid"></bbxDetailTable>
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
              :factor="childFactor"
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
import bbxDetailTable from '../common/bbx_detail_table.vue';
//前后端api
import { loadRealtime } from '../../../api/api.js';

import { strategyAppendRealtimeData } from '../../../module/search/ws_strategies.js';
import { menulist } from '../../../module/search/menu_list.js';
export default {
  //modal框主体部分
  data () {
    return {
      menulist: menulist,
      // menulist: [
      //   // {
      //   //   name: '降水',
      //   //   code: 'rain',
      //   //   url: ''
      //   // },
      //   {
      //     name: '能见度',
      //     code: 'vis',
      //     url: ''
      //   },
      //   {
      //     name: '风速',
      //     code: 'ws',
      //     url: ''
      //   }, {
      //     name: '气温',
      //     code: 'at',
      //     url: ''
      //   }, {
      //     name: '气压',
      //     code: 'bp',
      //     url: ''
      //   }, {
      //     name: '水温',
      //     code: 'wt',
      //     url: ''
      //   }, {
      //     name: '浪高',
      //     code: 'wv',
      //     url: ''
      //   }

      // ],
      indexMenu: 0,
      targetDate: null,
      childVals: [],
      childColumns: [],
      childFactor: null,
      childTitle: '测试测试',
      bbxCode: '',
      bid: 0,
      factor: null
    }
  },
  props: {
    kind: null
  },
  components: {
    bbxObservation,
    bbxDetailTable
  },
  methods: {
    showModal: function (par) {
      // console.log(par);
      this.bbxCode = par.code;
      this.bid = par.bid;
      this.targetDate = par.targetdate;
      $("#mymodal").modal();
      // 每次加载modal框时需要销毁echarts子组件
      this.$refs.bbxObs.destroyCharts();
    },
    initCharts: function (params) {

      // 父组件调用子组件的初始化方法
      this.$refs.bbxObs.initCharts();
      // console.log('调用成功');
    },

    // 切换导航栏
    active: function (index) {
      // console.log(index);
      this.indexMenu = index;
    },

    // 加载指定code以及指定datetime的观测值
    loadDetailData: function (code, bid, factor, date, kind) {
      var myself = this;
      let params = {
        code: code,
        targetdate: date,
        factor: factor,
        bid: bid,
        kind: kind
      };
      this.childVals = [];
      this.childColumns = [];
      this.childFactor = factor;
      loadRealtime(params).then(res => {

        // 暂时注释掉真正读取的操作
        // 父组件将由后台返回的vals与columns赋值为要传递给子组件的data中

        // 使用方式1，会导致子组件中的columns与values更新在initCharts之后
        var factor = (myself.factor == 'ws' || myself.factor == 'wd') ? 'w' : 'default';
        var obj = strategyAppendRealtimeData(factor, res.data);
        myself.childVals = obj['values'];
        myself.childColumns = obj['columns'];

        // 原始办法 方式v2
        // 此处由策略模式替代 19-01-15
        // res.data.forEach(obj => {
        //   if (obj.val != 9999 && obj.val != 999.9) {
        //     myself.childVals.push(obj.val);
        //     myself.childColumns.push(obj.timestamp);
        //   }
        //   else {
        //     myself.childVals.push(null);
        //     myself.childColumns.push(obj.timestamp);
        //   }
        // });
        // 初始化echarts
        // this.initCharts(params);
      });
    },
    mounted () {

    },
  },
  watch: {
    // 监听menu index，当发生变化时，向后台请求并获取指定类型
    indexMenu: function (newVal, oldVal) {
      // 获取当前选中的菜单中对应的code
      var factor = this.menulist[newVal].code;
      // 修改当前的factor
      this.factor = factor;
      // 修改子组件的title
      this.childTitle = this.menulist[newVal].name;
      // console.log(nowCode);
      var code = this.bbxCode;
      var bid = this.bid;
      var targetdate = this.targetDate;
      var kind = this.kind;

      this.childFactor = factor;
      // 
      this.loadDetailData(code, bid, factor, targetdate, kind);
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
.my-th-normal {
  color: #4154de;
}
.my-th-warm {
  color: rgba(255, 0, 0, 0.838);
}
/* 带一个阴影 */
.boxshadow {
  box-shadow: 2px 2px 10px grey;
}
/* 顶部字体加粗加大 */
.panel-heading {
  font-weight: bolder;
  font-size: large;
}
</style>
