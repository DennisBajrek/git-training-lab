"""
Exercise 12: Git Reflog - Recovering Lost Work
==============================================

GIT LEARNING GOALS:
- git reflog (view reference log)
- Recovering "deleted" commits
- Recovering deleted branches
- Understanding that Git rarely loses data permanently

CODING TASK: Flatten Nested List
Difficulty: ⭐⭐ Medium

INSTRUCTIONS:
1. Learn to use reflog to recover "lost" work
2. Understand that most Git mistakes are recoverable
3. This is your safety net!
"""


def flatten(nested_list: list) -> list:
    """
    Flatten a nested list into a single-level list.

    Takes a list that may contain other lists (nested to any depth)
    and returns a flat list with all elements.

    Examples:
        flatten([1, [2, 3], [4, [5, 6]]]) -> [1, 2, 3, 4, 5, 6]
        flatten([[1, 2], [3, 4]]) -> [1, 2, 3, 4]
        flatten([1, 2, 3]) -> [1, 2, 3]
        flatten([]) -> []
        flatten([[[1]]]) -> [1]

    Args:
        nested_list: A list that may contain nested lists

    Returns:
        A flat list with all elements
    """
    # TODO: Implement flatten
    #
    # Approach (recursive):
    # 1. Create empty result list
    # 2. For each item in nested_list:
    #    - If item is a list, recursively flatten it and extend result
    #    - If item is not a list, append it to result
    # 3. Return result
    #
    # Hint: Use isinstance(item, list) to check if item is a list
    pass


# Don't modify below this line - used for local testing
if __name__ == "__main__":
    test_cases = [
        ([1, [2, 3], [4, [5, 6]]], [1, 2, 3, 4, 5, 6]),
        ([[1, 2], [3, 4]], [1, 2, 3, 4]),
        ([1, 2, 3], [1, 2, 3]),
        ([], []),
        ([[[1]]], [1]),
        ([1, [2, [3, [4, [5]]]]], [1, 2, 3, 4, 5]),
        ([[[[]]]], []),
        ([1, [], 2, [], 3], [1, 2, 3]),
    ]

    print("Testing flatten...")
    for nested, expected in test_cases:
        result = flatten(nested)
        status = "+" if result == expected else "x"
        print(f"  {status} flatten({nested}) = {result}")


"""
=============================================================================
GIT EXERCISE - Reflog: Your Safety Net
=============================================================================

SCENARIO:
You accidentally ran `git reset --hard` and lost hours of work.
Or you deleted a branch with important commits. DON'T PANIC!

Git's reflog keeps a record of where HEAD has been. If it was ever
committed, it can probably be recovered!

=============================================================================
PART A: Understanding Reflog
=============================================================================

The reflog (reference log) records every time HEAD changes:
- Commits
- Checkouts
- Resets
- Merges
- Rebases

Even if a commit is "unreachable" from any branch, reflog remembers it
for at least 30 days (configurable).

=============================================================================
PART B: Setup - Create work to "lose"
=============================================================================

STEP 1: Make sure you're on main
    $ git checkout main

STEP 2: Create a branch for this exercise
    $ git checkout -b important-work

STEP 3: Implement flatten and commit
    -> Complete the TODO above
    $ git add exercises/solo/exercise_12.py
    $ git commit -m "Exercise 12: Implement flatten function"

STEP 4: Add more commits
    -> Add a comment: # This is important work!
    $ git add exercises/solo/exercise_12.py
    $ git commit -m "Add important comment"

    -> Add another comment: # Don't lose this!
    $ git add exercises/solo/exercise_12.py
    $ git commit -m "Add another important comment"

STEP 5: Check your log
    $ git log --oneline -4

    -> Note your commit hashes

=============================================================================
PART C: Simulate Disaster - Lose Your Work
=============================================================================

STEP 6: Go back to main
    $ git checkout main

STEP 7: "Accidentally" delete the branch!
    $ git branch -D important-work

    -> The -D flag force deletes even unmerged branches
    -> Your commits are now "lost"!

STEP 8: Verify the branch is gone
    $ git branch

    -> important-work is not listed

    $ git log --oneline -4

    -> Your commits are gone from the log!

=============================================================================
PART D: Recovery with Reflog
=============================================================================

STEP 9: Check the reflog
    $ git reflog

    -> You'll see a history of HEAD positions
    -> Look for your "Add another important comment" entry
    -> Note its hash (e.g., abc1234)

    Example output:
    def4567 HEAD@{0}: checkout: moving from important-work to main
    abc1234 HEAD@{1}: commit: Add another important comment
    789abcd HEAD@{2}: commit: Add important comment
    ...

STEP 10: Recover the lost commits by creating a new branch
    $ git branch recovered-work <hash-of-last-commit>

    -> This creates a branch pointing to that "lost" commit

STEP 11: Verify the recovery
    $ git checkout recovered-work
    $ git log --oneline -4

    -> Your commits are back!

STEP 12: Verify the file contents
    $ cat exercises/solo/exercise_12.py

    -> Your implementation and comments should be there

=============================================================================
PART E: Recover from Reset --hard
=============================================================================

STEP 13: Stay on recovered-work and make a new commit
    -> Change comment to: # Recovered and improved!
    $ git add exercises/solo/exercise_12.py
    $ git commit -m "Improve comments"

STEP 14: Now simulate an accidental hard reset
    $ git log --oneline -3  # Note current state
    $ git reset --hard HEAD~3  # Go back 3 commits!

STEP 15: Check the damage
    $ git log --oneline -3
    $ cat exercises/solo/exercise_12.py

    -> Your work is "gone"!

STEP 16: Use reflog to recover
    $ git reflog

    -> Find the "Improve comments" commit

    $ git reset --hard <hash-of-improve-comments>

    -> Your work is back!

=============================================================================
PART F: Clean up and merge to main
=============================================================================

STEP 17: Merge your recovered work to main
    $ git checkout main
    $ git merge recovered-work

STEP 18: Push
    $ git push origin main

STEP 19: Clean up branches
    $ git branch -d recovered-work

=============================================================================

REFLOG COMMANDS:

# View reflog
git reflog                    # Shows HEAD history
git reflog show <branch>      # Shows history of specific branch

# Reflog with dates
git reflog --date=relative    # Shows "2 hours ago" style dates
git reflog --date=iso         # Shows ISO format dates

# Recover using reflog
git branch <new-branch> <reflog-hash>  # Create branch at old position
git reset --hard <reflog-hash>         # Move HEAD to old position
git cherry-pick <reflog-hash>          # Copy commit to current branch

# Reflog notation
HEAD@{0}     # Current HEAD
HEAD@{1}     # Previous HEAD position
HEAD@{5}     # HEAD position 5 moves ago
HEAD@{1.week.ago}  # HEAD position 1 week ago

=============================================================================

REFLOG EXPIRATION:

By default, reflog entries expire after:
- 90 days for reachable commits
- 30 days for unreachable commits

You can configure this:
    git config gc.reflogExpire 180.days
    git config gc.reflogExpireUnreachable 90.days

=============================================================================
REFLECTION QUESTIONS:
- When is reflog more useful than regular log?
- Why does Git keep unreachable commits for 30 days?
- What's the difference between deleting a branch and losing commits?
=============================================================================
"""
