package main

import (
	"fmt"
	"net/http"
	"time"
)

func handler(writer http.ResponseWriter, _ *http.Request) {
	time.Sleep(5 * time.Second)
	fmt.Fprint(writer, "Hello World")
}

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":8080", nil)
}
