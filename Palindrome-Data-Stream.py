# 958, Palindrome Date Streme
# There is a data stream, one letter at a time, and determine whether the current stream's arrangement can form a palindrome.

# if more than one caractor showed up in odd num, then it won't be palindrome
def getStream(s):
    if s is None or len(s) == 0:
        return None

    odd_letter_cnt = 0
    result = [0 for _ in range(len(s))]
    letters = [0 for _ in range(26)]

    for i in range(len(s)):
        letters[ord(s[i]) - ord('a')] += 1
        if letters[ord(s[i])-ord('a')] % 2 == 1:
            odd_letter_cnt += 1
        else:
            odd_letter_cnt -= 1
        result[i] = 0 if odd_letter_cnt > 1 else 1
    return result


s = 'abba'
print(getStream(s))
