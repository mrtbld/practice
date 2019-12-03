package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func run(intcodes []int, noun int, verb int) (int, error) {
	mem := make([]int, len(intcodes))
	copy(mem, intcodes)

	mem[1] = noun
	mem[2] = verb

	for i := 0; i < len(mem); i++ {
		switch mem[i] {
		case 1:
			mem[mem[i+3]] = mem[mem[i+1]] + mem[mem[i+2]]
			i += 3
		case 2:
			mem[mem[i+3]] = mem[mem[i+1]] * mem[mem[i+2]]
			i += 3
		case 99:
			return mem[0], nil
		default:
			return 0, fmt.Errorf("not an opcode at position %d: %d", i, mem[i])
		}
	}
	return 0, fmt.Errorf("halt instruction not found")
}

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

	for noun := 0; noun < 100; noun++ {
		for verb := 0; verb < 100; verb++ {
			output, err := run(intcodes, noun, verb)
			if err != nil {
				continue
			}
			if output == 19690720 {
				fmt.Printf("%d%d\n", noun, verb)
				return
			}
		}
	}
	fmt.Println("failed to found target output")
}
