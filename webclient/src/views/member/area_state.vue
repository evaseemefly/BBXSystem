<template>
  <div class='area'>
    <span class='area_title'>{{area.name}}</span>
    <table>
      <tr>
        <td>
          <span>BBX_A</span>
        </td>
        <td>
          <span>BBX_B</span>
        </td>
        <td>
          <span>BBX_C</span>
        </td>
        <td>
          <span>BBX_D</span>
        </td>
        <td>
          <span>BBX_D</span>
        </td>
        <td>
          <span>BBX_D</span>
        </td>
        <td>
          <span>BBX_D</span>
        </td>
      </tr>
      <tr>
        <td>
          <span>BBX_D</span>
        </td>
        <td>
          <span>BBX_D</span>
        </td>
        <td>
          <span>BBX_D</span>
        </td>
      </tr>
    </table>
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
      bbxlist: [
        {
          code: 'BACA',
          name: 'BACA',
          state: '200'
        },
        {
          code: 'BACA',
          name: 'BACA',
          state: '200'
        },
        {
          code: 'BACA',
          name: 'BACA',
          state: '200'
        }
      ]
    }
  },
  props: {
    // 由父组件传入的海区对象
    area: {
      type: Object,
      required: true
    }
  },
  methods: {
    // 根据海区编号获取该海区所用的全部志愿船舶的状态集合
    loadBBXlist: function (area) {
      loadBBXStateList(area).then(res => {
        console.log(res)
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
  display: inline-block;
  color: #fff;
  font-size: 20px;
  background-color: #23b38d5f;
  border-radius: 5px;
  /* margin-top: 20px; */
  margin-bottom: 20px;
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
