var map = new AMap.Map('container', {
    viewMode: '2D', // 默认使用 2D 模式，如果希望使用带有俯仰角的 3D 模式，请设置 viewMode: '3D',
    zoom: 11, //初始化地图层级
    center: [106.315279, 29.420825] //初始化地图中心点: 交大
})

function btnClicked() {
    var ic = document.getElementById("input-card");
    if (ic.classList.contains("input-card-hide")) {
        ic.classList.remove("input-card-hide");
    } else {
        ic.classList.add("input-card-hide")
    }
}

var selectedBridge;
