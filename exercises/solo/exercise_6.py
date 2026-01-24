"""
Exercise 6: Undoing Commits - Reset vs Revert
==============================================

GIT LEARNING GOALS:
- git reset --soft (undo commit, keep staged)
- git reset (undo commit, keep unstaged)
- git reset --hard (undo commit AND discard changes)
- git revert (create new commit that undoes)
- When to use each

CODING TASK: Two Sum
Difficulty: ⭐⭐ Medium

INSTRUCTIONS:
1. First, make an INTENTIONALLY BAD commit
2. Practice undoing it with reset
3. Then implement correctly
4. Practice revert to understand the difference
"""


def two_sum(nums: list, target: int) -> list:
    """
    Find two numbers in the list that add up to the target.
    Return their indices.
    
    You may assume exactly one solution exists.
    
    Examples:
        two_sum([2, 7, 11, 15], 9) → [0, 1]  (because 2 + 7 = 9)
        two_sum([3, 2, 4], 6) → [1, 2]       (because 2 + 4 = 6)
        two_sum([3, 3], 6) → [0, 1]          (because 3 + 3 = 6)
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List containing the two indices
    """
    # TODO: Implement this function
    # 
    # Approach 1 (O(n²) - simpler):
    #   Use nested loops to check all pairs
    #
    # Approach 2 (O(n) - optimal):
    #   Use a dictionary to store seen numbers
    #   For each number, check if (target - number) exists in dict
    pass


# Don't modify below this line
if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9, {(0, 1)}),
        ([3, 2, 4], 6, {(1, 2)}),
        ([3, 3], 6, {(0, 1)}),
        ([1, 2, 3, 4, 5], 9, {(3, 4)}),
    ]
    
    print("Testing two_sum...")
    for nums, target, valid_answers in test_cases:
        result = two_sum(nums, target)
        if result is None:
            print(f"  ❌ two_sum({nums}, {target}) = None (not implemented)")
        else:
            result_tuple = tuple(sorted(result))
            status = "✅" if result_tuple in valid_answers else "❌"
            print(f"  {status} two_sum({nums}, {target}) = {result}")


"""
=============================================================================
GIT EXERCISE - Reset vs Revert
=============================================================================

PART A: Make a bad commit and RESET it

STEP 1: Make an intentionally wrong implementation
    → Add this bad code to two_sum:
    
        return [0, 0]  # Wrong on purpose!

STEP 2: Commit this bad code
    $ git add exercises/solo/exercise_6.py
    $ git commit -m "Exercise 6: Implement two_sum (WRONG)"

STEP 3: Check your log
    $ git log --oneline -3

STEP 4: Reset to undo the commit (soft - keeps changes staged)
    $ git reset --soft HEAD~1
    
    → HEAD~1 means "one commit before HEAD"
    → Your changes are still staged

STEP 5: Check status
    $ git status
    
    → File is staged but commit is gone

STEP 6: Unstage and discard the bad changes
    $ git reset HEAD exercises/solo/exercise_6.py
    $ git checkout -- exercises/solo/exercise_6.py

STEP 7: Now implement it CORRECTLY!

STEP 8: Commit the correct version
    $ git add exercises/solo/exercise_6.py
    $ git commit -m "Exercise 6: Implement two_sum correctly"
    $ git push origin main

=============================================================================

PART B: Understanding REVERT (after you've pushed)

IMPORTANT: Once you push, others might depend on your commits.
You should NOT use reset to rewrite pushed history.
Instead, use revert.

STEP 9: Let's simulate this. Make another small change and push it:
    → Add a comment to the file: # This is a test comment
    $ git add exercises/solo/exercise_6.py
    $ git commit -m "Add test comment (will revert)"
    $ git push origin main

STEP 10: Now let's undo that commit with revert
    $ git log --oneline -2
    → Copy the hash of the "Add test comment" commit

    $ git revert <that-hash>
    → This opens an editor for the revert commit message
    → Save and close (or use --no-edit flag)

STEP 11: Check the log
    $ git log --oneline -3
    
    → You now have THREE commits:
      1. The original
      2. "Add test comment"
      3. "Revert 'Add test comment'"
    
    → History is preserved! This is safe for shared branches.

STEP 12: Push the revert
    $ git push origin main

=============================================================================

RESET vs REVERT - When to use each:

RESET (rewrites history):
  ✅ Undo commits you haven't pushed yet
  ✅ Cleaning up local work before pushing
  ❌ NEVER on commits others have pulled

REVERT (preserves history):
  ✅ Undo commits that are already pushed
  ✅ When you need a clear audit trail
  ✅ Safe for shared branches

RESET modes:
  --soft  : Undo commit, keep changes staged
  (none)  : Undo commit, keep changes unstaged
  --hard  : Undo commit AND discard changes (careful!)

=============================================================================
REFLECTION QUESTIONS:
- Why is reset dangerous on pushed commits?
- When would you use --soft vs --hard?
- How does revert maintain a clear history?
=============================================================================
"""
