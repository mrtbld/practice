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

	var sum int
	masses := bytes.Split(data, []byte("\n"))
	for _, m := range masses {
		if len(m) == 0 {
			continue
		}
		n, err := strconv.Atoi(string(m))
		if err != nil {
			panic(err)
		}
		sum += (n / 3) - 2
	}
	fmt.Println(sum)
}
