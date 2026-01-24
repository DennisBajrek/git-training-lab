"""
Automated tests for all exercises.
Run with: pytest tests/ -v
"""

import pytest
import sys
import os

# Add exercises to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "exercises", "solo"))
sys.path.insert(
    0, os.path.join(os.path.dirname(__file__), "..", "exercises", "collaborative")
)


# =============================================================================
# Exercise 1: Reverse String
# =============================================================================
class TestExercise1:
    """Tests for reverse_string function."""

    def test_basic(self):
        from exercise_1 import reverse_string

        assert reverse_string("hello") == "olleh"

    def test_mixed_case(self):
        from exercise_1 import reverse_string

        assert reverse_string("Python") == "nohtyP"

    def test_empty(self):
        from exercise_1 import reverse_string

        # Verify function works first
        assert reverse_string("a") == "a", "Function not implemented yet"
        assert reverse_string("") == ""

    def test_single_char(self):
        from exercise_1 import reverse_string

        assert reverse_string("a") == "a"

    def test_numbers(self):
        from exercise_1 import reverse_string

        assert reverse_string("12345") == "54321"


# =============================================================================
# Exercise 2: FizzBuzz
# =============================================================================
class TestExercise2:
    """Tests for fizzbuzz function."""

    def test_fizzbuzz_15(self):
        from exercise_2 import fizzbuzz

        expected = [
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz",
        ]
        assert fizzbuzz(15) == expected

    def test_fizzbuzz_5(self):
        from exercise_2 import fizzbuzz

        assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]

    def test_fizzbuzz_1(self):
        from exercise_2 import fizzbuzz

        assert fizzbuzz(1) == ["1"]

    def test_fizzbuzz_3(self):
        from exercise_2 import fizzbuzz

        assert fizzbuzz(3) == ["1", "2", "Fizz"]


# =============================================================================
# Exercise 3: Find Max
# =============================================================================
class TestExercise3:
    """Tests for find_max function."""

    def test_basic(self):
        from exercise_3 import find_max

        assert find_max([1, 5, 3, 9, 2]) == 9

    def test_negative(self):
        from exercise_3 import find_max

        assert find_max([-1, -5, -3]) == -1

    def test_single(self):
        from exercise_3 import find_max

        assert find_max([42]) == 42

    def test_empty(self):
        from exercise_3 import find_max

        # First verify function works on non-empty list (ensures it's implemented)
        assert find_max([1]) == 1, "Function not implemented yet"
        # Then check empty case
        assert find_max([]) is None

    def test_all_same(self):
        from exercise_3 import find_max

        assert find_max([0, 0, 0]) == 0


# =============================================================================
# Exercise 4: Count Vowels
# =============================================================================
class TestExercise4:
    """Tests for count_vowels function."""

    def test_basic(self):
        from exercise_4 import count_vowels

        assert count_vowels("hello") == 2

    def test_all_vowels(self):
        from exercise_4 import count_vowels

        assert count_vowels("AEIOU") == 5

    def test_no_vowels(self):
        from exercise_4 import count_vowels

        # Verify function works first
        assert count_vowels("a") == 1, "Function not implemented yet"
        assert count_vowels("rhythm") == 0

    def test_empty(self):
        from exercise_4 import count_vowels

        # Verify function works first
        assert count_vowels("e") == 1, "Function not implemented yet"
        assert count_vowels("") == 0

    def test_mixed_case(self):
        from exercise_4 import count_vowels

        assert count_vowels("aEiOu") == 5


# =============================================================================
# Exercise 5: Palindrome
# =============================================================================
class TestExercise5:
    """Tests for is_palindrome function."""

    def test_simple_palindrome(self):
        from exercise_5 import is_palindrome

        assert is_palindrome("racecar") is True

    def test_not_palindrome(self):
        from exercise_5 import is_palindrome

        assert is_palindrome("hello") is False

    def test_with_spaces_and_punctuation(self):
        from exercise_5 import is_palindrome

        assert is_palindrome("A man, a plan, a canal: Panama") is True

    def test_empty(self):
        from exercise_5 import is_palindrome

        # Verify function works first
        assert is_palindrome("aa") is True, "Function not implemented yet"
        assert is_palindrome("") is True

    def test_with_question(self):
        from exercise_5 import is_palindrome

        assert is_palindrome("Was it a car or a cat I saw?") is True

    def test_single_char(self):
        from exercise_5 import is_palindrome

        assert is_palindrome("a") is True


