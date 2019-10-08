package fiveohthree

import (
	"math"
	"math/rand"
	"reflect"
	"strconv"
	"testing"
)

var cases = []struct {
	input    []int
	expected []int
}{
	{
		input:    []int(nil),
		expected: []int(nil),
	},
	{
		input:    []int{},
		expected: []int{},
	},
	{
		input:    []int{0},
		expected: []int{-1},
	},
	{
		input:    []int{1},
		expected: []int{-1},
	},
	{
		input:    []int{1, 2},
		expected: []int{2, -1},
	},
	{
		input:    []int{1, 2, 3},
		expected: []int{2, 3, -1},
	},
	{
		input:    []int{1, 2, 1},
		expected: []int{2, -1, 2},
	},
	{
		input:    []int{7, 7, 7, 7, 7, 7, 7},
		expected: []int{-1, -1, -1, -1, -1, -1, -1},
	},
	{
		input:    []int{0, 1, 2, 3, 4, 5, 6},
		expected: []int{1, 2, 3, 4, 5, 6, -1},
	},
	{
		input:    []int{6, 5, 4, 3, 2, 1, 0},
		expected: []int{-1, 6, 6, 6, 6, 6, 6},
	},
	{
		input:    []int{6, 5, 4, 3, 2, 1, 0, 7},
		expected: []int{7, 7, 7, 7, 7, 7, 7, -1},
	},
	{
		input:    []int{1, 5, 3, 2, 1, 3, 4, 0, 7, 5, 3, 4},
		expected: []int{5, 7, 4, 3, 3, 4, 7, 7, -1, 7, 4, 5},
	},
	{
		input:    []int{-1},
		expected: []int{-1},
	},
	{
		input:    []int{1, -1},
		expected: []int{-1, 1},
	},

	{
		input:    []int{-10, -2, 6, -6, -1, 0, -5},
		expected: []int{-2, 6, -1, -1, 0, 6, -2},
	},
}

func Test_nextGreaterElementsQuad(t *testing.T) {
	for _, c := range cases {
		output := nextGreaterElementsQuad(c.input)
		if !reflect.DeepEqual(output, c.expected) {
			t.Errorf("expected %#v to equal %#v for input %#v", output, c.expected, c.input)
		}
	}
}

func Test_nextGreaterElementsLinear(t *testing.T) {
	for _, c := range cases {
		output := nextGreaterElementsLinear(c.input)
		if !reflect.DeepEqual(output, c.expected) {
			t.Errorf("expected %#v to equal %#v for input %#v", output, c.expected, c.input)
		}
	}
}

const N = 5

func Benchmark_nextGreaterElementsQuad(b *testing.B) {
	for i := 1; i <= N; i++ {
		n := int(math.Pow10(i))
		input := make([]int, n)
		for i := range input {
			input[i] = rand.Intn(1000)
		}
		b.Run(strconv.Itoa(n), func(b *testing.B) {
			for n := 0; n < b.N; n++ {
				_ = nextGreaterElementsQuad(input)
			}
		})
	}
}

func Benchmark_nextGreaterElementsLinear(b *testing.B) {
	for i := 1; i <= N; i++ {
		n := int(math.Pow10(i))
		input := make([]int, n)
		for i := range input {
			input[i] = rand.Intn(1000)
		}
		b.Run(strconv.Itoa(n), func(b *testing.B) {
			for n := 0; n < b.N; n++ {
				_ = nextGreaterElementsLinear(input)
			}
		})
	}
}
