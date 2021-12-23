#encoding: utf-8
'''
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
	Input: "babad"
	Output: "bab"
	Note: "aba" is also a valid answer.

Example 2:
	Input: "cbbd"
	Output: "bb"
'''


'''
DP Solution Outline:
	1. A single letter is a palindrome by itself (of length 1)
	2. Two-letter palindromes (x+1, y if a[x+1] == a[y])
	3. Longest palindrome substring within a[x..z] is (x-z+1) if a[x] == a[z] and a[x+1 .. z-1] is a palindrome
	4. if a[x] != a[z], then return longest palindrome substring out of a[x..z-1] and a[x+1 .. z]
	5. Longest palindrome substring a[0..n-1] is when x = 0, z = n-1. step 3-4

Time: O(2ⁿ), Space: O(2ⁿ)


Sample run 1:
============
S: "abcbd"

lps("abcbd")
	a[0] == 'a' =/= a[4] == 'd'
	= max(lps("abcb"), lps("bcbd))
	  > lps("abcb):
	    a[0] = 'a' =/=  a[3] = 'b' 
		= max(lps("abc"), lps("bcb))
		  >> lps("abc"):
		     a[0] == 'a' =/= a[2] == 'c'
			 = max(lps("ab), lps("bc"))
			   >> > lps("ab"):
			        = max(lps("a"), lps("b"))
			        = 1
			   >> > lps("bc"):
			        = max(lps("b"), lps("c"))
			        = 1
			 = max(lps("ab), lps("bc")) = 1 => lps("abc") = 1
		  >> lps("bcb"):
		     a[1] == 'b' == a[3]
			 lps("c") == (palindrome)
			 == 3
		= max(lps("abc"), lps("bcb")) == max(1, 3) == 3 => lps("abcb") = 3 ("bcb")
	  > lps("bcbd"):
		= max(lps("bcb"), lps("cbd"))
		  >> lps("bcb") == 3
		  >> lps("cbd")
		     = max(lps("cb"), lps("bd"))
			   >> > lps("cb"):
			        = max(lps("c)", lps("d"))
					= 1
			   >> > lps( "bd"):
			        = max(lps("b"), lps("d"))
					= 1
		     = max(lps("cb"), lps("bd")) = 1 => lps("cbd") == 1
		= max(lps("bcb"), lps("cbd")) = max(3,1)= 3 ("bcb") => lps("bcbd") = 3 ("bcb")
	= max(lps("abcb"), lps("bcbd)) = max(3, 3) = 3 => lps("abcbd") = 3 ("bcb")
'''

# check if s[startIdx .. endIdx] is a palindrome or not
def isPalindrome(s, startIdx, endIdx):
	while (startIdx < endIdx):
		if s[startIdx] != s[endIdx]:
			return False
		startIdx += 1
		endIdx -= 1

	return True


# Find and return a (any if many such exist) longest palindromic substring of string 's'
def longest_palindromic_substring(s):
	def longest_palindromic_substring_r(s, l, r):
		if l == r:
			return (l,l)
		elif l+1 == r: # 2 letters
			return (l,r) if s[l] == s[r] else (l,l)

		if s[l] == s[r]:
			if isPalindrome(s, l+1, r-1):
				# whole of s[l..r] is a palindrome
				return (l, r)

		ls, le = longest_palindromic_substring_r(s, l, r-1)
		rs, re = longest_palindromic_substring_r(s, l+1, r)

		# return the left/right palindrome substrings length whichever is longer
		return (ls, le) if (le-ls) >= (re-rs) else (rs, re)

	start, end = longest_palindromic_substring_r(s, 0, len(s)-1)
	return s[start:end+1]



# Find and return the length of any longest palindromic substring of string 's'
def longest_palindromic_substring_len(s):
	def longest_palindromic_substring_len_r(s, l, r):
		if l == r:
			return 1

		elif l+1 == r: # 2 letters
			return 2 if s[l] == s[r] else 1

		if s[l] == s[r]:
			if isPalindrome(s, l+1, r-1):
				# whole of s[l..r] is a palindrome
				return (r-l+1)

		left = longest_palindromic_substring_len_r(s, l, r-1)
		right = longest_palindromic_substring_len_r(s, l+1, r)

		# return the left/right palindrome substrings length whichever is longer
		return max(left, right)

	return longest_palindromic_substring_len_r(s, 0, len(s)-1)




if __name__ == '__main__':
	assert longest_palindromic_substring("abcbd") == "bcb"
	assert longest_palindromic_substring("abcd") == "a"
	assert longest_palindromic_substring("cbbd") == "bb"
	assert longest_palindromic_substring("babad") == "bab"
	assert longest_palindromic_substring("aaaabcaaa") == "aaaa"
	assert longest_palindromic_substring("racecar") == "racecar"
	assert longest_palindromic_substring("mississippi") == "ississi"
	#assert longest_palindromic_substring("babaddtattarrattatddetartrateedredividerb") == "ddtattarrattatdd" # TLE

	assert longest_palindromic_substring_len("abcbd") == 3
	assert longest_palindromic_substring_len("abcd") == 1
	assert longest_palindromic_substring_len("cbbd") == 2
	assert longest_palindromic_substring_len("babad") == 3
	assert longest_palindromic_substring_len("aaaabcaaa") == 4
	assert longest_palindromic_substring_len("racecar") == 7
	assert longest_palindromic_substring_len("mississippi") == 7

