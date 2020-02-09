// js读取本地文件, 基于ajax
function readJsonFile(file, callback) {
    var rawFile = new XMLHttpRequest();
    rawFile.overrideMimeType("application/json");   // 用于读取json文件, mime类型参数覆盖到"text/html"，"text/plain可以读取html, text
    rawFile.open("GET", file, true);   // 注意这里是否需要异步进行
    rawFile.onreadystatechange = function () {
        if (rawFile.readyState === 4 && rawFile.status == "200") {
            callback(rawFile.responseText);
        }
    };
    rawFile.send(null);
}
// 调用方式
readJsonFile("./data/config.json", function(text){
    var data = JSON.parse(text);
    console.log(data);
});
