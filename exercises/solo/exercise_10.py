"""
Exercise 10: Cherry-Pick - Grabbing Specific Commits
====================================================

GIT LEARNING GOALS:
- git cherry-pick <commit> (apply a specific commit)
- git cherry-pick --no-commit (apply changes without committing)
- git cherry-pick --abort (cancel a cherry-pick)
- Understanding when cherry-pick is useful

CODING TASK: Binary Search
Difficulty: ⭐⭐ Medium

INSTRUCTIONS:
1. Create a commit on a separate branch
2. Cherry-pick it to another branch
3. Understand when and why you'd use cherry-pick
"""


def binary_search(arr: list, target: int) -> int:
    """
    Find the index of target in a sorted array using binary search.

    Binary search works by repeatedly dividing the search interval in half.
    Much faster than linear search for large sorted arrays!

    Examples:
        binary_search([1, 2, 3, 4, 5], 3) -> 2
        binary_search([1, 2, 3, 4, 5], 1) -> 0
        binary_search([1, 2, 3, 4, 5], 5) -> 4
        binary_search([1, 2, 3, 4, 5], 6) -> -1  (not found)
        binary_search([], 1) -> -1

    Args:
        arr: Sorted list of integers
        target: The value to search for

    Returns:
        Index of target if found, -1 otherwise
    """
    # TODO: Implement binary search
    #
    # Algorithm:
    # 1. Set left = 0, right = len(arr) - 1
    # 2. While left <= right:
    #    a. Find mid = (left + right) // 2
    #    b. If arr[mid] == target, return mid
    #    c. If arr[mid] < target, search right half (left = mid + 1)
    #    d. If arr[mid] > target, search left half (right = mid - 1)
    # 3. Return -1 if not found
    pass


# Don't modify below this line - used for local testing
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], 3, 2),
        ([1, 2, 3, 4, 5], 1, 0),
        ([1, 2, 3, 4, 5], 5, 4),
        ([1, 2, 3, 4, 5], 6, -1),
        ([], 1, -1),
        ([1], 1, 0),
        ([1, 3, 5, 7, 9], 7, 3),
        ([2, 4, 6, 8, 10], 5, -1),
    ]

    print("Testing binary_search...")
    for arr, target, expected in test_cases:
        result = binary_search(arr, target)
        status = "+" if result == expected else "x"
        print(f"  {status} binary_search({arr}, {target}) = {result} (expected {expected})")


"""
=============================================================================
GIT EXERCISE - Cherry-Pick: Grabbing Specific Commits
=============================================================================

SCENARIO:
You made a great bugfix on a feature branch, but now you need that same
fix on main RIGHT NOW - without merging your entire feature branch.

Cherry-pick lets you copy specific commits from one branch to another.

=============================================================================
PART A: Setup - Create branches with different commits
=============================================================================

STEP 1: Make sure you're on main and it's clean
    $ git checkout main
    $ git status

STEP 2: Create a feature branch
    $ git checkout -b feature/new-search

STEP 3: Implement binary_search and commit
    -> Complete the TODO above
    $ git add exercises/solo/exercise_10.py
    $ git commit -m "Implement binary_search function"

STEP 4: Make another commit (simulating more feature work)
    -> Add a comment at the top: # Feature: Advanced Search
    $ git add exercises/solo/exercise_10.py
    $ git commit -m "Add feature header comment"

STEP 5: Check your commits
    $ git log --oneline -3

    -> Note the hash of "Implement binary_search function" commit

=============================================================================
PART B: Cherry-pick to main
=============================================================================

STEP 6: Switch to main
    $ git checkout main

STEP 7: Cherry-pick ONLY the implementation commit (not the comment)
    $ git cherry-pick <hash-of-implementation-commit>

    -> This copies that specific commit to main
    -> The feature header comment is NOT included

STEP 8: Verify the cherry-pick
    $ git log --oneline -3

    -> You should see the cherry-picked commit on main
    -> Notice it has a NEW hash (it's a copy, not the original)

STEP 9: Check that only the implementation was copied
    $ git diff HEAD~1

    -> Should show the binary_search implementation
    -> Should NOT show the feature header comment

=============================================================================
PART C: Cherry-pick with conflicts
=============================================================================

STEP 10: Go back to feature branch and make a conflicting change
    $ git checkout feature/new-search
    -> Modify the docstring of binary_search
    $ git add exercises/solo/exercise_10.py
    $ git commit -m "Update docstring"

STEP 11: Make a different docstring change on main
    $ git checkout main
    -> Make a DIFFERENT change to the same docstring
    $ git add exercises/solo/exercise_10.py
    $ git commit -m "Different docstring update"

STEP 12: Try to cherry-pick the feature branch's docstring commit
    $ git cherry-pick <hash-of-docstring-commit>

    -> CONFLICT! Both branches modified the same lines

STEP 13: Resolve the conflict or abort

    To abort:
    $ git cherry-pick --abort

    To resolve:
    -> Edit the file, remove conflict markers
    $ git add exercises/solo/exercise_10.py
    $ git cherry-pick --continue

=============================================================================
PART D: Clean up and push
=============================================================================

STEP 14: Push main
    $ git checkout main
    $ git push origin main

STEP 15: Delete the feature branch (optional)
    $ git branch -d feature/new-search

    -> Or keep it if you want to continue feature work

=============================================================================

WHEN TO USE CHERRY-PICK:

+ Hotfix needed on main but developed on feature branch
+ Backporting a fix to an older release branch
+ Grabbing a specific commit from a colleague's branch
+ Recovering a commit from a deleted branch (via reflog)

WHEN NOT TO USE CHERRY-PICK:

- Want ALL commits from a branch -> use merge or rebase
- The commit depends on previous commits -> merge instead
- Cherry-picking the same commit multiple times -> causes duplicates

=============================================================================

CHERRY-PICK OPTIONS:

# Basic cherry-pick
git cherry-pick <commit>

# Cherry-pick without auto-commit (useful for combining changes)
git cherry-pick --no-commit <commit>

# Cherry-pick multiple commits
git cherry-pick <commit1> <commit2> <commit3>

# Cherry-pick a range of commits
git cherry-pick <start-commit>..<end-commit>

# Abort a cherry-pick in progress
git cherry-pick --abort

=============================================================================
REFLECTION QUESTIONS:
- Why does a cherry-picked commit get a new hash?
- When would you use --no-commit?
- What's the danger of cherry-picking the same commit to multiple branches?
=============================================================================
"""
