package fiveohthree

import "sort"

func nextGreaterElements(nums []int) []int {
	return nextGreaterElementsBinarySearch(nums)
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

// t:O(n×log(n)), s:O(n)
func nextGreaterElementsBinarySearch(nums []int) []int {
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

		// Binary search next greater number, since it's always sorted (desc).
		g := sort.Search(len(nextGreatElems), func(k int) bool {
			return nextGreatElems[k] <= n
		})

		if g == 0 {
			r[j] = -1
		} else {
			r[j] = nextGreatElems[g-1]
		}

		nextGreatElems = append(nextGreatElems[:g], n)
	}
	return r
}
