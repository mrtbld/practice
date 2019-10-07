package two

import (
	"math/rand"
	"reflect"
	"testing"
)

var cases = []struct {
	a        *ListNode
	b        *ListNode
	expected *ListNode
}{
	{
		a:        nil,
		b:        nil,
		expected: nil,
	},
	{
		a:        &ListNode{},
		b:        &ListNode{},
		expected: &ListNode{},
	},
	{
		a:        &ListNode{},
		b:        &ListNode{Val: 1},
		expected: &ListNode{Val: 1},
	},
	{
		a:        &ListNode{Val: 1},
		b:        &ListNode{Val: 1},
		expected: &ListNode{Val: 2},
	},
	{
		a:        &ListNode{Val: 1},
		b:        &ListNode{Val: 2},
		expected: &ListNode{Val: 3},
	},
	{
		a:        &ListNode{Val: 1, Next: &ListNode{Val: 1, Next: &ListNode{Val: 1}}},
		b:        &ListNode{Val: 2, Next: &ListNode{Val: 2, Next: &ListNode{Val: 2}}},
		expected: &ListNode{Val: 3, Next: &ListNode{Val: 3, Next: &ListNode{Val: 3}}},
	},
	{
		a:        &ListNode{Val: 9, Next: &ListNode{Val: 9, Next: &ListNode{Val: 9}}},
		b:        &ListNode{Val: 9, Next: &ListNode{Val: 9, Next: &ListNode{Val: 9}}},
		expected: &ListNode{Val: 8, Next: &ListNode{Val: 9, Next: &ListNode{Val: 9, Next: &ListNode{Val: 1}}}},
	},
	{
		a:        &ListNode{Val: 2, Next: &ListNode{Val: 4, Next: &ListNode{Val: 3}}},
		b:        &ListNode{Val: 5, Next: &ListNode{Val: 6, Next: &ListNode{Val: 4}}},
		expected: &ListNode{Val: 7, Next: &ListNode{Val: 0, Next: &ListNode{Val: 8}}},
	},
}

var benchA = makeLongLI(10000)
var benchB = makeLongLI(10002)

func makeLongLI(l int) *ListNode {
	li := &ListNode{Val: rand.Intn(10)}
	for i := 0; i < l; i++ {
		li = &ListNode{Val: rand.Intn(10), Next: li}
	}
	return li
}

func Test_addTwoNumbersRecur(t *testing.T) {
	for _, c := range cases {
		output := addTwoNumbersRecur(c.a, c.b, 0)
		if !reflect.DeepEqual(output, c.expected) {
			t.Errorf("expected %v to equal %v, result of %v + %v", output, c.expected, c.a, c.b)
		}
		reverseOutput := addTwoNumbersRecur(c.b, c.a, 0)
		if !reflect.DeepEqual(reverseOutput, output) {
			t.Errorf("expected addTwoNumbersRecur() to be transitive for %v and %v", c.a, c.b)
		}
	}
}

func Test_addTwoNumbersIter(t *testing.T) {
	for _, c := range cases {
		output := addTwoNumbersIter(c.a, c.b)
		if !reflect.DeepEqual(output, c.expected) {
			t.Errorf("expected %v to equal %v, result of %v + %v", output, c.expected, c.a, c.b)
		}
		reverseOutput := addTwoNumbersIter(c.b, c.a)
		if !reflect.DeepEqual(reverseOutput, output) {
			t.Errorf("expected addTwoNumbersIter() to be transitive for %v and %v", c.a, c.b)
		}
	}
}

func Benchmark_addTwoNumbersRecur(b *testing.B) {
	for n := 0; n < b.N; n++ {
		addTwoNumbersRecur(benchA, benchB, 0)
	}
}

func Benchmark_addTwoNumbersIter(b *testing.B) {
	for n := 0; n < b.N; n++ {
		addTwoNumbersIter(benchA, benchB)
	}
}