# =============================================================================
# Exercise 6: Two Sum
# =============================================================================
class TestExercise6:
    """Tests for two_sum function."""

    def test_basic(self):
        from exercise_6 import two_sum

        result = two_sum([2, 7, 11, 15], 9)
        assert sorted(result) == [0, 1]

    def test_middle_elements(self):
        from exercise_6 import two_sum

        result = two_sum([3, 2, 4], 6)
        assert sorted(result) == [1, 2]

    def test_same_element(self):
        from exercise_6 import two_sum

        result = two_sum([3, 3], 6)
        assert sorted(result) == [0, 1]

    def test_larger_list(self):
        from exercise_6 import two_sum

        result = two_sum([1, 2, 3, 4, 5], 9)
        assert sorted(result) == [3, 4]


# =============================================================================
# Exercise 7: Merge Sorted Arrays
# =============================================================================
class TestExercise7:
    """Tests for merge_sorted_arrays function."""

    def test_basic(self):
        from exercise_7 import merge_sorted_arrays

        assert merge_sorted_arrays([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

    def test_different_lengths(self):
        from exercise_7 import merge_sorted_arrays

        assert merge_sorted_arrays([1, 2], [3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_first_empty(self):
        from exercise_7 import merge_sorted_arrays

        assert merge_sorted_arrays([], [1, 2, 3]) == [1, 2, 3]

    def test_second_empty(self):
        from exercise_7 import merge_sorted_arrays

        assert merge_sorted_arrays([1], []) == [1]

    def test_both_empty(self):
        from exercise_7 import merge_sorted_arrays

        # Verify function works first
        assert merge_sorted_arrays([1], [2]) == [1, 2], "Function not implemented yet"
        assert merge_sorted_arrays([], []) == []

    def test_duplicates(self):
        from exercise_7 import merge_sorted_arrays

        assert merge_sorted_arrays([1, 1, 1], [1, 1]) == [1, 1, 1, 1, 1]

    def test_negative(self):
        from exercise_7 import merge_sorted_arrays

        assert merge_sorted_arrays([-5, 0, 5], [-3, 3]) == [-5, -3, 0, 3, 5]


# =============================================================================
# Exercise 8: Group Anagrams
# =============================================================================
class TestExercise8:
    """Tests for group_anagrams function."""

    def _compare_anagram_groups(self, result, expected):
        """Compare anagram groups regardless of order."""
        if result is None:
            return False
        result_normalized = {frozenset(group) for group in result}
        expected_normalized = {frozenset(group) for group in expected}
        return result_normalized == expected_normalized

    def test_basic(self):
        from exercise_8 import group_anagrams

        result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        assert self._compare_anagram_groups(result, expected)

    def test_empty_string(self):
        from exercise_8 import group_anagrams

        result = group_anagrams([""])
        expected = [[""]]
        assert self._compare_anagram_groups(result, expected)

    def test_single(self):
        from exercise_8 import group_anagrams

        result = group_anagrams(["a"])
        expected = [["a"]]
        assert self._compare_anagram_groups(result, expected)


# =============================================================================
# Exercise 9: Valid Parentheses
# =============================================================================
class TestExercise9:
    """Tests for is_valid_parentheses function."""

    def test_simple_valid(self):
        from exercise_9 import is_valid_parentheses

        assert is_valid_parentheses("()") is True

    def test_multiple_types(self):
        from exercise_9 import is_valid_parentheses

        assert is_valid_parentheses("()[]{}") is True

    def test_mismatched(self):
        from exercise_9 import is_valid_parentheses

        assert is_valid_parentheses("(]") is False

    def test_interleaved_wrong(self):
        from exercise_9 import is_valid_parentheses

        assert is_valid_parentheses("([)]") is False

    def test_nested(self):
        from exercise_9 import is_valid_parentheses

        assert is_valid_parentheses("{[]}") is True

    def test_empty(self):
        from exercise_9 import is_valid_parentheses

        # Verify function works first
        assert is_valid_parentheses("()") is True, "Function not implemented yet"
        assert is_valid_parentheses("") is True

    def test_unbalanced(self):
        from exercise_9 import is_valid_parentheses

        assert is_valid_parentheses("((())") is False

    def test_deeply_nested(self):
        from exercise_9 import is_valid_parentheses

        assert is_valid_parentheses("((({{{[[[]]]}}})))") is True

    def test_only_closing(self):
        from exercise_9 import is_valid_parentheses

        assert is_valid_parentheses("]") is False
