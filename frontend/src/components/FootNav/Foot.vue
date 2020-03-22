<template>
  <div class="FootNav">
    <div class="content_h">
      <h3>说明:</h3>
      <p>1. 本网站的数据主要来源于<el-link type="primary" href="http://gr.xupt.edu.cn/xbwz/zsxx/dsjj.htm" target="_blank">西安邮电大学研究生导师简介</el-link>。</p>
      <p>2. 本网站属于个人网站，本网站的所有数据均无商业用途。若有违反规定或不妥之处，请及时联系本人，并删除。</p>
      <p>3. 由于个人技术还在学习过程中，在爬取、清洗数据过程中有部分数据丢失。即所有数据并无参考作用，以官网发布数据为准。</p>
      <p>4. 本网站的目的主要是个人对专业知识的学习和研究之用，也有许多的不足之处，欢迎大牛批评指正交流。</p>
      <p>5. 电话：15565857009； 邮箱：haohuan630@163.com </p>
    </div>
    
  </div>
</template>

<script>
export default {
  name: "FootNav",
  components: {},
  data() {
    return {};
  },
  computed: {},
  //监控data中的数据变化
  watch: {},
  //方法集合
  methods: {},
  created() {},
  mounted() {},
  beforeCreate() {},
  beforeMount() {},
  beforeUpdate() {},
  updated() {},
  beforeDestroy() {},
  destroyed() {},
  // 如果页面有keep-alive缓存功能，这个函数会触发
  activated() {}
};
</script>
<style lang='scss' scoped>
.FootNav {
  margin-top: 60px;
  padding: 30px 0 50px 0;
  min-height: 250px;
  // text-align: center;
  background: #00005B;
  font-size: 14px;
  color: white;

  h3 {
    padding: 30px 0 0 60px;
  }
  p {
    padding: 0 0 0 100px;
  }

}
</style>