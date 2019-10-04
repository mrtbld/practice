package two

func addTwoNumbers(a, b *ListNode) *ListNode {
	return addTwoNumbersRecur(a, b, 0)
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
