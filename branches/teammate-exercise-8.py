"""
TEAMMATE'S VERSION - Exercise 8 Reference
==========================================

This file shows the teammate's DIFFERENT implementation of group_anagrams.

On the teammate/exercise-8 branch, only the function body differs from main.
The rest of exercise_8.py (docstrings, tests, instructions) stays the same.

KEY DIFFERENCE:
- Your approach (suggested in exercise): Sort characters as key
    key = ''.join(sorted(word))  # "eat" -> "aet"

- Teammate's approach: Counter signature as key
    key = tuple(sorted(Counter(word).items()))  # "eat" -> (('a',1),('e',1),('t',1))

Both are valid! The conflict teaches students to compare approaches and choose.
"""


def group_anagrams(words: list) -> list:
    """
    Group anagrams together.

    Two strings are anagrams if they contain the same characters
    with the same frequencies, just rearranged.

    Args:
        words: List of strings

    Returns:
        List of lists, where each inner list contains anagrams
    """
    # TEAMMATE'S IMPLEMENTATION
    # Using Counter to create character frequency signature
    from collections import Counter

    anagram_map = {}
    for word in words:
        # Create a signature from character counts
        signature = tuple(sorted(Counter(word).items()))
        if signature not in anagram_map:
            anagram_map[signature] = []
        anagram_map[signature].append(word)

    return list(anagram_map.values())


# Test code (same as main branch)
if __name__ == "__main__":
    def compare_anagram_groups(result, expected):
        if result is None:
            return False
        result_normalized = {frozenset(group) for group in result}
        expected_normalized = {frozenset(group) for group in expected}
        return result_normalized == expected_normalized

    test_cases = [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ]

    print("Testing teammate's group_anagrams...")
    for words, expected in test_cases:
        result = group_anagrams(words)
        status = "✅" if compare_anagram_groups(result, expected) else "❌"
        print(f"  {status} group_anagrams({words})")
