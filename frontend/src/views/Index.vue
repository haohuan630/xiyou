<template>
  <div class="index cpt-s content_h">
    <div>
      <el-select
        size="small"
        v-model="id1"
        placeholder="请选择"
        @change="option1"
        style="margin-right:20px"
      >
        <el-option v-for="item in areas_list1" :key="item.id" :label="item.name" :value="item.id"></el-option>
      </el-select>
      <el-select
        v-model="id2"
        size="small"
        placeholder="请选择"
        @change="option2"
        style="margin-right:20px"
      >
        <el-option v-for="item in areas_list2" :key="item.id" :label="item.name" :value="item.id"></el-option>
      </el-select>
      <el-select
        v-model="id3"
        size="small"
        placeholder="请选择"
        @change="option3"
        style="margin-right:20px"
      >
        <el-option v-for="item in areas_list3" :key="item.id" :label="item.name" :value="item.id"></el-option>
      </el-select>
    </div>
    <div style="margin-top: 30px">
      <el-table
        :data="info_data"
        border
        header-row-class-name="common-table-header"
        header-cell-class-name="common-table-header"
        cell-class-name="common-table-cell"
        style="width: 100%"
      >
        <el-table-column
          :width="flexColumnWidth(item.label)" 
          :show-overflow-tooltip="true"
          :prop="item.prop"
          :label="item.label"
          :key="index+''"
          v-for="(item,index) in info_head_list"
        >
          <!-- <template slot-scope="scope" v-if="item.prop == '1'">
            <el-button @click="handleClick(scope.row)" type="text" size="small">查看详情</el-button>
          </template> -->
        </el-table-column>
        <el-table-column 
        :width="flexColumnWidth('datail')"
        align="center" label="操作">
          <template slot-scope="scope">
            <el-button @click="handleClick(scope.row)" type="text" size="small">查看详情</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import ELineBar from "@/components/echarts/ELineBar.vue";
import { api } from "@/api";
export default {
  name: "index",
  components: {
    ELineBar
  },
  data() {
    return {
      id1: "", // 第一级数据id
      id2: "", // 第二级数据id
      id3: "", // 第三级数据id
      areas_list1: [], // 第一级数据
      areas_list2: [], // 第一级数据
      areas_list3: [], // 第一级数据
      info_data: [], // 人员信息数据
      info_head_list: [
        {
          label: "姓名",
          prop: "name"
        },
        {
          label: "邮箱",
          prop: "email"
        },
        {
          label: "访问量",
          prop: "views"
        },
        {
          label: "简介",
          prop: "brief_intro"
        },
      ]
    };
  },
  computed: {},
  //监控data中的数据变化
  watch: {
    id1: {
      immediate: true,
      handler: function(newVal) {
        if (this.isRealNum(newVal)) {
          // console.log("newVal", newVal);
          this.option1(newVal);
        }
      }
    },
    id2: {
      immediate: true,
      handler: function(newVal) {
        if (this.isRealNum(newVal)) {
          // console.log("newVal", newVal);
          this.option2(newVal);
        }
      }
    },
    id3: {
      immediate: true,
      handler: function(newVal) {
        if (this.isRealNum(newVal)) {
          // console.log("newVal", newVal);
          this.option3(newVal);
        }
      }
    }
  },
  //方法集合
  methods: {
    init() {
      // 初始化获取第一级数据
      api.getPerentArea().then(
        success => {
          console.log("123", success.data);
          this.areas_list1 = success.data;
          if (success.data) {
            this.id1 = success.data[2].name;
            // this.option2(success.data[2].id)
            // 初始化获取第二级数据
            api.getSubsArea({ id: success.data[2].id }).then(success => {
              this.areas_list2 = success.data.subs;
              if (success.data) {
                this.id2 = success.data.subs[0].name;
                // this.option3(success.data.subs[0].id)
                // 初始化获取第三级数据
                api.getSubsArea({ id: success.data.subs[0].id })
                  .then(success => {
                    this.areas_list3 = success.data.subs;
                    if (success.data) {
                      this.id3 = success.data.subs[0].name;
                      this.getInfo(success.data.subs[0].id)
                    }
                  });
              }
            });
          }
        },
        error => {
          console.log("error");
        }
      );
    },
    option1(e) {
      this.id1 = e;
      api.getSubsArea({ id: e }).then(success => {
        this.areas_list2 = success.data.subs;
        this.id2 = success.data.subs[0].id;
      });
    },
    option2(e) {
      api.getSubsArea({ id: e }).then(success => {
        this.areas_list3 = success.data.subs;
        this.id3 = success.data.subs[0].id;
      });
    },
    option3(e) {
      // console.log("option3", e)
      this.getInfo(e)
    },

    // 获取人员详情
    getInfo(e){
      api.getPersonInfo({"id": e}).then(success => {
        this.info_data = success.data
        console.log("1111111111222222222222222", success.data)
      })
    },

    // 查看人员详情
    handleClick(e) {
      console.log("eeeeeeeeeeeeeeeeee", e.url)
      // window.localtion.href = e.url
      window.open(e.url, "_blank");
    },

    // 自定义表格列宽
    flexColumnWidth(str) {
      let flexWidth = 0
      if (str != '简介') {
        if (str == '邮箱'){
          flexWidth = 160 + 'px'
        }else {
          flexWidth = 100 + 'px'
        }
      }

      // if (flexWidth < 50) {
      //   // 设置最小宽度
      //   flexWidth = 100
      // }
      // if (flexWidth > 250) {
      //   // 设置最大宽度
      //   flexWidth = 250
      // }
      return flexWidth
    },

    isRealNum(val) {
      // isNaN()函数 把空串 空格 以及NUll 按照0来处理 所以先去除
      if (val === "" || val == null) {
        return false;
      }
      if (!isNaN(val)) {
        return true;
      } else {
        return false;
      }
    }
  },
  created() {
    this.init();
  },
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
</style>