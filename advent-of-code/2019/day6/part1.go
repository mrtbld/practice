package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

func f(adj map[string][]string, a string, orb map[string]int) map[string]int {
	var n int
	for _, b := range adj[a] {
		orb = f(adj, b, orb)
		n += 1 + orb[b]
	}
	orb[a] = n
	return orb
}

func main() {
	data, err := ioutil.ReadFile("./input")
	if err != nil {
		panic(err)
	}

	adj := make(map[string][]string)

	lines := strings.Split(string(data), "\n")
	for _, l := range lines {
		l = strings.TrimSpace(l)
		if l == "" {
			continue
		}
		o := strings.Split(l, ")")
		a, b := o[0], o[1]
		adj[a] = append(adj[a], b)
	}

	orb := f(adj, "COM", make(map[string]int))
	var total int
	for _, n := range orb {
		total += n
	}
	fmt.Println(total)
}
