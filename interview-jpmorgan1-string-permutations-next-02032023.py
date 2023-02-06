# give you a string 'bac', return 'bca' which is the permutation of the string, the next of the input.
# bac permutation array [abc, acb, bac, bca, cab, cba]

def nextPermutation(s):
    s = list(s)
    # ['b','a','c']
    print(s)
    i = len(s) - 2
    while i >= 0 and s[i] >= s[i + 1]:
        i -= 1
    if i == -1:
        s.reverse()
        return ''.join(s)
        'cab'

    print(s)
    j = len(s) - 1
    while s[j] <= s[i]:
        j -= 1
    s[i], s[j] = s[j], s[i]
    s[i + 1:] = reversed(s[i + 1:])
    return ''.join(s)


s = 'bac'
nextPermutation(s)
