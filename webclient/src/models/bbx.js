// 船舶状态信息
export function BBXStateInfo(code, name, state) {
  this.code = code;
  this.name = name;
  this.state = state;
}

export function BBXTrackInfo(id, code, start, end, latlngs, speeds) {
  this.id = id;
  this.code = code;
  this.start = start;
  this.end = end;
  this.latlngs = latlngs;
  this.speeds = speeds;
}
