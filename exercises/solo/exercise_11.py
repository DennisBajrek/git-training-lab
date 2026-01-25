"""
Exercise 11: Git Bisect - Finding Bug-Introducing Commits
==========================================================

GIT LEARNING GOALS:
- git bisect start (begin a bisect session)
- git bisect bad (mark current commit as broken)
- git bisect good <commit> (mark a commit as working)
- git bisect reset (end the bisect session)
- Understanding binary search through commit history

CODING TASK: Validate Email
Difficulty: ⭐⭐ Medium

INSTRUCTIONS:
1. This exercise simulates finding when a bug was introduced
2. You'll use git bisect to efficiently search through history
3. Learn the most powerful debugging tool in Git
"""


def validate_email(email: str) -> bool:
    """
    Check if an email address is valid.

    A valid email must have:
    - At least one character before @
    - Exactly one @ symbol
    - At least one character between @ and .
    - At least one . after @
    - At least two characters after the last .

    Examples:
        validate_email("user@example.com") -> True
        validate_email("test.user@domain.org") -> True
        validate_email("invalid") -> False
        validate_email("no@dot") -> False
        validate_email("@nodomain.com") -> False
        validate_email("spaces not@allowed.com") -> False

    Args:
        email: The email string to validate

    Returns:
        True if valid, False otherwise
    """
    # TODO: Implement email validation
    #
    # Approach:
    # 1. Check for exactly one @
    # 2. Split by @ into local and domain parts
    # 3. Check local part is not empty and has no spaces
    # 4. Check domain has at least one . with valid parts
    #
    # Hint: You can use string methods like count(), split(), etc.
    pass


# Don't modify below this line - used for local testing
if __name__ == "__main__":
    test_cases = [
        ("user@example.com", True),
        ("test.user@domain.org", True),
        ("name@subdomain.domain.com", True),
        ("invalid", False),
        ("no@dot", False),
        ("@nodomain.com", False),
        ("nodomain@.com", False),
        ("spaces not@allowed.com", False),
        ("double@@at.com", False),
        ("", False),
        ("a@b.co", True),
        ("test@domain.c", False),  # TLD too short
    ]

    print("Testing validate_email...")
    for email, expected in test_cases:
        result = validate_email(email)
        status = "+" if result == expected else "x"
        print(f"  {status} validate_email('{email}') = {result} (expected {expected})")


"""
=============================================================================
GIT EXERCISE - Bisect: Finding the Bug
=============================================================================

SCENARIO:
Your tests were passing last week, but now they're failing. You have
100 commits since then. Instead of checking each one manually, use
git bisect to find the bad commit in just 7 steps (log2(100) ~ 7)!

Git bisect uses binary search through your commit history.

=============================================================================
PART A: Understanding Bisect Conceptually
=============================================================================

Imagine you have 8 commits:

    A - B - C - D - E - F - G - H (HEAD, tests fail)

You know commit A worked (tests passed). Somewhere between A and H,
a bug was introduced.

Bisect process:
1. Start: Mark H as bad, A as good
2. Git checks out D (middle): You test it
3. If D is bad: Bug is in A-D, check B
4. If D is good: Bug is in D-H, check F
5. Continue halving until you find the exact commit

=============================================================================
PART B: Setup for Bisect Practice
=============================================================================

For this exercise, we'll simulate a bug being introduced.

STEP 1: Make sure you're on main with a clean state
    $ git checkout main
    $ git status

STEP 2: Create the "working" version
    -> Implement validate_email correctly above
    $ git add exercises/solo/exercise_11.py
    $ git commit -m "Exercise 11: Implement validate_email"

STEP 3: Save this commit hash (the "good" commit)
    $ git log --oneline -1
    -> Write down this hash: ____________

STEP 4: Make a few more commits (simulating ongoing work)
    -> Add a comment: # Version 1
    $ git add exercises/solo/exercise_11.py
    $ git commit -m "Add version comment"

    -> Change comment to: # Version 2
    $ git add exercises/solo/exercise_11.py
    $ git commit -m "Update to version 2"

STEP 5: Now "introduce a bug" - break the function
    -> Change the function to return False always:
       return False  # BUG!
    $ git add exercises/solo/exercise_11.py
    $ git commit -m "Refactor validation logic"

STEP 6: Make more commits after the bug
    -> Add comment: # Version 3
    $ git add exercises/solo/exercise_11.py
    $ git commit -m "Update to version 3"

    -> Add comment: # Version 4
    $ git add exercises/solo/exercise_11.py
    $ git commit -m "Update to version 4"

=============================================================================
PART C: Use Bisect to Find the Bug
=============================================================================

STEP 7: Start bisect
    $ git bisect start

STEP 8: Mark current HEAD as bad (tests fail)
    $ git bisect bad

STEP 9: Mark the known good commit
    $ git bisect good <hash-from-step-3>

    -> Git will checkout a commit in the middle
    -> You'll see: "Bisecting: X revisions left to test"

STEP 10: Test the current commit
    $ python exercises/solo/exercise_11.py

    -> If tests pass: $ git bisect good
    -> If tests fail: $ git bisect bad

STEP 11: Repeat step 10
    -> Git automatically checks out the next commit to test
    -> Keep marking good or bad

STEP 12: Find the culprit!
    -> Eventually Git will say:
       "<hash> is the first bad commit"
    -> This is the commit that introduced the bug!

STEP 13: Examine the bad commit
    $ git show <bad-commit-hash>

    -> You can see exactly what changed

STEP 14: End the bisect session
    $ git bisect reset

    -> Returns you to where you started

=============================================================================
PART D: Fix the Bug and Push
=============================================================================

STEP 15: Now that you know which commit broke things, fix it!
    -> Restore the correct implementation
    $ git add exercises/solo/exercise_11.py
    $ git commit -m "Fix validate_email bug introduced in <hash>"

STEP 16: Push
    $ git push origin main

=============================================================================

BISECT COMMANDS REFERENCE:

# Start bisect session
git bisect start

# Mark commits
git bisect bad [commit]    # Current or specified commit is broken
git bisect good [commit]   # Current or specified commit works

# Navigation during bisect
git bisect reset           # End session, return to original HEAD
git bisect skip            # Skip current commit (can't test it)

# View bisect log
git bisect log             # Shows the bisect history

# Automated bisect (advanced)
git bisect run <script>    # Auto-run a test script on each commit

=============================================================================

AUTOMATED BISECT EXAMPLE:

If you have a test that returns 0 on success, 1 on failure:

    $ git bisect start
    $ git bisect bad HEAD
    $ git bisect good abc123
    $ git bisect run python -m pytest tests/test_email.py

Git will automatically run the test on each commit and find the bad one!

=============================================================================
REFLECTION QUESTIONS:
- Why is bisect faster than checking each commit manually?
- When would you use "git bisect skip"?
- How does automated bisect save time on large codebases?
=============================================================================
"""
