from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counter = Counter(magazine)
        note_counter = Counter(ransomNote)
        for letter, count in note_counter.items():
            if magazine_counter[letter] < count:
                return False
        return True
