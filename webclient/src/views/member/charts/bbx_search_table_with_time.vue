<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="panel panel-default">
          <!-- Default panel contents -->
          <div class="panel-heading">数据详情</div>
          <div class="panel-body">
            <!-- Table -->
            <table class="table table-striped table-bordered" v-show="hasData">
              <thead>
                <th>index</th>
                <th>dt</th>
                <th>lat</th>
                <th>lon</th>
                <th>val</th>
              </thead>
              <tbody>
                <tr v-for="(row,idx) in tableData" :key="idx">
                  <td>{{idx}}</td>
                  <td>{{row.nowdate}}</td>
                  <td>{{row.lat}}</td>
                  <td>{{row.lon}}</td>
                  <td>{{row.factor}}</td>
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
      if (!this.bid || !this.dateRange) {
        this.tableData = [];
        return;
      }
      loadBBXTableData(this.bid, this.dateRange).then(res => {
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

