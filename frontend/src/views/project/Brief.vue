<template>
  <div class="Brief">
    <h3>一、项目描述</h3>
    <!-- https://github.com/haohuan630/xiyou   https://cli.vuejs.org/zh/guide/cli-service.html -->
    <p>1. 本项目由github托管：<el-link type="primary" href="https://github.com/haohuan630/xiyou" target="_blank">https://github.com/haohuan630/xiyou</el-link>。</p>
    <p>2. 本网站的数据主要来源于<el-link type="primary" href="http://gr.xupt.edu.cn/xbwz/zsxx/dsjj.htm" target="_blank">西安邮电大学研究生导师简介</el-link>。
    本网站属于个人网站，本网站的所有数据均无商业用途。若有违反规定或不妥之处，请及时联系本人，并删除。</p>
     
    <el-divider></el-divider>
    <h3>二、前/后端技术</h3>
    <p>前端项目使用Vue.js框架以及ElementUI库，通过使用Vue CLI3.0
      <!-- <el-link type="primary" href="https://cli.vuejs.org/zh/guide/cli-service.html" target="_blank">Vue CLI3.0</el-link> -->
      （vue脚手架）搭建项目。后端项目使用Django框架。采用前后端分离的形式进行项目开发。</p>
    
    <el-divider></el-divider>
    <h3>三、数据库</h3>
    <p>本项目数据库使用Mysql数据库。共创建三张表：t_areas, t_persons, t_collect。其关系如下图（三级联动和多对多关联）：</p>
    <div class="db_img">
      <img :src="src" alt="" srcset="" width="100%">
      <!-- <img :src="src"> -->
    </div>

    <el-divider></el-divider>
    <h3>四、数据来源</h3>
    <p>本项目的数据是使用python库requests对<el-link type="primary" href="http://gr.xupt.edu.cn/xbwz/zsxx/dsjj.htm" target="_blank">西安邮电大学研究生导师简介</el-link>
        信息进行爬取，并进行数据清洗入库。
    </p>

    <el-divider></el-divider>
    <h3>五、项目部署</h3>
    <p>本项目部署在腾讯云服务器上。部署环境：Ubuntu18.04、 Nginx、Uwsgi、Python3.7、Mysql5.7、Django2.1.8、虚拟环境(xiyou)等。</p>




    
    
    



  </div>
</template>

<script>
export default {
  name: "Brief",
  components: {},
  data() {
    return {
      src:require('../../assets/database.png')
    };
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
.Brief {
  font-size: 14px;
  h3 {
    margin-bottom: 5px;
  }
  p {
    padding-left: 20px;
  }

  .db_img {
    padding-left: 100px;
    max-width: 600px;
    max-height: 400px;
  }
}
</style>