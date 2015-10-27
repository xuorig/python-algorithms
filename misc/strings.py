# Given a string and two words which are present in the string,
# find the minimum distance between the words
# Eg: "the brown qucik frog quick the", "the" "quick" O/P -> 1
# "the quick the brown quick brown the frog", "the" "the" O/P -> 2

def distanceBetweenWords(text, wordA, wordB):
    indexA = 0
    indexB = 0
    for i, word in enumerate(text.split(' ')):
        if word == wordA:
            indexA = i
        elif word == wordB:
            indexB = i
    return abs(indexA - indexB)

print distanceBetweenWords("the brown qucik frog quick the", "the", "quick")
