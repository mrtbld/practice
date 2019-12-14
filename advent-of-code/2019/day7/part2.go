package main

import (
	"errors"
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

const N = 5

const (
	instAdd = 1
	instMul = 2
	instIn  = 3
	instOut = 4
	instJIT = 5
	instJIF = 6
	instLT  = 7
	instEq  = 8
	instEnd = 99
)

var done = errors.New("done")

func read(mem []int, modes [3]int, pos, offset int) int {
	switch modes[offset-1] {
	case 0:
		return mem[mem[pos+offset]]
	case 1:
		return mem[pos+offset]
	default:
		panic(fmt.Errorf("unknown mode %d", modes[offset-1]))
	}
}

func run(intcodes []int, in chan int, out chan<- int, e chan<- error) {
	mem := make([]int, len(intcodes))
	copy(mem, intcodes)

	var modes [3]int
	var i int

	r := func(offset int) int {
		return read(mem, modes, i, offset)
	}

	w := func(offset int, value int) {
		mem[mem[i+offset]] = value
	}

	for i = 0; i < len(mem); i++ {
		instruction := mem[i] % 100
		modes = [3]int{
			(mem[i] / 100) % 10,
			(mem[i] / 1000) % 10,
			(mem[i] / 10000) % 10,
		}

		switch instruction {
		case instAdd:
			w(3, r(1)+r(2))
			i += 3
		case instMul:
			w(3, r(1)*r(2))
			i += 3
		case instIn:
			in <- 0
			w(1, <-in)
			i += 1
		case instOut:
			out <- r(1)
			i += 1
		case instEnd:
			e <- done
			return
		case instJIT:
			if r(1) != 0 {
				i = r(2) - 1
			} else {
				i += 2
			}
		case instJIF:
			if r(1) == 0 {
				i = r(2) - 1
			} else {
				i += 2
			}
		case instLT:
			if r(1) < r(2) {
				w(3, 1)
			} else {
				w(3, 0)
			}
			i += 3
		case instEq:
			if r(1) == r(2) {
				w(3, 1)
			} else {
				w(3, 0)
			}
			i += 3
		default:
			e <- fmt.Errorf("not a valid instruction at position %d: %d", i, mem[i])
			return
		}
	}
	e <- fmt.Errorf("halt instruction not found")
}

type ampChans struct {
	in  chan int
	out chan int
	e   chan error
}

func runAmps(intcodes []int, phases []int, result chan<- int) {
	doneChan := make(chan struct{})

	chans := make([]ampChans, len(phases))
	for i, _ := range phases {
		chans[i] = ampChans{
			in:  make(chan int),
			out: make(chan int, 1),
			e:   make(chan error, 1),
		}
	}

	for i, p := range phases {
		go func(phase int, c ampChans, prevOut <-chan int) {
			select {
			case <-c.in:
				c.in <- phase
			case err := <-c.e:
				if !errors.Is(err, done) {
					panic(err)
				}
				panic("done before phasing")
			}

			for {
				select {
				case <-c.in:
					c.in <- <-prevOut
				case err := <-c.e:
					if !errors.Is(err, done) {
						panic(err)
					}
					doneChan <- struct{}{}
					return
				}
			}
		}(p, chans[i], chans[(i+len(chans)-1)%len(chans)].out)
	}

	lastOut := chans[len(chans)-1].out
	lastOut <- 0

	for i, _ := range phases {
		c := chans[i]
		go run(intcodes, c.in, c.out, c.e)
	}

	ended := 0
	for ended != len(phases) {
		select {
		case <-doneChan:
			ended += 1
		}
	}
	result <- <-lastOut
}

func permutations(values []int) [][]int {
	if len(values) == 1 {
		return [][]int{values}
	}
	p := [][]int{}
	for i, v := range values {
		remaining := make([]int, len(values)-1)
		k := 0
		for j, r := range values {
			if i == j {
				continue
			}
			remaining[k] = r
			k++
		}
		for _, sub := range permutations(remaining) {
			p = append(p, append(sub, v))
		}
	}
	return p
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

	values := make([]int, N)
	for i := 0; i < N; i++ {
		values[i] = 5 + i
	}

	phasess := permutations(values)
	r := make(chan int, 1000)
	for _, phases := range phasess {
		go runAmps(intcodes, phases, r)
	}

	var highest int
	for i := 0; i < len(phasess); i++ {
		select {
		case result := <-r:
			if result > highest {
				highest = result
			}
		}
	}
	fmt.Println(highest)
}
