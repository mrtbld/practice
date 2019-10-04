package two

import "testing"

func Test_ListNode_eq_true(t *testing.T) {
	cases := []struct {
		a *ListNode
		b *ListNode
	}{
		{nil, nil},
		{nil, &ListNode{}},
		{&ListNode{}, &ListNode{}},
		{&ListNode{Val: 1}, &ListNode{Val: 1}},
		{&ListNode{Val: 1, Next: &ListNode{Val: 5}}, &ListNode{Val: 1, Next: &ListNode{Val: 5}}},
		{&ListNode{Val: 1, Next: &ListNode{}}, &ListNode{Val: 1}},
	}

	for _, c := range cases {
		output := c.a.eq(c.b)
		if !output {
			t.Errorf("expected %v to equal %v", c.a, c.b)
		}
		reverseOutput := c.b.eq(c.a)
		if reverseOutput != output {
			t.Errorf("expected eq() to be transitive for %v and %v", c.a, c.b)
		}
	}
}

func Test_ListNode_eq_false(t *testing.T) {
	cases := []struct {
		a *ListNode
		b *ListNode
	}{
		{&ListNode{}, &ListNode{Val: 1}},
		{&ListNode{Val: 1}, &ListNode{Val: 2}},
		{&ListNode{Val: 1, Next: &ListNode{Val: 5}}, &ListNode{Val: 1}},
	}

	for _, c := range cases {
		output := c.a.eq(c.b)
		if output {
			t.Errorf("expected %v not to equal %v", c.a, c.b)
		}
		reverseOutput := c.b.eq(c.a)
		if reverseOutput != output {
			t.Errorf("expected eq() to be transitive for %v and %v", c.a, c.b)
		}
	}
}
