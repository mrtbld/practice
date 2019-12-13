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
		runes := []rune(strconv.Itoa(i))
		var last, lastlast rune
		increasing := true
		has_double := false
		for i, r := range runes {
			var next rune
			if i+1 < len(runes) {
				next = runes[i+1]
			}
			increasing = increasing && last <= r
			has_double = has_double || (last == r && lastlast != r && next != r)
			lastlast = last
			last = r
		}
		if increasing && has_double {
			n += 1
		}
	}
	fmt.Println(n)
}
