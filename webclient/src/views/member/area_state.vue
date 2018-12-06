<template>
  <div class='area'>
    <span class='area_title'>{{area.name}}</span>
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
    </table> -->
    <!-- 方式2，不使用table，使用div -->
    <div
      class='cell'
      v-for="(item, index) in bbxlist"
      :key="index"
      :class="item.state"
    >
      {{item.name}}
    </div>
  </div>
</template>

<script>
// 加载各类model
import { BBXStateInfo } from '../../models/bbx.js'

// 前后端交互api
import { loadBBXStateList } from '../../api/api.js'
export default {
  data () {
    return {
      // 该海区的船舶列表
      // 当前为测试数据
      bbxlist: [
        {
          code: "BBX_1",
          name: "BBX_1",
          state: "ok"
        },
        {
          code: "BBX_2",
          name: "BBX_2",
          state: "invalid"
        },
        {
          code: "BBX_3",
          name: "BBX_3",
          state: "ok"
        },
        {
          code: "BBX_4",
          name: "BBX_4",
          state: "noarrival"
        },
        {
          code: "BBX_5",
          name: "BBX_5",
          state: "late"
        },
        {
          code: "BBX_6",
          name: "BBX_6",
          state: "ok"
        },
        {
          code: "BBX_7",
          name: "BBX_7",
          state: "noarrival"
        },
        {
          code: "BBX_8",
          name: "BBX_8",
          state: "ok"
        }
      ],
      columnsCount: 5
    }
  },
  props: {
    // 由父组件传入的海区对象
    area: {
      type: Object,
      required: true
    }
  },
  computed: {
    //获取船舶集合的总行数（长度/行长度）
    bbxlistRowsNum: function () {
      return Math.round(this.bbxlist.length / this.columnsCount)
    },
    // 获取船舶的列数
    bbxlistColumnsNum: function () {
      var num = this.columnsCount;
      if (this.bbxlist.length < num) {
        num = this.bbxlist.length
      }
      return num;
    }
  },
  methods: {
    // 根据海区编号获取该海区所用的全部志愿船舶的状态集合
    loadBBXlist: function (area) {
      loadBBXStateList(area).then(res => {
        console.log(res);
      })
    }
  }
}
</script>

<style>
.area {
  background: #143b4d;
  border-radius: 5px;
  padding-bottom: 5px;
  padding-left: 5px;
  padding-right: 5px;

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
