import axios from 'axios'

// 后端的请求地址及端口
export const host = 'http://127.0.0.1:8000'
// export const host = "http://192.168.139.128:8015";
// export const host = "http://128.5.6.112:8015";

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
export const loadBBXStateList: any = (par: any) => {
  let bbxstateUrl = `${host}/bbx/statelist`
  return axios.get(bbxstateUrl, {
    params: par
  })
}
export const loadBBXGPS = (par: any) => {
  let bbxgpsUrl = `${host}/gis/gps`
  return axios.get(bbxgpsUrl, { params: par })
}
export const loadBBXNowList = (par: any) => {
  let bbxnowUrl = `${host}/gis/bbxspace`
  return axios.get(bbxnowUrl)
}

// 获取当前时间24小时范围内的全部船舶列表
export const loadBBXlistByNow = (par: any) => {
  let bbxTrackUrl = `${host}/bbx/areaalllist`
  return axios.get(bbxTrackUrl, { params: par })
}
export const loadBBXTrack = (par: any) => {
  let bbxTrackUrl = `${host}/bbx/track`
  return axios.get(bbxTrackUrl, { params: par })
}

//加载指定船舶的指定时间的指定要素的观测值
export const loadObservationData = (par: any) => {
  let dataUrl = `${host}/bbx/detail`
  return axios.get(dataUrl, { params: par })
}

// 加载指定海区的船舶列表
export const loadBBXList = (par: any) => {
  let bbxlistUrl = `${host}/bbx/list`
  return axios.get(bbxlistUrl, { params: par })
}

// 获取指定bbx的指定时间的指定要素的观测列表
export const loadRealtime = (par: any) => {
  let realtimeUrl = `${host}/bbx/facotrlist`
  return axios.get(realtimeUrl, { params: par })
}

export const loadAllAreaStatistic = (par: any) => {
  let bbxlistUrl = `${host}/bbx/areastatelist`
  return axios.get(bbxlistUrl, { params: par })
}

export const loadBBXState = (area: string, time: string) => {
  let bbxStateUrl = `${host}/bbx/GetBaseState/${area}/${time}`
  return axios.get(bbxStateUrl)
}
