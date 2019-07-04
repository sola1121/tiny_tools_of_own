package RedirectPkg

import (
	"fmt"
	"net/http"
)

var pkgMeta string = `<meta name="go-import" content="example.com/pkg/foo git https://github.com/pkg/foo">`

/*
* 重定向go get, 或着包导入
 */
func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, pkgMeta)
}

func DoServer() {
	http.HandleFunc("/pkg/foo", handler)
	http.ListenAndServe(":80", nil)
}
