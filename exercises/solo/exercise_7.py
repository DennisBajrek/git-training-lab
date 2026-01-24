"""
Exercise 7: Restoring Files - checkout and restore
====================================================

GIT LEARNING GOALS:
- git checkout -- <file> (discard working directory changes)
- git restore <file> (newer syntax for the above)
- git restore --staged <file> (unstage changes)
- git checkout <commit> -- <file> (restore file from specific commit)
- Understanding the working directory vs staging area

CODING TASK: Merge Two Sorted Arrays
Difficulty: ⭐⭐ Medium

INSTRUCTIONS:
1. Make changes to this file
2. Practice discarding and restoring at different stages
3. Then implement the function correctly
"""


def merge_sorted_arrays(arr1: list, arr2: list) -> list:
    """
    Merge two sorted arrays into one sorted array.
    
    Both input arrays are already sorted in ascending order.
    Return a new sorted array containing all elements from both.
    
    Examples:
        merge_sorted_arrays([1, 3, 5], [2, 4, 6]) → [1, 2, 3, 4, 5, 6]
        merge_sorted_arrays([1, 2], [3, 4, 5]) → [1, 2, 3, 4, 5]
        merge_sorted_arrays([], [1, 2, 3]) → [1, 2, 3]
        merge_sorted_arrays([1], []) → [1]
    
    Args:
        arr1: First sorted array
        arr2: Second sorted array
        
    Returns:
        Merged sorted array
    """
    # TODO: Implement this function
    #
    # Approach 1 (Simple):
    #   Concatenate and sort: sorted(arr1 + arr2)
    #
    # Approach 2 (Optimal O(n+m) - two pointers):
    #   - Keep two pointers, one for each array
    #   - Compare elements at both pointers
    #   - Add the smaller one to result
    #   - Move that pointer forward
    #   - Repeat until both arrays are exhausted
    pass


# Don't modify below this line
if __name__ == "__main__":
    test_cases = [
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 2], [3, 4, 5], [1, 2, 3, 4, 5]),
        ([], [1, 2, 3], [1, 2, 3]),
        ([1], [], [1]),
        ([], [], []),
        ([1, 1, 1], [1, 1], [1, 1, 1, 1, 1]),
        ([-5, 0, 5], [-3, 3], [-5, -3, 0, 3, 5]),
    ]
    
    print("Testing merge_sorted_arrays...")
    for arr1, arr2, expected in test_cases:
        result = merge_sorted_arrays(arr1, arr2)
        status = "✅" if result == expected else "❌"
        print(f"  {status} merge_sorted_arrays({arr1}, {arr2}) = {result}")


"""
=============================================================================
GIT EXERCISE - Restoring and Recovering Files
=============================================================================

This exercise teaches you how to undo changes at different stages:
1. Changes in working directory (not yet staged)
2. Changes that are staged (not yet committed)
3. Restoring a file from an older commit

=============================================================================
PART A: Discard unstaged changes
=============================================================================

STEP 1: Make a mess of this file intentionally
    → Add some random text below this docstring
    → Maybe delete some code
    → Don't stage it yet!

STEP 2: Check status
    $ git status
    
    → File shows as modified (red)

STEP 3: See what you changed
    $ git diff exercises/solo/exercise_7.py

STEP 4: Discard your changes (restore to last commit)
    $ git checkout -- exercises/solo/exercise_7.py
    
    → Modern alternative: git restore exercises/solo/exercise_7.py

STEP 5: Verify the file is restored
    $ git status
    $ git diff exercises/solo/exercise_7.py
    
    → Should be clean!

=============================================================================
PART B: Unstage changes (but keep them in working directory)
=============================================================================

STEP 6: Now implement merge_sorted_arrays correctly!
    → Write your solution

STEP 7: Stage your changes
    $ git add exercises/solo/exercise_7.py

STEP 8: Check status
    $ git status
    
    → File should be green (staged)

STEP 9: Oops, let's unstage it (but keep the changes)
    $ git reset HEAD exercises/solo/exercise_7.py
    
    → Modern alternative: git restore --staged exercises/solo/exercise_7.py

STEP 10: Check status again
    $ git status
    
    → File should be red (modified, not staged)
    → BUT your code changes are still there!

STEP 11: Re-stage and commit
    $ git add exercises/solo/exercise_7.py
    $ git commit -m "Exercise 7: Implement merge_sorted_arrays"

=============================================================================
PART C: Restore file from a specific commit
=============================================================================

STEP 12: Make another change and commit it
    → Add a comment: # Oops, wrong comment
    $ git add exercises/solo/exercise_7.py
    $ git commit -m "Add wrong comment"

STEP 13: View recent commits
    $ git log --oneline -3
    
    → Note the hash of your "Implement merge_sorted_arrays" commit

STEP 14: Restore the file from that older commit
    $ git checkout <commit-hash> -- exercises/solo/exercise_7.py
    
    → This replaces the current file with the version from that commit
    → The change is staged automatically

STEP 15: Commit this restoration
    $ git commit -m "Restore exercise_7 to correct version"

STEP 16: Push everything
    $ git push origin main

=============================================================================

COMMAND SUMMARY:

# Discard unstaged changes (working directory)
git checkout -- <file>
git restore <file>               # modern

# Unstage changes (but keep in working directory)
git reset HEAD <file>
git restore --staged <file>      # modern

# Restore file from specific commit
git checkout <commit> -- <file>
git restore --source=<commit> <file>  # modern

=============================================================================
REFLECTION QUESTIONS:
- What's the difference between checkout and restore?
- Why might you want to unstage a file but keep the changes?
- How can you recover a file that was deleted several commits ago?
=============================================================================
"""
