<template>

</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";

@Component
export default class About extends Vue {
  msg:number = 123;

  mounted() {
    this.greet();
  }

  get computedMsg() {
    return "computed" + this.msg;
  }

  greet() {
    alert("greeting:" + this.msg);
  }
}
</script>

<style>
</style>
