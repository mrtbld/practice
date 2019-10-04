package two

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func (ln *ListNode) eq(other *ListNode) bool {
	if ln == nil && other == nil {
		return true
	}
	if ln == nil {
		ln = &ListNode{}
	}
	if other == nil {
		other = &ListNode{}
	}
	return ln.Val == other.Val && ln.Next.eq(other.Next)
}

func (ln *ListNode) String() string {
	if ln.Next == nil {
		return fmt.Sprintf("%d", ln.Val)
	}
	return fmt.Sprintf("%d→%s", ln.Val, ln.Next)
}
