package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"strconv"
)

func main() {
	data, err := ioutil.ReadFile("./input")
	if err != nil {
		panic(err)
	}

	var fuel int
	for _, m := range bytes.Split(data, []byte("\n")) {
		if len(m) == 0 {
			continue
		}
		n, err := strconv.Atoi(string(m))
		if err != nil {
			panic(err)
		}
		for i := (n / 3) - 2; i > 0; i = (i / 3) - 2 {
			fuel += i
		}
	}

	fmt.Println(fuel)
}
