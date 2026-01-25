"""
Exercise 8: Merge Conflicts - Working with a Team
==================================================

GIT LEARNING GOALS:
- Understanding merge conflicts
- Resolving conflicts manually
- git merge --abort (cancel a merge)
- Best practices for conflict resolution

CODING TASK: Group Anagrams
Difficulty: ⭐⭐ Medium

INSTRUCTIONS:
This is a COLLABORATIVE exercise. You'll work with a simulated 
"teammate" whose changes conflict with yours.

1. Create your solution on a branch
2. Try to merge with your teammate's branch
3. Resolve the conflict
4. Complete the merge
"""


def group_anagrams(words: list) -> list:
    """
    Group anagrams together.

    Two strings are anagrams if they contain the same characters
    with the same frequencies, just rearranged.

    Examples:
        group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        → [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

        group_anagrams([""])
        → [[""]]

        group_anagrams(["a"])
        → [["a"]]

    Note: The order of groups and order within groups doesn't matter
    for the tests.

    Args:
        words: List of strings

    Returns:
        List of lists, where each inner list contains anagrams
    """
    # TEAMMATE'S IMPLEMENTATION
    # Using Counter to create character frequency signature
    from collections import Counter

    anagram_map = {}
    for word in words:
        # Create a signature from character counts
        signature = tuple(sorted(Counter(word).items()))
        if signature not in anagram_map:
            anagram_map[signature] = []
        anagram_map[signature].append(word)

    return list(anagram_map.values())


# Don't modify below this line
if __name__ == "__main__":
    def compare_anagram_groups(result, expected):
        """Compare anagram groups regardless of order."""
        if result is None:
            return False
        # Convert to sets of frozensets for comparison
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
        (["abc", "bca", "cab", "xyz", "zyx"], [["abc", "bca", "cab"], ["xyz", "zyx"]]),
    ]
    
    print("Testing group_anagrams...")
    for words, expected in test_cases:
        result = group_anagrams(words)
        status = "✅" if compare_anagram_groups(result, expected) else "❌"
        print(f"  {status} group_anagrams({words})")
        if result:
            print(f"      Got: {result}")


"""
=============================================================================
GIT EXERCISE - Resolving Merge Conflicts
=============================================================================

SCENARIO:
You and a teammate are both implementing group_anagrams. You both started
from the same point but took different approaches. When you try to merge,
Git can't automatically combine your changes - you have a CONFLICT!

This repo includes a branch called "teammate/exercise-8" with a different
implementation. You'll merge it with yours and resolve the conflict.

=============================================================================
STEP 1: Create your branch
=============================================================================

    $ git checkout main
    $ git checkout -b my-exercise-8

=============================================================================
STEP 2: Implement your solution
=============================================================================

    → Write your implementation of group_anagrams
    → Use the hint about sorting characters as keys

    $ git add exercises/collaborative/exercise_8.py
    $ git commit -m "My implementation of group_anagrams"

=============================================================================
STEP 3: Fetch the teammate's branch from the remote
=============================================================================

    $ git fetch origin teammate/exercise-8

    → This downloads the branch from GitHub to your local machine
    → Without this step, Git won't know about the teammate's branch!

=============================================================================
STEP 4: Try to merge your teammate's branch
=============================================================================

    $ git merge origin/teammate/exercise-8

    → You'll see something like:
      CONFLICT (content): Merge conflict in exercises/collaborative/exercise_8.py
      Automatic merge failed; fix conflicts and then commit the result.

    → Note: We use "origin/teammate/exercise-8" (with origin/) because
      this is a remote-tracking branch we fetched, not a local branch.

=============================================================================
STEP 5: Examine the conflict
=============================================================================

    $ git status

    → Shows the file as "both modified"

    Open exercises/collaborative/exercise_8.py in your editor.
    You'll see conflict markers:

    <<<<<<< HEAD
    # Your code is here
    =======
    # Teammate's code is here
    >>>>>>> origin/teammate/exercise-8

=============================================================================
STEP 6: Resolve the conflict
=============================================================================

    To resolve the conflict, you need to:
    
    1. Decide which code to keep (yours, theirs, or a combination)
    2. Remove the conflict markers (<<<<<<, ======, >>>>>>)
    3. Make sure the final code is correct

    For this exercise, examine both solutions:
    - If your teammate's solution is better, use theirs
    - If yours is better, use yours
    - You can also combine the best parts of both!

    After editing, the file should have NO conflict markers.

=============================================================================
STEP 7: Complete the merge
=============================================================================

    $ git add exercises/collaborative/exercise_8.py
    $ git commit -m "Merge teammate's branch, resolve conflict in group_anagrams"

    → Git recognizes this as a merge commit

=============================================================================
STEP 8: Verify the merge
=============================================================================

    $ git log --oneline --graph -10

    → You should see both branches coming together

=============================================================================
STEP 9: Test your resolution
=============================================================================

    $ python exercises/collaborative/exercise_8.py

    → Make sure tests pass!

=============================================================================
STEP 10: Merge to main and push
=============================================================================

    $ git checkout main
    $ git merge my-exercise-8
    $ git push origin main

=============================================================================

BONUS: If you want to abort a merge

If you're in the middle of a conflict and want to start over:

    $ git merge --abort

This cancels the merge and returns to the state before you tried to merge.

=============================================================================

CONFLICT PREVENTION TIPS:
- Pull frequently to stay up to date
- Communicate with teammates about who's working on what
- Make smaller, focused commits
- Review diffs before committing

=============================================================================
REFLECTION QUESTIONS:
- What causes a merge conflict?
- How can you prevent conflicts in a team?
- When might you use git merge --abort?
=============================================================================
"""
