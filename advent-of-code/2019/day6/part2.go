package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

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
		adj[b] = append(adj[b], a)
	}

	dist := make(map[string]int)
	q := []string{adj["YOU"][0]}
	for len(q) != 0 {
		a := q[0]
		q = q[1:]
		for _, b := range adj[a] {
			if _, seen := dist[b]; seen {
				continue
			}
			d := dist[a] + 1
			if b == adj["SAN"][0] {
				fmt.Println(d)
				return
			}
			dist[b] = d
			q = append(q, b)
		}
	}
	fmt.Println("no route :(")

}
