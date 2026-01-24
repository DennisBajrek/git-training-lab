"""
TEAMMATE'S VERSION - Exercise 8
================================

This file represents a teammate's implementation that will create
a merge conflict with your implementation.

This is used for the merge conflict exercise.
"""


def group_anagrams(words: list) -> list:
    """
    Group anagrams together.
    
    TEAMMATE'S APPROACH: Using Counter for comparison
    """
    from collections import Counter
    
    # Teammate's different approach using Counter
    anagram_groups = {}
    
    for word in words:
        # Using frozenset of Counter items as key
        # This is different from sorting!
        key = frozenset(Counter(word).items())
        
        if key not in anagram_groups:
            anagram_groups[key] = []
        anagram_groups[key].append(word)
    
    return list(anagram_groups.values())


# Don't modify below this line - used for local testing
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
