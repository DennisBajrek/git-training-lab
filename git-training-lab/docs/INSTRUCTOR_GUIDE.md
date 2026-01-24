# Instructor / Setup Guide 📋

This document explains how to set up and manage the Git Training Lab for new cohorts.

---

## Quick Setup

### For a New Cohort

1. **Create a new GitHub repository** (or use an existing organization repo)

2. **Push this training lab to the repo:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Git Training Lab"
   git remote add origin https://github.com/YOUR-ORG/git-training-lab.git
   git push -u origin main
   ```

3. **Create the simulated teammate branches:**
   ```bash
   # Branch for Exercise 8 (merge conflict)
   git checkout -b teammate/exercise-8
   cp branches/teammate-exercise-8.py exercises/collaborative/exercise_8.py
   git add exercises/collaborative/exercise_8.py
   git commit -m "Teammate implementation of group_anagrams"
   git push origin teammate/exercise-8
   git checkout main
   
   # Branch for Exercise 9 (rebase exercise)
   git checkout -b main-updated
   cp branches/main-updated-content.py utils/changelog.py
   mkdir -p utils
   mv branches/main-updated-content.py utils/changelog.py
   git add utils/
   git commit -m "Add changelog and utility functions"
   git push origin main-updated
   git checkout main
   ```

4. **Have engineers fork the repository** to their own GitHub accounts

---

## Expected Solutions

Below are reference solutions for each exercise. Engineers may implement these differently—that's okay as long as tests pass!

### Exercise 1: Reverse String
```python
def reverse_string(s: str) -> str:
    return s[::-1]
```

### Exercise 2: FizzBuzz
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

### Exercise 3: Find Max
```python
def find_max(numbers: list) -> int | None:
    if not numbers:
        return None
    return max(numbers)
```

### Exercise 4: Count Vowels
```python
def count_vowels(text: str) -> int:
    vowels = "aeiouAEIOU"
    return sum(1 for c in text if c in vowels)
```

### Exercise 5: Palindrome
```python
def is_palindrome(text: str) -> bool:
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]
```

### Exercise 6: Two Sum
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

### Exercise 7: Merge Sorted Arrays
```python
def merge_sorted_arrays(arr1: list, arr2: list) -> list:
    return sorted(arr1 + arr2)  # Simple solution

# Or optimal O(n+m) solution:
def merge_sorted_arrays(arr1: list, arr2: list) -> list:
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result
```

### Exercise 8: Group Anagrams
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

### Exercise 9: Valid Parentheses
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

## Resetting Between Cohorts

To reset the repository for a new cohort:

```bash
# Make sure you're on main
git checkout main

# Reset to initial state (keeping the structure but clearing solutions)
# Option 1: If you tagged the initial state
git reset --hard initial-state

# Option 2: Manually restore exercise files
git checkout initial-state -- exercises/

# Recreate the teammate branches if needed
# (Follow the setup steps above)

# Force push (only if you own the repo!)
git push --force origin main
```

### Recommended: Tag the Initial State

After first setup, create a tag:
```bash
git tag initial-state
git push origin initial-state
```

This makes resetting much easier.

---

## Common Issues & Solutions

### 1. "Tests fail even though my code is correct"

- Check for trailing whitespace or encoding issues
- Make sure function names match exactly
- Verify return types (e.g., `None` vs empty list)

### 2. "Can't push to origin"

- They need to push to their fork, not the original repo
- Check: `git remote -v` should show their fork URL

### 3. "Merge conflict is confusing"

- Walk through the conflict markers with them
- Explain that BOTH versions are shown
- They need to manually choose/combine

### 4. "Rebase went wrong"

```bash
git rebase --abort  # Start over
```

### 5. "Accidentally committed to main instead of feature branch"

```bash
# Create the feature branch at current position
git branch feature/my-work

# Move main back
git checkout main
git reset --hard origin/main

# Continue on feature branch
git checkout feature/my-work
```

---

## Customization Options

### Adding More Exercises

1. Create new Python file in `exercises/solo/` or `exercises/collaborative/`
2. Add corresponding tests in `tests/test_exercises.py`
3. Update `README.md` exercise table

### Changing Difficulty

- Solo exercises 1-4: Should be trivially easy (focus is on Git)
- Solo exercises 5-7: Can require some thinking
- Collaborative 8-9: Can be LeetCode medium level

### Adding More Git Concepts

Consider adding exercises for:
- `git cherry-pick`
- `git bisect`
- `git reflog`
- `git tag`
- `.gitignore` usage

---

## Assessment Checklist

Use this to verify completion:

| Exercise | Git Skill | Code Works | Commits Clean |
|----------|-----------|------------|---------------|
| 1 | Basic workflow | ☐ | ☐ |
| 2 | History exploration | ☐ | ☐ |
| 3 | Branching | ☐ | ☐ |
| 4 | Remote operations | ☐ | ☐ |
| 5 | Stashing | ☐ | ☐ |
| 6 | Reset/Revert | ☐ | ☐ |
| 7 | File restoration | ☐ | ☐ |
| 8 | Merge conflicts | ☐ | ☐ |
| 9 | Rebase + PR | ☐ | ☐ |

---

## Contact / Feedback

If you have suggestions for improving this training lab, please:
- Open an issue on the repository
- Submit a pull request with improvements

Happy teaching! 🎓
