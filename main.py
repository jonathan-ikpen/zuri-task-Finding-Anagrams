# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = word.lower()
    anagram = anagram.lower()
    word = word.strip()
    anagram = anagram.strip()
    if len(word) == len(anagram) and sorted(word) == sorted(anagram):
        return True
    else:
        return False

    

find_anagram("hello", "check")
find_anagram("below", "elbow")