from collections import Counter

def findAnagrams(self, s: str, p: str) -> List[int]:
        win_size = len(p)

        anagram = Counter(list(p))

        output = []

        for i in range(len(s) - win_size + 1):
            if Counter(list(s[i:i+win_size])) == anagram:
                output.append(i)

        return output