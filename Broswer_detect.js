// PPK中使用的判断方式
var BrowserDetect = {
    init: function () {
        this.browser = this.searchString(this.dataBrowser) || "An unknown browser";
        this.version = this.searchVersion(navigator.userAgent)
            || this.searchVersion(navigator.appVersion)
            || "an unknown version";
        this.OS = this.searchString(this.dataOS) || "an unknown OS";
    },
    searchString: function (data) {
        for (var i=0;i<data.length;i++)    {
            var dataString = data[i].string;
            var dataProp = data[i].prop;
            this.versionSearchString = data[i].versionSearch || data[i].identity;
            if (dataString) {
                if (dataString.indexOf(data[i].subString) != -1)
                    return data[i].identity;
            }
            else if (dataProp)
                return data[i].identity;
        }
    },
    searchVersion: function (dataString) {
        var index = dataString.indexOf(this.versionSearchString);
        if (index == -1) return;
        return parseFloat(dataString.substring(index+this.versionSearchString.length+1));
    },
    dataBrowser: [
        {
            string: navigator.userAgent,
            subString: "Chrome",
            identity: "Chrome"
        },
        {     string: navigator.userAgent,
            subString: "OmniWeb",
            versionSearch: "OmniWeb/",
            identity: "OmniWeb"
        },
        {
            string: navigator.vendor,
            subString: "Apple",
            identity: "Safari",
            versionSearch: "Version"
        },
        {
            prop: window.opera,
            identity: "Opera"
        },
        {
            string: navigator.vendor,
            subString: "iCab",
            identity: "iCab"
        },
        {
            string: navigator.vendor,
            subString: "KDE",
            identity: "Konqueror"
        },
        {
            string: navigator.userAgent,
            subString: "Firefox",
            identity: "Firefox"
        },
        {
            string: navigator.vendor,
            subString: "Camino",
            identity: "Camino"
        },
        {        // for newer Netscapes (6+)
            string: navigator.userAgent,
            subString: "Netscape",
            identity: "Netscape"
        },
        {
            string: navigator.userAgent,
            subString: "MSIE",
            identity: "Explorer",
            versionSearch: "MSIE"
        },
        {
            string: navigator.userAgent,
            subString: "Gecko",
            identity: "Mozilla",
            versionSearch: "rv"
        },
        {         // for older Netscapes (4-)
            string: navigator.userAgent,
            subString: "Mozilla",
            identity: "Netscape",
            versionSearch: "Mozilla"
        }
    ],
    dataOS : [
        {
            string: navigator.platform,
            subString: "Win",
            identity: "Windows"
        },
        {
            string: navigator.platform,
            subString: "Mac",
            identity: "Mac"
        },
        {
               string: navigator.userAgent,
               subString: "iPhone",
               identity: "iPhone/iPod"
        },
        {
            string: navigator.platform,
            subString: "Linux",
            identity: "Linux"
        }
    ]
 
};
BrowserDetect.init();
document.write('你正在使用的是：' + BrowserDetect.browser + ' ' + BrowserDetect.version + ' on ' + BrowserDetect.OS + '!');


// 方法二: 使用User-Agent判断
var Sys = {};  
var ua = navigator.userAgent.toLowerCase();  
var s;  
(s = ua.match(/msie ([\d.]+)/)) ? Sys.ie = s[1] :  
(s = ua.match(/firefox\/([\d.]+)/)) ? Sys.firefox = s[1] :  
(s = ua.match(/chrome\/([\d.]+)/)) ? Sys.chrome = s[1] :  
(s = ua.match(/opera.([\d.]+)/)) ? Sys.opera = s[1] :  
(s = ua.match(/version\/([\d.]+).*safari/)) ? Sys.safari = s[1] : 0;   

//以下进行测试  
if (Sys.ie) document.write('IE: ' + Sys.ie);  
if (Sys.firefox) document.write('Firefox: ' + Sys.firefox);  
if (Sys.chrome) document.write('Chrome: ' + Sys.chrome);  
if (Sys.opera) document.write('Opera: ' + Sys.opera);  
if (Sys.safari) document.write('Safari: ' + Sys.safari);  

