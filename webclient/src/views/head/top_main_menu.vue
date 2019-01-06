
<template>
  <div>
    <nav class="navbar navbar-default navbar-fixed-top navbar-inverse">
      <div class="container-fluid bbx-title-bar">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
          <button
            type="button"
            class="navbar-toggle collapsed"
            data-toggle="collapse"
            data-target="#bs-example-navbar-collapse-1"
            aria-expanded="false"
          >
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a
            class="navbar-brand"
            href="#"
          >志愿船舶显示系统</a>
        </div>

        <!-- Collect the nav links, forms, and other content for toggling -->
        <div
          class="collapse navbar-collapse"
          id="bs-example-navbar-collapse-1"
        >
          <ul class="nav navbar-nav">
            <li class="active">
              <!-- <a href="#">船舶地图<span class="sr-only">(current)</span></a> -->
              <router-link to="/map">船舶地图</router-link>
            </li>
            <li>
              <!-- <a href="#">状态显示</a> -->
              <router-link to="/state">船舶状态</router-link>
            </li>
            <li>
              <!-- <a href="#">数据查询</a> -->
              <router-link to="/search">实时数据查询</router-link>
            </li>
            <li>
              <!-- <a href="#">数据查询</a> -->
              <router-link to="/searchWithTime">历史数据查询</router-link>
            </li>
          </ul>
        </div>
        <!-- /.navbar-collapse -->
      </div>
      <!-- /.container-fluid -->
    </nav>
  </div>
</template>

<script>
export default {
  mounted: function () {
    let li = document.querySelectorAll(".navbar-nav li");
    li.forEach(x => {
      x.onclick = function () {
        li.forEach(function (l) {
          l.classList = [];
        });
        this.classList.add("activedli");
      };
    });
    li[0].click();
  }
};
</script>

<style scoped>
.bbx-title-bar {
  /* background: linear-gradient(to right, #1a6865, #2c3e50); */
  background: linear-gradient(to right, #1a6865 30%, rgba(4, 107, 114, 0.639));
}
.navbar-nav li {
  transition: 0.3s;
}
.navbar-brand {
  color: rgba(254, 203, 0, 0.934) !important;
  font-weight: bolder;
  text-shadow: 2px 2px 10px #000;
}
.navbar-nav > li > a {
  color: rgba(254, 233, 0, 0.851) !important;
  font-weight: bolder;
  text-shadow: 2px 2px 10px #000;
}
.activedli {
  background: #143b4d;
  transform: scale(1.1);
  box-shadow: 0px 1px 2px black;
}
</style>
