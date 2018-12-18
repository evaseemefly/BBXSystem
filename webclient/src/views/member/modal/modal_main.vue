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
          <h4 class="modal-title">船舶编号</h4>
        </div>
        <div class="modal-body">
          <div>
            <ul
              id="mytabs"
              class="nav nav-tabs"
            >
              <li
                v-for="item in menulist"
                role="presentation"
                class="active"
              >
                <a href="#">{{item.name}}</a>
              </li>
            </ul>
            <!-- <div
              id="main"
              style=""
            ></div> -->
            <bbxObservation></bbxObservation>
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
export default {
  //modal框主体部分
  data () {
    return {
      menulist: [
        {
          name: '降水',
          code: '',
          url: ''
        },
        {
          name: '能见度',
          code: '',
          url: ''
        },
        {
          name: '风向',
          code: '',
          url: ''
        }, {
          name: '降水',
          code: '',
          url: ''
        }
      ]
    }
  },
  components: {
    bbxObservation
  },
  methods: {
    showModal: function () {
      console.log('显示modal窗');
      $("#mymodal").modal();
    },
    initCharts: function () {

    }
  }

}
</script>

<style>
</style>
