package main

import (
	"errors"
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
	"time"
)

const (
	instAdd = 1
	instMul = 2
	instIn  = 3
	instOut = 4
	instJIT = 5
	instJIF = 6
	instLT  = 7
	instEq  = 8
	instRB  = 9
	instEnd = 99

	modePos = 0
	modeVal = 1
	modeRel = 2
)

var done = errors.New("done")

func read(mem map[int]int, relbase int, modes [3]int, pos int, offset int) int {
	switch modes[offset-1] {
	case modePos:
		return mem[mem[pos+offset]]
	case modeVal:
		return mem[pos+offset]
	case modeRel:
		return mem[relbase+mem[pos+offset]]
	default:
		panic(fmt.Errorf("unknown mode %d", modes[offset-1]))
	}
}

func write(mem map[int]int, relbase int, modes [3]int, pos int, offset int, value int) {
	switch modes[offset-1] {
	case modePos:
		mem[mem[pos+offset]] = value
	case modeVal:
		panic(fmt.Errorf("value mode for write"))
	case modeRel:
		mem[relbase+mem[pos+offset]] = value
	default:
		panic(fmt.Errorf("unknown mode %d", modes[offset-1]))
	}
}

func run(intcodes []int, in chan int, out chan<- int, e chan<- error) {
	mem := make(map[int]int, len(intcodes))
	for i, v := range intcodes {
		mem[i] = v
	}

	var relbase int
	var modes [3]int
	var i int

	r := func(offset int) int {
		return read(mem, relbase, modes, i, offset)
	}

	w := func(offset int, value int) {
		write(mem, relbase, modes, i, offset, value)
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
		case instRB:
			relbase += r(1)
			i += 1
		default:
			e <- fmt.Errorf("not a valid instruction at position %d: %d", i, mem[i])
			return
		}
	}
	e <- fmt.Errorf("halt instruction not found")
}

type tile int

func (t tile) String() string {
	switch t {
	case tileEmpty:
		return " "
	case tileWall:
		return "█"
	case tileBlock:
		return "▒"
	case tilePaddle:
		return "▔"
	case tileBall:
		return "●"
	}
	panic(fmt.Errorf("cannot draw tile ID %d", t))
}

const (
	tileEmpty tile = iota
	tileWall
	tileBlock
	tilePaddle
	tileBall
)

const clear = "\033[H\033[2J"

type screen map[[2]int]tile

func (s screen) draw() {
	var w, h int
	for k, _ := range s {
		if k[0] >= w {
			w = k[0] + 1
		}
		if k[1] >= h {
			h = k[1] + 1
		}
	}

	out := make([]string, h)
	line := make([]string, w)
	for y := 0; y < h; y++ {
		for x := 0; x < w; x++ {
			line[x] = s[[2]int{x, y}].String()
		}
		out[y] = strings.Join(line, "")
	}

	fmt.Println(clear + strings.Join(out, "\n"))
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

	in := make(chan int)
	out := make(chan int, 3)
	e := make(chan error)
	go run(intcodes, in, out, e)

	s := make(screen)
	var isDone bool
	var i, x, y int
	for !isDone {
		if i == 0 {
			s.draw()
			time.Sleep(time.Millisecond)
		}

		select {
		case v := <-out:
			switch i {
			case 0:
				x = v
			case 1:
				y = v
			case 2:
				s[[2]int{x, y}] = tile(v)
			}
			i = (i + 1) % 3
		case <-in:
			panic("unexpected prompt")
		case err := <-e:
			if !errors.Is(err, done) {
				panic(err)
			}
			isDone = true
		}
	}

	var n int
	for _, v := range s {
		if v == tileBlock {
			n++
		}
	}
	fmt.Println(n)
}
