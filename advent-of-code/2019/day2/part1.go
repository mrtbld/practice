package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func main() {
	data, err := ioutil.ReadFile("./input")
	if err != nil {
		panic(err)
	}

	rawIntcodes := strings.Split(string(data), ",")
	intcodes := make([]int, len(rawIntcodes))
	for i, v := range rawIntcodes {
		var err error
		intcodes[i], err = strconv.Atoi(strings.TrimSpace(v))
		if err != nil {
			panic(err)
		}
	}

	intcodes[1] = 12
	intcodes[2] = 2

	for i := 0; i < len(intcodes); i++ {
		switch intcodes[i] {
		case 1:
			intcodes[intcodes[i+3]] = intcodes[intcodes[i+1]] + intcodes[intcodes[i+2]]
			i += 3
		case 2:
			intcodes[intcodes[i+3]] = intcodes[intcodes[i+1]] * intcodes[intcodes[i+2]]
			i += 3
		case 99:
			fmt.Println(intcodes[0])
			return
		default:
			panic(fmt.Sprintf("not an opcode: [%d] %d", i, intcodes[i]))
		}
	}
	panic("halting opcode not found")
}
