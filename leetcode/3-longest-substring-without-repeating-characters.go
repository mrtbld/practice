package leetcode3

// t:O(n), s:O(a) where a is alphabet size
func lengthOfLongestSubstring(s string) int {
	m := map[byte]int{}
	i := 0
	j := 0
	l := 0
	for j < len(s) {
		seen_i, seen := m[s[j]]
		if seen && seen_i >= i {
			i = seen_i + 1
		}
		m[s[j]] = j
		if j-i+1 > l {
			l = j - i + 1
		}
		j++
	}
	return l
}
