"""
Exercise 13: Amend and Squash - Cleaning Up History
====================================================

GIT LEARNING GOALS:
- git commit --amend (modify the last commit)
- git rebase -i (interactive rebase for squashing)
- Squashing multiple commits into one
- Writing better commit messages

CODING TASK: Remove Duplicates
Difficulty: ⭐⭐ Medium

INSTRUCTIONS:
1. Learn to fix commit messages and combine commits
2. Practice amending before pushing
3. Understand when it's safe to rewrite history
"""


def remove_duplicates(nums: list) -> list:
    """
    Remove duplicates from a list while preserving order.

    Returns a new list with only the first occurrence of each element.

    Examples:
        remove_duplicates([1, 2, 2, 3, 1]) -> [1, 2, 3]
        remove_duplicates([1, 1, 1, 1]) -> [1]
        remove_duplicates([1, 2, 3]) -> [1, 2, 3]
        remove_duplicates([]) -> []
        remove_duplicates(['a', 'b', 'a', 'c']) -> ['a', 'b', 'c']

    Args:
        nums: List with possible duplicates

    Returns:
        New list with duplicates removed, order preserved
    """
    # TODO: Implement remove_duplicates
    #
    # Approach:
    # 1. Create empty result list and a set for "seen" items
    # 2. For each item in nums:
    #    - If not in seen set, add to result and seen
    # 3. Return result
    #
    # Note: Use a set for O(1) lookup of seen items
    pass


# Don't modify below this line - used for local testing
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 2, 3, 1], [1, 2, 3]),
        ([1, 1, 1, 1], [1]),
        ([1, 2, 3], [1, 2, 3]),
        ([], []),
        (['a', 'b', 'a', 'c'], ['a', 'b', 'c']),
        ([5, 4, 3, 2, 1, 1, 2, 3], [5, 4, 3, 2, 1]),
        ([1], [1]),
    ]

    print("Testing remove_duplicates...")
    for nums, expected in test_cases:
        result = remove_duplicates(nums)
        status = "+" if result == expected else "x"
        print(f"  {status} remove_duplicates({nums}) = {result}")


"""
=============================================================================
GIT EXERCISE - Amend and Squash
=============================================================================

SCENARIO:
You've made several small commits while working on a feature:
- "WIP"
- "fix typo"
- "oops forgot a file"
- "actually working now"

Before pushing, you want to combine these into one clean commit.
This exercise teaches you how to clean up your commit history.

=============================================================================
PART A: Amending the Last Commit
=============================================================================

STEP 1: Create a branch for this exercise
    $ git checkout main
    $ git checkout -b feature/remove-duplicates

STEP 2: Make a commit with a typo in the message
    -> Implement remove_duplicates above (just the first part)
    $ git add exercises/solo/exercise_13.py
    $ git commit -m "Implment remove_duplicates"  # Typo!

STEP 3: Fix the typo with amend
    $ git commit --amend -m "Implement remove_duplicates"

    -> The commit message is fixed!
    -> NOTE: The commit hash changes (it's a new commit)

STEP 4: Verify
    $ git log --oneline -1

    -> Message should be corrected

=============================================================================
PART B: Amending to Add Forgotten Files
=============================================================================

STEP 5: Simulate forgetting to add a change
    -> Add a comment: # Helper function below
    -> Don't commit yet (pretend you forgot)

STEP 6: Make another commit for something else
    -> Add another comment: # TODO: Add more test cases
    $ git add exercises/solo/exercise_13.py
    $ git commit -m "Add TODO comment"

STEP 7: Oops! You wanted that first comment in the previous commit
    -> You can't easily amend now (there's a commit in between)
    -> This is where interactive rebase helps!

=============================================================================
PART C: Interactive Rebase - Squashing Commits
=============================================================================

STEP 8: Make a few more "messy" commits
    -> Change the TODO comment
    $ git add exercises/solo/exercise_13.py
    $ git commit -m "WIP"

    -> Change it again
    $ git add exercises/solo/exercise_13.py
    $ git commit -m "more changes"

    -> And again
    $ git add exercises/solo/exercise_13.py
    $ git commit -m "fix"

STEP 9: View your messy history
    $ git log --oneline -6

    -> You'll see multiple small commits

STEP 10: Start interactive rebase
    $ git rebase -i HEAD~5

    -> Opens an editor with your last 5 commits
    -> Each line starts with "pick"

STEP 11: Modify the rebase instructions

    Original:
    pick abc1234 Implement remove_duplicates
    pick def5678 Add TODO comment
    pick 111aaaa WIP
    pick 222bbbb more changes
    pick 333cccc fix

    Change to (squash the last 4 into the first):
    pick abc1234 Implement remove_duplicates
    squash def5678 Add TODO comment
    squash 111aaaa WIP
    squash 222bbbb more changes
    squash 333cccc fix

    -> "squash" (or "s") combines into previous commit
    -> Save and close the editor

STEP 12: Edit the combined commit message
    -> An editor opens with all the commit messages
    -> Write a single, clean message:
       "Implement remove_duplicates function"
    -> Save and close

STEP 13: Verify the squash
    $ git log --oneline -3

    -> You should have one clean commit instead of 5!

=============================================================================
PART D: Rebase Commands Cheatsheet
=============================================================================

In the interactive rebase editor:

pick   (p) - use commit as-is
reword (r) - use commit but edit the message
edit   (e) - use commit but stop for amending
squash (s) - combine with previous commit (keep message)
fixup  (f) - like squash but discard this commit's message
drop   (d) - remove commit entirely

=============================================================================
PART E: Merge to main and push
=============================================================================

STEP 14: Merge your clean branch to main
    $ git checkout main
    $ git merge feature/remove-duplicates

STEP 15: Push
    $ git push origin main

STEP 16: Clean up
    $ git branch -d feature/remove-duplicates

=============================================================================

SAFETY RULES FOR REWRITING HISTORY:

+ Amend commits you haven't pushed yet
+ Squash commits on your feature branch before pushing
+ Clean up local history before sharing

- NEVER amend or rebase commits already pushed to a shared branch
- NEVER force push to main/master
- If you've pushed, use revert instead of rebase

=============================================================================

COMMON AMEND/SQUASH COMMANDS:

# Amend last commit message
git commit --amend -m "New message"

# Amend last commit to include staged changes
git add forgotten-file.py
git commit --amend --no-edit

# Interactive rebase last N commits
git rebase -i HEAD~N

# Abort a rebase if something goes wrong
git rebase --abort

# Continue rebase after resolving conflicts
git rebase --continue

=============================================================================
REFLECTION QUESTIONS:
- Why does amending change the commit hash?
- When is it safe to use interactive rebase?
- Why would you use fixup instead of squash?
=============================================================================
"""
