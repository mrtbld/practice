package two

import "testing"

func Test_addTwoNumbers(t *testing.T) {
	cases := []struct {
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

	for _, c := range cases {
		output := addTwoNumbers(c.a, c.b)
		if !output.eq(c.expected) {
			t.Errorf("expected %v to equal %v, result of %v + %v", output, c.expected, c.a, c.b)
		}
		reverseOutput := addTwoNumbers(c.b, c.a)
		if !reverseOutput.eq(output) {
			t.Errorf("expected addTwoNumbers() to be transitive for %v and %v", c.a, c.b)
		}
	}
}
