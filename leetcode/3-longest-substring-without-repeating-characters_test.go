// https://leetcode.com/problems/longest-substring-without-repeating-characters/

package leetcode3

import "testing"

func Test(t *testing.T) {
	cases := []struct {
		input    string
		expected int
	}{
		{"abcabcbb", 3},
		{"bbbbb", 1},
		{"pwwkew", 3},
		{"abc", 3},
		{"a", 1},
		{"", 0},
		{"abacd", 4},
		{"abcdefcghijklmn", 12},
		{"abcdefcghijklmnd", 12},
	}

	for _, c := range cases {
		output := lengthOfLongestSubstring(c.input)
		if output != c.expected {
			t.Errorf("\nFor input: %s\nOutput expected: %d\nGot: %d\n", c.input, c.expected, output)
		}
	}
}
