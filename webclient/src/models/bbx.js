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

// 海区状态
export function AreaStatisticsInfo(id, area, name, state) {
  this.id = id;
  this.area = area;
  this.name = name;
  this.state = state;
  // this.normal = normal;
  // this.late = late;
  // this.noarrival = noarrival;
  // this.invalid = invalid;
}

export function StatesInfo(normal, late, noarrival, invalid) {
  this.normal = normal;
  this.late = late;
  this.noarrival = noarrival;
  this.invalid = invalid;
}
