<template>
  <div class="container">

    <div
      class="panel-body"
      style="padding-bottom:0px;"
    >
      <div class="panel ">
        <div class="panel-heading">查询条件</div>
        <div class="panel-body table-parent-panel searchbar">
          <form
            id="formSearch"
            class="form-horizontal"
          >
            <div
              class="form-group"
              style="margin-top:15px"
            >
              <label
                class="control-label col-sm-1"
                for="txt_search_departmentname"
              >船舶</label>
              <div class="col-md-2">
                <select
                  class="form-control"
                  v-model="selectedBBX"
                >
                  <option
                    v-for='option in optionsBBX_order'
                    :key="option.text"
                    v-bind:value="option.value"
                  >
                    {{option.text}}
                  </option>
                </select>
              </div>
              <label
                class="control-label col-sm-1"
                for="txt_search_departmentname"
              >要素</label>
              <div class="col-md-2">
                <select
                  class="form-control"
                  v-model="selectedFactor"
                >
                  <option
                    v-for='option in optionsFactor'
                    v-bind:value="option.value"
                  >
                    {{option.text}}
                  </option>
                </select>
              </div>
              <div
                class="col-md-2"
                style="text-align:left;"
              ><button
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
// import _ from 'lodash';
import { loadBBXlistByNow } from '../../../api/api.js';
import { optionsFactors } from '../../../module/search/menu_options.js';
export default {
  data () {
    return {
      optionsFactor: optionsFactors,
      optionsBBX: [],
      selectedFactor: null,
      selectedBBX: null,

    }
  },
  methods: {
    summit: function () {
      console.log("提交给后端")
    },
    initFatherParams: function () {
      var myself = this;
      this.$emit('initParams', myself.selectedFactor, myself.selectedBBX);
    },
    loadBBXList: function () {
      var myself = this;
      var params = {
        operation: 'now',
        nowdate: '2018-12-08 00:00'
      }
      loadBBXlistByNow(params).then(res => {
        // console.log(res.data);
        if (res.data[0].area === 'a') {
          res.data[0].bbxlist.forEach(obj => {
            myself.optionsBBX.push({
              text: obj.code,
              value: obj.bid
            })
          })
        }
      })
    }

  },
  mounted: function () {
    // this.optionsBBX.push({
    //   text: 'BBXA',
    //   value: 1
    // })
    this.loadBBXList();
  },
  watch: {
    selectedFactor: function () {
      this.initFatherParams();
    },
    selectedBBX: function () {
      this.initFatherParams();
    }
  },
  computed: {
    optionsBBX_order: function () {
      // return _.orderBy(this.optionsBBX, "text")
      return this.lodash.orderBy(this.optionsBBX, "text");
      // return []
    }
  }

}
</script>

<style scoped>
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
