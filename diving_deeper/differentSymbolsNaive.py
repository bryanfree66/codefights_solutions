from collections import Counter

def differentSymbolsNaive(s):
    character_count = Counter(s)
    return len(character_count)
