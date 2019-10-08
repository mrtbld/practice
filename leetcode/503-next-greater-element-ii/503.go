package fiveohthree

func nextGreaterElements(nums []int) []int {
	return nextGreaterElementsLinear(nums)
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

// t:O(n), s:O(n)
func nextGreaterElementsLinear(nums []int) []int {
	if nums == nil {
		return nil
	}

	l := len(nums)
	r := make([]int, l)
	if l == 0 {
		return r
	}

	// Find index of max value, to start iteration from, and initialize
	// nextGreatElems with.
	maxI := 0
	maxV := nums[0]
	for i, n := range nums {
		if n > maxV {
			maxV = n
			maxI = i
		}
	}

	// nextGreatElems holds the potential next greater for each number during
	// the iteration, from farthest to closest.
	nextGreatElems := []int{maxV}

	for i := l - 1; i >= 0; i-- {
		j := (i + maxI) % l
		n := nums[j]

		var k int
		for k = len(nextGreatElems) - 1; k >= 0; k-- {
			if nextGreatElems[k] > n {
				break
			}
		}

		if k == -1 {
			r[j] = -1
		} else {
			r[j] = nextGreatElems[k]
		}

		nextGreatElems = append(nextGreatElems[:k+1], n)
	}
	return r
}
