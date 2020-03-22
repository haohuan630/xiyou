const Test = () => import('@/views/Test.vue')

const Login = () => import('@/views/Login.vue')
const NotFound = () => import('@/views/NotFound.vue')

const Home = () => import('@/views/Home.vue')
const Index = () => import('@/views/Index.vue')

const TopNav = () => import('@/components/TopNav')
const LeftNav = () => import('@/components/LeftNav')
const FootNav = () => import('@/components/FootNav')


const MySettings = () => import('@/views/setting/MySetting.vue')
const Info = () => import('@/views/setting/Info.vue')
const Setting = () => import('@/views/setting/Setting.vue')

const Brief = () => import('@/views/project/Brief.vue')
// const Validate = () => import('@/views/project/Validate.vue')

const routes = [{
    path: '/login',
    name: 'login',
    component: Login,
    meta: {
      icon: 'el-icon-menu',
      title: "登录"
    }
  },
  {
    path: '*',
    component: NotFound
  },
  // {
  //   path: '/',
  //   name: 'foot',
  //   component: FootNav,
  // },
  {
    path: '/',
    name: 'home',
    redirect: '/index',
    component: Home,
    meta: {
      icon: 'el-icon-menu',
      title: "首页",
      isTopMenu: true,
    },
    children: [{
        path: '/index',
        name: 'index',
        components: {
          default: Index,
          top: TopNav,
          aside: LeftNav,
          foot: FootNav,
        },
        meta: {
          title: "工作台",
          icon: 'el-icon-menu', // 图标样式class
        }
      },
    ]
  },
  {
    path: '/project',
    name: 'project',
    component: Home,
    redirect: '/project/list',
    meta: {
      icon: 'el-icon-menu',
      title: "项目管理",
      isTopMenu: true
    },
    children: [{
      path: '/project/list',
      name: 'Brief',
      components: {
        default: Brief,
        top: TopNav,
        aside: LeftNav
      },
      meta: {
        icon: 'el-icon-menu',
        title: "项目简介"
      },
    }, {
      path: '/project/myset',
      name: 'mySet',
      components: {
        default: MySettings,
        top: TopNav,
        aside: LeftNav
      },
      meta: {
        icon: 'el-icon-menu',
        icon: 'el-icon-menu',
        title: "我的设置"
      },
      children: [{
        path: 'info',
        component: Info,
        name: 'info',
        meta: {
          icon: 'el-icon-menu',
          icon: 'el-icon-menu',
          title: "个人信息"
        }
      }, {
        path: 'setting',
        component: Setting,
        name: 'Setting',
        meta: {
          icon: 'el-icon-menu',
          icon: 'el-icon-menu',
          title: "设置"
        }
      }]
    }]
  }
]

export {
  routes
}