import axios from 'axios'

// 后端的请求地址及端口
export const host = 'http://127.0.0.1:8000'

axios.defaults.withCredentials = true
axios.defaults.headers = {
  // 'Access-Control-Allow-Headers': 'Authorization,Origin, X-Requested-With, Content-Type, Accept,access-control-allow-methods,access-control-allow-origin',
  // 'Access-Control-Allow-Headers': 'Content-Type',
  // 'Content-Type': 'application/json;charset=UTF-8',
  // 'Content-Type': 'application/x-www-form-urlencoded',
  // 'Access-Control-Allow-Origin': '*',
  // 'Access-Control-Allow-Methods': 'GET, POST, OPTIONS, PUT, PATCH, DELETE'
}
// 加载船舶状态信息列表
export const loadBBXStateList = par => {
  let bbxstateUrl = `${host}/bbx/statelist`
  return axios.get(bbxstateUrl, {
    params: par
  })
}
export const loadBBXGPS = par => {
  let bbxgpsUrl = `${host}/gis/gps`
  return axios.get(bbxgpsUrl, {
    params: par
  })
}
export const loadBBXNowList = par => {
  let bbxnowUrl = `${host}/gis/bbxspace`
  return axios.get(bbxnowUrl)
}
// 加载指定海区的船舶列表
export const loadBBXList = par => {
  let bbxlistUrl = `${host}/bbx/list`
  return axios.get(bbxlistUrl, {
    params: par
  })
}
export const loadBBXState = (area, time) => {
  let bbxStateUrl = `${host}/bbx/GetBaseState/${area}/${time}`
  return axios.get(bbxStateUrl)
}
