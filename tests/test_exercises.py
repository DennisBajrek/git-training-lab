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


# =============================================================================
# Exercise 10: Binary Search (Cherry-Pick)
# =============================================================================
class TestExercise10:
    """Tests for binary_search function."""

    def test_found_middle(self):
        from exercise_10 import binary_search

        assert binary_search([1, 2, 3, 4, 5], 3) == 2

    def test_found_first(self):
        from exercise_10 import binary_search

        assert binary_search([1, 2, 3, 4, 5], 1) == 0

    def test_found_last(self):
        from exercise_10 import binary_search

        assert binary_search([1, 2, 3, 4, 5], 5) == 4

    def test_not_found(self):
        from exercise_10 import binary_search

        assert binary_search([1, 2, 3, 4, 5], 6) == -1

    def test_empty_list(self):
        from exercise_10 import binary_search

        assert binary_search([], 1) == -1

    def test_single_element_found(self):
        from exercise_10 import binary_search

        assert binary_search([1], 1) == 0

    def test_single_element_not_found(self):
        from exercise_10 import binary_search

        assert binary_search([1], 2) == -1


# =============================================================================
# Exercise 11: Validate Email (Bisect)
# =============================================================================
class TestExercise11:
    """Tests for validate_email function."""

    def test_valid_simple(self):
        from exercise_11 import validate_email

        assert validate_email("user@example.com") is True

    def test_valid_subdomain(self):
        from exercise_11 import validate_email

        assert validate_email("test.user@domain.org") is True

    def test_invalid_no_at(self):
        from exercise_11 import validate_email

        assert validate_email("invalid") is False

    def test_invalid_no_dot(self):
        from exercise_11 import validate_email

        assert validate_email("no@dot") is False

    def test_invalid_no_local(self):
        from exercise_11 import validate_email

        assert validate_email("@nodomain.com") is False

    def test_invalid_spaces(self):
        from exercise_11 import validate_email

        assert validate_email("spaces not@allowed.com") is False

    def test_invalid_empty(self):
        from exercise_11 import validate_email

        # Verify function works first
        assert validate_email("a@b.co") is True, "Function not implemented yet"
        assert validate_email("") is False

    def test_short_tld(self):
        from exercise_11 import validate_email

        assert validate_email("test@domain.c") is False


# =============================================================================
# Exercise 12: Flatten (Reflog)
# =============================================================================
class TestExercise12:
    """Tests for flatten function."""

    def test_nested(self):
        from exercise_12 import flatten

        assert flatten([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]

    def test_simple_nested(self):
        from exercise_12 import flatten

        assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]

    def test_already_flat(self):
        from exercise_12 import flatten

        assert flatten([1, 2, 3]) == [1, 2, 3]

    def test_empty(self):
        from exercise_12 import flatten

        assert flatten([]) == []

    def test_deeply_nested(self):
        from exercise_12 import flatten

        assert flatten([[[1]]]) == [1]

    def test_mixed_nesting(self):
        from exercise_12 import flatten

        assert flatten([1, [2, [3, [4, [5]]]]]) == [1, 2, 3, 4, 5]


# =============================================================================
# Exercise 13: Remove Duplicates (Amend/Squash)
# =============================================================================
class TestExercise13:
    """Tests for remove_duplicates function."""

    def test_basic(self):
        from exercise_13 import remove_duplicates

        assert remove_duplicates([1, 2, 2, 3, 1]) == [1, 2, 3]

    def test_all_same(self):
        from exercise_13 import remove_duplicates

        assert remove_duplicates([1, 1, 1, 1]) == [1]

    def test_no_duplicates(self):
        from exercise_13 import remove_duplicates

        assert remove_duplicates([1, 2, 3]) == [1, 2, 3]

    def test_empty(self):
        from exercise_13 import remove_duplicates

        assert remove_duplicates([]) == []

    def test_strings(self):
        from exercise_13 import remove_duplicates

        assert remove_duplicates(['a', 'b', 'a', 'c']) == ['a', 'b', 'c']

    def test_preserves_order(self):
        from exercise_13 import remove_duplicates

        assert remove_duplicates([5, 4, 3, 2, 1, 1, 2, 3]) == [5, 4, 3, 2, 1]


# =============================================================================
# Exercise 14: Word Frequency (Blame/Log)
# =============================================================================
class TestExercise14:
    """Tests for word_frequency function."""

    def test_basic(self):
        from exercise_14 import word_frequency

        assert word_frequency("hello world hello") == {"hello": 2, "world": 1}

    def test_case_insensitive(self):
        from exercise_14 import word_frequency

        assert word_frequency("The the THE") == {"the": 3}

    def test_punctuation(self):
        from exercise_14 import word_frequency

        assert word_frequency("Hello, World!") == {"hello": 1, "world": 1}

    def test_empty(self):
        from exercise_14 import word_frequency

        assert word_frequency("") == {}

    def test_single_word(self):
        from exercise_14 import word_frequency

        assert word_frequency("one") == {"one": 1}

    def test_multiple_counts(self):
        from exercise_14 import word_frequency

        assert word_frequency("a a a b b c") == {"a": 3, "b": 2, "c": 1}


# =============================================================================
# Exercise 15: Version Parser (Tags)
# =============================================================================
class TestExercise15:
    """Tests for version parsing functions."""

    def test_parse_basic(self):
        from exercise_15 import parse_version

        assert parse_version("1.2.3") == {"major": 1, "minor": 2, "patch": 3}

    def test_parse_zeros(self):
        from exercise_15 import parse_version

        assert parse_version("0.1.0") == {"major": 0, "minor": 1, "patch": 0}

    def test_parse_large_numbers(self):
        from exercise_15 import parse_version

        assert parse_version("10.20.30") == {"major": 10, "minor": 20, "patch": 30}

    def test_compare_less_than(self):
        from exercise_15 import compare_versions

        assert compare_versions("1.2.3", "1.2.4") == -1

    def test_compare_greater_than(self):
        from exercise_15 import compare_versions

        assert compare_versions("2.0.0", "1.9.9") == 1

    def test_compare_equal(self):
        from exercise_15 import compare_versions

        assert compare_versions("1.0.0", "1.0.0") == 0

    def test_compare_minor(self):
        from exercise_15 import compare_versions

        assert compare_versions("1.1.0", "1.0.9") == 1
