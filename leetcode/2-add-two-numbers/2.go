package two

func addTwoNumbers(a, b *ListNode) *ListNode {
	return addTwoNumbersIter(a, b)
}

// t:O(n), s:O(n)
func addTwoNumbersRecur(a, b *ListNode, carry int) *ListNode {
	if a == nil && b == nil && carry == 0 {
		return nil
	}
	if a == nil {
		a = &ListNode{}
	}
	if b == nil {
		b = &ListNode{}
	}
	return &ListNode{
		Val:  (a.Val + b.Val + carry) % 10,
		Next: addTwoNumbersRecur(a.Next, b.Next, (a.Val+b.Val+carry)/10),
	}
}

// t:O(n), s:O(n)
func addTwoNumbersIter(a, b *ListNode) *ListNode {
	var r *ListNode
	var last *ListNode
	var carry int
	for a != nil || b != nil || carry != 0 {
		if a == nil {
			a = &ListNode{}
		}
		if b == nil {
			b = &ListNode{}
		}
		new := &ListNode{
			Val: (a.Val + b.Val + carry) % 10,
		}
		if r == nil {
			r = new
		} else {
			last.Next = new
		}
		carry = (a.Val + b.Val + carry) / 10
		last = new
		a, b = a.Next, b.Next
	}
	return r
}
