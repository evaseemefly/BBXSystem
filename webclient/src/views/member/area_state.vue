<template>
  <div class="area">
    <div>
      <span class="area_title">{{area.name}}</span>
    </div>
    <!-- <table>
      <tr
        v-for="(rowindex,index) in bbxlistRowsNum"
        :key="index"
      >       
        <td
          v-for="(columnsindex, index) in bbxlistColumnsNum"
          :key="index"
        >
          <span>{{bbxlist[(columnsindex+(rowindex-1)*columnsCount)-1]}}</span>
          <span>{{(columnsindex+(rowindex-1)*columnsCount)-1}}</span>
          <span>{{rowindex-1}}-{{(columnsindex-1)}}</span>
          <span>{{rowindex}}-{{columnsindex}}</span>
        </td>
      </tr>
    </table>-->
    <!-- 方式2，不使用table，使用div -->
    <div
      class="cell"
      v-for="(item, index) in bbxlist"
      :key="index"
      :class="item.state"
      :title="item.lastestTime"
    >{{item.name}}</div>
  </div>
</template>

<script>
// 加载各类model
import { BBXStateInfo } from "../../models/bbx.js";

// 前后端交互api
import { loadBBXStateList, loadBBXState } from "../../api/api.js";

export default {
  data() {
    return {
      // 该海区的船舶列表
      // 当前为测试数据
      bbxlist: [],
      columnsCount: 5
    };
  },
  props: {
    // 由父组件传入的海区对象
    area: {
      type: Object,
      required: true
    }
  },
  // props: ["area"],
  computed: {
    //获取船舶集合的总行数（长度/行长度）
    bbxlistRowsNum: function() {
      return Math.round(this.bbxlist.length / this.columnsCount);
    },
    // 获取船舶的列数
    bbxlistColumnsNum: function() {
      var num = this.columnsCount;
      if (this.bbxlist.length < num) {
        num = this.bbxlist.length;
      }
      return num;
    }
  },
  methods: {
    // 根据海区编号获取该海区所用的全部志愿船舶的状态集合
    loadBBXlist: function(area) {
      loadBBXStateList(this.props.area).then(res => {
        console.log(res);
      });
    },
    // 加载指定海区的全部船舶列表
    loadBaseBBXlist: function(area) {
      let timeParam = "2018-12-22 22:22";
      var that = this;
      var area = this.area.id;
      loadBBXState(area, "")
        .then(res => {
          that.bbxlist = res.data;
          that.columnsCount = res.data.length;
        })
        .catch(err => {
          console.log(err);
        });
    }
  },
  mounted: function() {
    //页面加载时根据area获取指定海区的全部船舶
    this.loadBaseBBXlist();
  }
};
</script>

<style>
.area {
  background: #143b4d;
  border-radius: 5px;
  padding-bottom: 5px;
  padding-left: 5px;
  padding-right: 5px;
  padding-bottom: 10px;
  margin-top: 5px;
}

.area .area_title {
  display: block;
  color: #fff;
  font-size: 20px;
  background-color: #23b38d5f;
  border-radius: 5px;
  /* margin-top: 20px; */
  margin-bottom: 20px;
  font-family: "微软雅黑";
}
.area_title {
  display: inline-block;
  margin-top: 0.5em;
}
.cell {
  display: inline-block;
  width: 133px;
  height: 32px;
  line-height: 32px;
  padding: 0 20px;
  box-sizing: border-box;
  border-radius: 5px;

  color: #fff;
  font-size: 14px;
  margin-left: 5px;
  margin-right: 5px;
  margin-top: 5px;
  transition: 0.5s;
}
.cell:hover {
  cursor: pointer;
  box-shadow: 0px 0px 5px white;
  text-shadow: 1px 1px 2px black;
}

.ok {
  background: #23b37e;
}
.noarrival {
  background: #de1b0d;
}
.late {
  background: yellow;
}
.invalid {
  background: #a5bab3;
}

table td span {
  display: inline-block;
  width: 133px;
  height: 32px;
  line-height: 32px;
  padding: 0 20px;
  box-sizing: border-box;
  border-radius: 5px;
  background: #23b37e;
  color: #fff;
  font-size: 14px;
}
</style>