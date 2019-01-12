<template>
  <el-date-picker
    v-model="targetDate"
    type="date"
    placeholder="选择日期"
    @change="changeDate"
    format="yyyy-MM-dd"
    value-format="yyyy-MM-dd"
  >
  </el-date-picker>
</template>

<script>
var dateFormat = require('dateformat');
export default {
  data () {
    return {
      pickerOptions1: {
        disabledDate (time) {
          return time.getTime() > Date.now();
        },
        shortcuts: [{
          text: '今天',
          onClick (picker) {
            picker.$emit('pick', new Date());
          }
        }, {
          text: '昨天',
          onClick (picker) {
            const date = new Date();
            date.setTime(date.getTime() - 3600 * 1000 * 24);
            picker.$emit('pick', date);
          }
        }, {
          text: '一周前',
          onClick (picker) {
            const date = new Date();
            date.setTime(date.getTime() - 3600 * 1000 * 24 * 7);
            picker.$emit('pick', date);
          }
        }]
      },
      targetDate: '',
      value2: '',
    };
  },
  methods: {
    // 日期改变时重新加载船舶的轨迹列表
    changeDate: function (newVal) {
      /*
        当日期修改或首次创建时，调用父类中的加载tracks的方法
        将当前时间传入
      */
      this.$emit('loadTracks', newVal);
      // console.log(`${newVal}：${oldVal}`);
    }
  },
  // 创建时为targetDate赋值
  created () {
    // this.targetDate = new Date();
    // var now= = new Date().toLocaleDateString();
    var now = new Date();
    var nowStr = dateFormat(now, 'yyyy-mm-dd');
    this.targetDate = nowStr;
    this.changeDate(this.targetDate);
    // console.log(nowStr);
    // console.log(new Date().format('yyy-MM-dd'));
  }
};
</script>

<style>
</style>
