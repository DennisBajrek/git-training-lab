# Solutions 🔑

**⚠️ SPOILER ALERT**: Only look at these if you're truly stuck!

Try to solve the exercises yourself first. The learning happens in the struggle.

---

## Exercise 1: Reverse String

```python
def reverse_string(s: str) -> str:
    return s[::-1]
```

---

## Exercise 2: FizzBuzz

```python
def fizzbuzz(n: int) -> list:
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result
```

---

## Exercise 3: Find Max

```python
def find_max(numbers: list) -> int | None:
    if not numbers:
        return None
    return max(numbers)
```

---

## Exercise 4: Count Vowels

```python
def count_vowels(text: str) -> int:
    vowels = "aeiouAEIOU"
    return sum(1 for c in text if c in vowels)
```

---

## Exercise 5: Palindrome

```python
def is_palindrome(text: str) -> bool:
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]
```

---

## Exercise 6: Two Sum

```python
def two_sum(nums: list, target: int) -> list:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

---

## Exercise 7: Merge Sorted Arrays

```python
def merge_sorted_arrays(arr1: list, arr2: list) -> list:
    # Simple solution
    return sorted(arr1 + arr2)
    
    # Or optimal O(n+m) solution:
    # result = []
    # i = j = 0
    # while i < len(arr1) and j < len(arr2):
    #     if arr1[i] <= arr2[j]:
    #         result.append(arr1[i])
    #         i += 1
    #     else:
    #         result.append(arr2[j])
    #         j += 1
    # result.extend(arr1[i:])
    # result.extend(arr2[j:])
    # return result
```

---

## Exercise 8: Group Anagrams

```python
def group_anagrams(words: list) -> list:
    anagrams = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(word)
    return list(anagrams.values())
```

---

## Exercise 9: Valid Parentheses

```python
def is_valid_parentheses(s: str) -> bool:
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    
    return len(stack) == 0
```

---

## Still Stuck?

If the solution doesn't make sense:
1. Re-read the exercise description
2. Try running the solution with print statements
3. Ask a teammate or mentor to explain

The goal isn't just to pass the tests — it's to understand the code!
