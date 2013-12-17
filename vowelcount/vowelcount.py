from collections import defaultdict


def vowelcount(string):
    stats = defaultdict(int)
    vowels = ["a", "e", "i", "o", "u", ]

    for vowel in vowels:
        count = string.count(vowel)
        if count:
            stats[vowel] += string.count(vowel)

    return stats
