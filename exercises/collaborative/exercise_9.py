"""
Exercise 9: Rebase and Pull Requests
=====================================

GIT LEARNING GOALS:
- git rebase (replay commits on top of another branch)
- git rebase vs git merge (when to use each)
- Interactive rebase basics
- Creating a Pull Request on GitHub
- Code review workflow

CODING TASK: Valid Parentheses
Difficulty: ⭐⭐⭐ Harder

INSTRUCTIONS:
This is the final collaborative exercise. You'll:
1. Create a feature branch
2. Implement the solution
3. Rebase onto an updated main
4. Create a Pull Request
"""


def is_valid_parentheses(s: str) -> bool:
    """
    Determine if the input string has valid parentheses.
    
    A string is valid if:
    - Open brackets are closed by the same type of brackets
    - Open brackets are closed in the correct order
    - Every close bracket has a corresponding open bracket
    
    The string may contain: '(', ')', '{', '}', '[', ']'
    
    Examples:
        is_valid_parentheses("()") → True
        is_valid_parentheses("()[]{}") → True
        is_valid_parentheses("(]") → False
        is_valid_parentheses("([)]") → False
        is_valid_parentheses("{[]}") → True
        is_valid_parentheses("") → True
        is_valid_parentheses("((())") → False
    
    Args:
        s: String containing only parentheses characters
        
    Returns:
        True if valid, False otherwise
    """
    # TODO: Implement this function
    #
    # Hint: Use a stack!
    # 1. When you see an opening bracket, push it onto the stack
    # 2. When you see a closing bracket:
    #    - If stack is empty → invalid
    #    - If top of stack isn't matching opener → invalid
    #    - Otherwise, pop from stack
    # 3. At the end, stack should be empty
    #
    # Matching pairs: () {} []
    pass


# Don't modify below this line
if __name__ == "__main__":
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("((())", False),
        ("((()))", True),
        ("]", False),
        ("([{}])", True),
        ("({[]})", True),
        ("((({{{[[[]]]}}})))", True),
    ]
    
    print("Testing is_valid_parentheses...")
    for s, expected in test_cases:
        result = is_valid_parentheses(s)
        status = "✅" if result == expected else "❌"
        display_s = f'"{s}"' if s else '""'
        print(f"  {status} is_valid_parentheses({display_s}) = {result} (expected {expected})")


"""
=============================================================================
GIT EXERCISE - Rebase and Pull Requests
=============================================================================

SCENARIO:
You're working on a feature branch, but main has been updated by teammates.
Before creating a Pull Request, you'll rebase your changes on top of the
latest main to keep history clean.

This repo includes a branch "main-updated" that simulates updates to main
that happened while you were working.

=============================================================================
PART A: Work on a Feature Branch
=============================================================================

STEP 1: Start from main
    $ git checkout main
    $ git pull origin main

STEP 2: Create a feature branch
    $ git checkout -b feature/valid-parentheses

STEP 3: Implement is_valid_parentheses
    → Write your solution using the stack approach
    → Test locally: python exercises/collaborative/exercise_9.py

STEP 4: Make commits (practice atomic commits)
    First commit - basic structure:
    $ git add exercises/collaborative/exercise_9.py
    $ git commit -m "Add stack-based structure for valid parentheses"

    Second commit - complete implementation:
    $ git add exercises/collaborative/exercise_9.py
    $ git commit -m "Complete valid parentheses implementation"

STEP 5: View your branch
    $ git log --oneline main..feature/valid-parentheses
    
    → Shows commits in your branch that aren't in main

=============================================================================
PART B: Rebase onto Updated Main
=============================================================================

SCENARIO: While you were working, main was updated. Let's simulate this.

STEP 6: Simulate main being updated
    $ git checkout main
    $ git merge main-updated
    
    → Now main has commits your feature branch doesn't have

STEP 7: Go back to your feature branch
    $ git checkout feature/valid-parentheses

STEP 8: See the divergence
    $ git log --oneline --graph --all
    
    → Your branch and main have diverged

STEP 9: Rebase your branch onto main
    $ git rebase main
    
    → This "replays" your commits on top of main's new commits
    → If there are conflicts, resolve them like in Exercise 8

STEP 10: View the result
    $ git log --oneline --graph --all
    
    → Your commits are now on TOP of main's commits
    → History is linear and clean!

=============================================================================
PART C: Create a Pull Request
=============================================================================

STEP 11: Push your feature branch to GitHub
    $ git push origin feature/valid-parentheses

STEP 12: Go to GitHub in your browser
    → Navigate to your forked repository
    → You should see a banner: "feature/valid-parentheses had recent pushes"
    → Click "Compare & pull request"

STEP 13: Fill out the Pull Request
    Title: "Exercise 9: Implement valid parentheses checker"
    
    Description (example):
    ```
    ## Summary
    Implements the valid parentheses checker using a stack-based approach.
    
    ## Approach
    - Use a stack to track opening brackets
    - Match closing brackets with the top of the stack
    - Return true if stack is empty at the end
    
    ## Testing
    - All test cases pass locally
    ```

STEP 14: Review the diff
    → GitHub shows what changed
    → In a real team, a teammate would review this

STEP 15: Merge the Pull Request
    → Click "Merge pull request"
    → Choose "Squash and merge" or "Rebase and merge" for clean history
    → Click "Confirm merge"

STEP 16: Update your local main
    $ git checkout main
    $ git pull origin main

STEP 17: Clean up
    $ git branch -d feature/valid-parentheses
    $ git push origin --delete feature/valid-parentheses  # delete remote branch

=============================================================================

MERGE vs REBASE:

MERGE creates a merge commit:
    A - B - C - - - F (main)
         \\       /
          D - E - (feature)

REBASE replays commits:
    A - B - C - D' - E' (main after rebase+merge)

WHEN TO USE EACH:
- Rebase: For your own feature branches before merging (clean history)
- Merge: For shared branches or when history matters

GOLDEN RULE: Never rebase commits that others have built on!

=============================================================================

INTERACTIVE REBASE (BONUS):

You can clean up commits before pushing:

    $ git rebase -i HEAD~3

This lets you:
- Squash commits together
- Reorder commits
- Edit commit messages
- Drop commits

=============================================================================
REFLECTION QUESTIONS:
- Why rebase before creating a PR?
- What's the difference between "Squash and merge" vs "Rebase and merge"?
- Why should you never rebase public/shared branches?
=============================================================================
"""
