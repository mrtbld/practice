package main

import (
	"fmt"
	"strconv"
)

const (
	lo = 357253
	hi = 892942
)

func main() {
	var n int
	for i := lo; i <= hi; i++ {
		var last rune
		increasing := true
		has_repeated := false
		for _, r := range []rune(strconv.Itoa(i)) {
			increasing = increasing && last <= r
			has_repeated = has_repeated || last == r
			last = r
		}
		if increasing && has_repeated {
			n += 1
		}
	}
	fmt.Println(n)
}
