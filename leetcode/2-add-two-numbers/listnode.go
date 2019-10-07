package two

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func (ln *ListNode) String() string {
	if ln.Next == nil {
		return fmt.Sprintf("%d", ln.Val)
	}
	return fmt.Sprintf("%d→%s", ln.Val, ln.Next)
}
