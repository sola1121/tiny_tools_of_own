function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


// 获取cookie中的对应名称的cookie的值
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');   // 获取到cookie中CSRF值


// 基于Jquery的异步请求在每次请求前自动从cookie中获取CSRF验证传递
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


// 获取URL中的对应名称的条件的值
function getQueryString(name){
    var urlQuery = window.location.search;
    var reg = new RegExp('(^|&)' + name + '=([^&]*)(&|$)', 'i');
    var result = urlQuery.substr(1).match(reg);
    if (result != null && result != undefined){
        return unescape(decodeURIComponent(result[2]));
    }
    return '';
}

// 根据Object(一个类似字典或者说json格式)的数据对象, 将会把key转化为参数名,其值转换为对应值, 生成get字符串, queryNum是这个字典的长度
function generateQuery(dict, queryNum) {
    var queryString = "?", count = 1, flag = 0;
    for (var key in dict) {
        if (dict[key]) {flag++;}
        queryString += key + "=" + (dict[key]?dict[key]:'') + (queryNum>count?'&':'');
        count ++;
    }
    if (flag>0){
        return queryString;
    } else {
        return '';
    }
}
