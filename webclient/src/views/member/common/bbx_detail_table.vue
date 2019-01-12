<template>
  <form class="form-horizontal">
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
                <td>{{code}}</td>
                <td>{{name}}</td>
                <td class="my-th-normal">{{area}}</td>
                <td class="my-th-warm">{{ton}}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </form>
</template>

<script>
import { loadBBXDetail } from '../../../api/api.js';

import { areaDict } from '../../../components/js/common/area.js';
export default {
  data () {
    return {
      // 船舶名称
      name: null,
      // 海区
      area: null,
      // 吨位
      ton: null,
      // 呼号
      code: null

    }
  },
  props: {
    // 组件传递来的船舶基础信息
    detailInfo: Object,
    // 船舶id
    bid: Number
  },
  methods: {
    // 加载详情table信息
    initTable: function (bid) {
      var myself = this;
      var params = {
        bid: bid
      };
      // 根据bid加载船舶的详情信息
      loadBBXDetail(params).then(res => {
        // console.log(res);
        myself.code = res.data.code;
        myself.name = res.data.desc;
        myself.area = areaDict[res.data.area];
        myself.ton = res.data.shipton;
      });
    }
  },
  mounted: function () {
    // 根据bid加载
    // this.initTable();
  },
  watch: {
    // 当bid修改时重新加载表格
    bid: function (newVal) {
      console.log(newVal);
      this.initTable(newVal);
    }
  }

}
</script>

<style scoped>
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
