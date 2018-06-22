from collections import Counter


def commonCharacterCount(s1, s2):
    common_characters = Counter(s1) & Counter(s2)
    result = sum(common_characters.values())
    return result
