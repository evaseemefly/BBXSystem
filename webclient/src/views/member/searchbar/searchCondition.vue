<template>
  <div class="container">
    <div class="panel-body" style="padding-bottom:0px;">
      <div class="panel">
        <div class="panel-heading">查询条件</div>
        <div class="panel-body table-parent-panel searchbar">
          <form id="formSearch" class="form-horizontal">
            <div class="form-group" style="margin-top:15px">
              <label class="control-label col-sm-1" for="txt_search_departmentname">船舶</label>
              <div class="col-md-2">
                <select class="form-control" v-model="selectedBBX">
                  <option v-for="option in optionsBBX" v-bind:value="option.value">{{option.text}}</option>
                </select>
              </div>
              <label class="control-label col-sm-1" for="txt_search_departmentname">要素</label>
              <div class="col-md-2">
                <select class="form-control" v-model="selectedFactor">
                  <option
                    v-for="option in optionsFactor"
                    v-bind:value="option.value"
                  >{{option.text}}</option>
                </select>
              </div>
              <label class="control-label col-sm-1" for="txt_search_departmentname">时间</label>
              <div class="col-md-2">
                <Date-picker
                  type="daterange"
                  placement="bottom-end"
                  placeholder="选择日期"
                  style="width: 200px"
                  v-model="dateRange"
                  :options="datePickerOption"
                  @on-change="datePickerChosenChanged($event)"
                ></Date-picker>
              </div>

              <div class="col-md-2" style="text-align:left;">
                <button
                  type="button"
                  id="btn_search"
                  style="margin-left:50px"
                  v-on:click="summit()"
                  class="btn btn-primary"
                >查询</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { loadBBXlistByNow } from "../../../api/api.js";

export default {
  data() {
    return {
      optionsFactor: [
        {
          text: "降雨",
          value: "rain"
        },
        {
          text: "能见度",
          value: "vis"
        },
        {
          text: "风向",
          value: "wd"
        },
        {
          text: "风速",
          value: "ws"
        },
        {
          text: "气温",
          value: "at"
        }
      ],
      datePickerOption: {
        disabledDate(date, date2) {
          // let now = new Date();
          // let nowstr = `${now.getFullYear()}-${now.getMonth() +
          //   1}-${now.getDate()} 23:59:59`;
          // let limit = new Date(nowstr);
          // console.log(limit, limit.valueOf(), date.valueOf() > limit.valueOf());
          return date && date.valueOf() < Date.now() - 31 * 24 * 60 * 60 * 1000;
        }
      },
      dateRange: "",
      optionsBBX: [],
      selectedFactor: null,
      selectedBBX: null
    };
  },
  methods: {
    summit: function() {
      console.log("提交给后端");
    },
    initFatherParams: function() {
      var myself = this;

      this.$emit(
        "initParams",
        myself.selectedFactor,
        myself.selectedBBX,
        myself.dateRange
      );
    },
    loadBBXList: function() {
      var myself = this;
      var params = {
        operation: "now",
        nowdate: "2018-12-08 00:00"
      };
      loadBBXlistByNow(params).then(res => {
        if (res.data[0].area === "a") {
          res.data[0].bbxlist.forEach(obj => {
            myself.optionsBBX.push({
              text: obj.code,
              value: obj.bid
            });
          });
        }
      });
    },
    datePickerChosenChanged: function(event) {
      if (this.dateRange) {
        let time1 = this.dateRange[0];
        let time2 = this.dateRange[1];
        if (time1 instanceof Date && time2 instanceof Date) {
          if (time2 - time1 > 604800000) {
            this.$Message.info("所选时间区间不能超过1周,请重新选择");
            this.dateRange = ["", ""];
            return;
          }
        }
      }

      this.initFatherParams();
    }
  },
  mounted: function() {
    // this.optionsBBX.push({
    //   text: 'BBXA',
    //   value: 1
    // })
    this.loadBBXList();
  },
  watch: {
    selectedFactor: function() {
      this.initFatherParams();
    },
    selectedBBX: function() {
      this.initFatherParams();
    }
  }
};
</script>
<style scoped>
* {
  font-family: "微软雅黑";
}
.searchbar {
  box-shadow: 0 2px 10px rgb(229, 238, 238);
}
.panel {
  border: 0px;
}
.panel-heading {
  background-color: rgb(33, 108, 81);
  color: aliceblue;
  font-size: 2em;
  font-weight: bold;
  text-shadow: 2px 2px 10px #000;
}
</style>


