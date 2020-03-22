<template>
  <el-container>
    <el-header>
      <router-view name="top"></router-view>
    </el-header>
    <el-container>
      <div>
        <router-view name="aside" v-if="isLeftNav"></router-view>
      </div>
      <el-main class="content">
        <router-view></router-view>
      </el-main>
    </el-container>
    <el-footer>
      <router-view name="foot"></router-view>
    </el-footer>
  </el-container>
</template>

<script>
export default {
  name: "home",
  data() {
    return {};
  },
  methods: {},
  computed: {
    isLeftNav() {
      return this.$route.path == "/index" ? false : true
    }
  },
};
</script>
