package fiveohthree

func nextGreaterElements(nums []int) []int {
	return nextGreaterElementsQuad(nums)
}

// t:O(n²), s:O(n)
func nextGreaterElementsQuad(nums []int) []int {
	if nums == nil {
		return nil
	}
	l := len(nums)
	r := make([]int, l)
	for i := range nums {
		n := nums[i]
		r[i] = -1
		for j := range nums {
			m := nums[(i+j+1)%l]
			if m > n {
				r[i] = m
				break
			}
		}
	}
	return r
}
