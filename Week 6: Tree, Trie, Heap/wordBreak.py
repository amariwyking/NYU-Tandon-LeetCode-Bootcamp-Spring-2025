from typing import List

def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    # Initialize an array to keep track of celebration
    dp = [False] * (len(s) + 1)

    # Set the last value as true. This is the base case
    # If we can make it to the last index we've successfully parsed the string
    dp[len(s)] = True

    # We're going to iterate from the end of the string backwards
    # That way we can reference previously explored states should they reoccur
    for i in range(len(s) - 1, -1, -1):
        # For each state, search for a word in the dictionary which satisfies the state
        for w in wordDict:
            # If this word fits in the rest of the string
            # and
            # If the substring matches the word
            if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                dp[i] = dp[i + len(w)]
            if dp[i]:
                break

    return dp[0]