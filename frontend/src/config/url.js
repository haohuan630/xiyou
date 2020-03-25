let baseUrl_config = {
  development: "http://150.158.113.76",
  production: "http://150.158.113.76",
}
let port = {
  development: 8000,
  production: 8000,
}
let needPort = {
  development: true,
  production: true
}
let path = {
  development: '/api',
  production: '/api',
}

function baseUrlsplitJoint() {
  for (let key in baseUrl_config) {
    if (needPort[key]) {
      baseUrl_config[key] += ":"
      baseUrl_config[key] += port[key]
    }
    baseUrl_config[key] += path[key]
  }
}

baseUrlsplitJoint()

// 获取 当前环境 baseUrl_config中的值
let env = process.env.NODE_ENV
let baseUrl = baseUrl_config[env]
export {
  baseUrl,
}
