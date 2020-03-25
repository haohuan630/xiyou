<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: "app",
  components: {}
};
</script>

<style lang="scss">
body,
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 0px;

  // 特殊组件样式
  .el-header {
    padding: 0px;
  }
  .el-footer {
    padding: 0;
  }

  // 内容部分的样式
  .content {
    min-height: 800px;
  }

  // 公共样式
  .common-s {
    .wrap-c {
      padding: 20px;
    }
  }

  // 内容宽度限制
  .content_h {
    max-width: 1200px;
    // background: red;
    margin-left: auto;
    margin-right: auto;
  }

  // 组件样式
  .cpt-s {
    .el-row {
      margin-bottom: 20px;
    }
    .el-col {
      border-radius: 4px;
    }
    .el-card {
      background: #f2f2f2;
    }
  }

  // 表格样式
  .common-table-header {
    background-color: #fafafa;
    color: #333333;
    text-align: center;
  }
  .el-tooltip__popper {
    max-width: 50%;
    font-size: 14px;
  }
  // .common-table-cell {
  //   text-align: center;
  // }

  // 分割线
  .el-divider--horizontal {
    margin: 12px 0;
  }
}
</style>
