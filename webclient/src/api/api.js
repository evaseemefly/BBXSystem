import axios from "axios";

// 后端的请求地址及端口
export const host = "http://127.0.0.1:8000";

axios.defaults.withCredentials = true;

// 加载船舶状态信息列表
export const loadBBXStateList = par => {
  let bbxstateUrl = `${host}/bbx/statelist`;
  return axios.get(bbxstateUrl, {
    params: par
  });
};
