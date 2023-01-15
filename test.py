# leetcode 49
from collections import defaultdict
strs = ['abc', 'bca', 'cba', 'att', 'taa', 'tta']
a = ('abc', 'bcs')
print(list(a))


def groupAnagrams(strs):
    anagrams = defaultdict(list)
    for word in strs:
        sorted_word = ''.join(sorted(word))
        print('sorted_word0---------', sorted(word))
        print('sorted_word---------', sorted_word)
        anagrams[sorted_word].append(word)
        print('anagrams----------', anagrams)
        print('key----------', anagrams.keys())
        print('value-----------', anagrams.values())
        print('value list-----------', list(anagrams.values()))
    return list(anagrams.values())


groupAnagrams(strs)
