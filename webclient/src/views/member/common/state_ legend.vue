<template>
  <div>
    <div class="card mb-4 col-md-4 box-shadow">
      <div class="row">
        <div class="cell ok">
          正常
        </div>
        <div id="">
          <span>小于24h</span>
        </div>
      </div>
      <div class="row">
        <div class="cell noarrival">
          迟到
        </div>
        <div id="">
          <span>小于48h</span>
        </div>
      </div>
      <div class="row">
        <div class="cell late">
          未到
        </div>
        <div id="">
          <span>小于72h</span>

        </div>
      </div>
      <div class="row">
        <div class="cell invalid">
          缺失
        </div>
        <div id="">
          <span>超过72小时</span>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style scoped>
.row {
  text-align: center;
  /* text-shadow: 2px 2px 10px grey; */
  margin-bottom: 10px;
  display: flex;
  flex-direction: row;
  /* color: white; */
}
.row div {
  display: flex;
}
/* 注意card有一个左右15px的padding */
span {
  color: white;
  margin-top: 10px;
}
.card {
  padding-left: 0px;
  padding-right: 0px;
  position: absolute;
  bottom: 100px;
  left: 100px;
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
</style>
