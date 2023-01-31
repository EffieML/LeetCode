# You are given a string S of length N containing only characters a and b.
# A substring (contiguous gragment) of S is called a semi-alternating substring if it does not contain three identical consecutive characters.
# In other words, it does not contain either aaa or bbb substrings. Note that whole S is its own substring.
# Write a function, which given a string S, returns the length of the longest semi-alternating substring of S.

# b a a a b a a a b b b
def longestSemiAlternatingSubstring(s):
    if s is None or len(s) == 0:
        return 0
    if len(s) < 3:
        return len(s)

    start = 0
    end_dup_cnt = 1
    max_len = 0

    for end in range(1, len(s)):
        prev_char = s[end-1]
        curr_char = s[end]

        if prev_char == curr_char:
            end_dup_cnt += 1
            if end_dup_cnt == 3:
                start = end - 1
                end_dup_cnt = 2
        else:
            end_dup_cnt = 1
        max_len = max(max_len, end-start+1)
    return max_len


print(longestSemiAlternatingSubstring('baaabaaabbb'))
