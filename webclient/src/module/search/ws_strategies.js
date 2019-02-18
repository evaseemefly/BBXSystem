// 风向风速的策略这模式

// 使用策略模式
var strategies = {
  w: function(list) {
    var columns = [];
    var values = [];
    list.forEach(obj => {
      /*
      后端返回的结果
      1- 存在时
      {
         "timestamp": "2018-12-30 16:00:00",
         "val": {
                  "ws": 0,
                  "wd": 60
                }
      }

      2- 不存在时：
      {
        "timestamp": "2018-12-01 00:00:00",
        "val": {}
      }
      */
      // 1- 先判断val是否包含ws与wd
      if (obj.val["ws"] != null && obj.val["wd"] != null) {
        if (
          (obj.val.ws != 9999 && obj.val.ws != 999.9) ||
          (obj.val.wd != 9999 && obj.val.wd != 999.9)
        ) {
          //如果数据为缺省值那么就改成0
          values.push({
            value: obj.val.ws,
            symbolRotate: obj.val.wd
          });
          columns.push(obj.timestamp);
        } else {
          values.push(null);
          columns.push(obj.timestamp);
        }
      }
    });
    return {
      columns: columns,
      values: values
    };
  },
  default: function(list) {
    var columns = [];
    var values = [];
    list.forEach(obj => {
      // myself.values.push(obj.val);
      // myself.columns.push(obj.timestamp);
      if (obj.val != 9999 && obj.val != 999.9) {
        //如果数据为缺省值那么就改成0
        values.push(obj.val);
        columns.push(obj.timestamp);
      } else {
        values.push(null);
        columns.push(obj.timestamp);
      }
    });
    return {
      columns: columns,
      values: values
    };
  }
};
export const strategyAppendRealtimeData = function(factor, list) {
  return strategies[factor](list);
};
