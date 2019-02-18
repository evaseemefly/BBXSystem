<template>
  <div>
    <div class="container" v-show="hasData">
      <div class="row">
        <div class="panel panel-default">
          <!-- Default panel contents -->
          <div class="panel-heading table-title">数据详情</div>
          <div class="panel-body">
            <!-- Table -->
            <table class="table table-striped table-bordered table-hover dataTable">
              <thead>
                <th>INDEX</th>
                <th>DT</th>
                <th>LAT</th>
                <th>LON</th>
                <th>VAL({{this.facotr==''?'':this.factor.toUpperCase()}})</th>
              </thead>
              <tbody>
                <tr v-for="(row,idx) in tableData" :key="idx">
                  <td class="table-cell table-index">{{idx+1}}</td>
                  <td class="table-cell">{{row.nowdate }}</td>
                  <td class="table-cell">{{row.lat }}</td>
                  <td class="table-cell">{{row.lon }}</td>
                  <td class="table-cell">{{row.factor }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { loadBBXTableData } from "../../../api/api.js";
export default {
  data() {
    return {
      tableData: [],
      originData: [],
      hasData: false
    };
  },
  watch: {
    bid() {
      //重新获取数据
      this.loadData();
    },
    dateRange() {
      //重新获取数据
      this.loadData();
    },
    factor() {
      //不获取数据只更新列显示
      this.rebuildTableData();
    }
  },
  props: {
    factor: String,
    bid: Number,
    dateRange: String
  },
  methods: {
    loadData() {
      // if (!this.bid || !this.dateRange) {
      //   this.tableData = [];
      //   return;
      // }
      if (!this.bid) {
        this.tableData = [];
        return;
      }
      let paramDateRange = this.dateRange;
      if (!paramDateRange) {
        let d = new Date();
        paramDateRange = `${d.getFullYear()}-${d.getMonth() +
          1}-${d.getDate()} ${d.getFullYear()}-${d.getMonth() +
          1}-${d.getDate()}`;
      }
      loadBBXTableData(this.bid, paramDateRange).then(res => {
        if (res.status === 200) {
          this.originData = res.data;
          this.rebuildTableData();
        }
      });
    },
    rebuildTableData() {
      if (!this.factor) {
        this.tableData = [];
        return;
      }
      if (this.originData.length > 0) {
        var tmp = [];
        for (let x of this.originData) {
          let obj = {};
          obj.nowdate = x.nowdate;
          obj.lat = x.lat;
          obj.lon = x.lon;
          obj["factor"] = x[this.factor];
          if (!isNaN(obj.factor)) obj.factor = Math.floor(obj.factor * 10) / 10;
          tmp.push(obj);
        }
        this.hasData = tmp.length > 0;
        this.tableData = tmp;
      }
    }
  }
};
</script>

<style scoped>
.table-cell {
  text-align: left;
}
.container {
  font-family: "微软雅黑";
  transition: 0.5s;
}
.panel-default > .panel-heading {
  background-color: rgb(33, 108, 81) !important;
  color: aliceblue !important;
  font-size: 2em;
  font-weight: bold;
  text-shadow: 2px 2px 10px #000;
}
.panel-default > .panel-body {
  padding: 0;
}
td,
th {
  padding-left: 5px;
}
.table-index {
  font-size: larger;
  font-weight: border;
  font-family: black;
}
.panel {
  border-style: none;
}
table {
  cursor: pointer;
}
.panel-body {
  box-shadow: 0 2px 10px rgb(229, 238, 238);
}
</style>


