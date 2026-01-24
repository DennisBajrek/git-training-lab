"""
Exercise 1: Your First Commit
=============================

GIT LEARNING GOALS:
- git status (check what's changed)
- git add (stage files)
- git commit (save snapshot)
- git push (upload to GitHub)

CODING TASK: Reverse a String
Difficulty: ⭐ Easy

INSTRUCTIONS:
1. Read through this file
2. Complete the TODO in the function below
3. Follow the Git steps at the bottom
"""


def reverse_string(s: str) -> str:
    return s[::-1]
    """
    Reverse the input string.

    Examples:
        reverse_string("hello") → "olleh"
        reverse_string("Python") → "nohtyP"
        reverse_string("") → ""
        reverse_string("a") → "a"

    Args:
        s: The string to reverse

    Returns:
        The reversed string
    """
    # TODO: Implement this function
    # Hint: Python has a simple way to reverse strings using slicing
    pass


# Don't modify below this line - used for local testing
if __name__ == "__main__":
    test_cases = [
        ("hello", "olleh"),
        ("Python", "nohtyP"),
        ("", ""),
        ("a", "a"),
        ("12345", "54321"),
    ]

    print("Testing reverse_string...")
    for input_val, expected in test_cases:
        result = reverse_string(input_val)
        status = "✅" if result == expected else "❌"
        print(
            f"  {status} reverse_string('{input_val}') = '{result}' (expected '{expected}')"
        )


"""
=============================================================================
GIT EXERCISE - Follow these steps after completing the code:
=============================================================================

STEP 1: Check the current status
    $ git status
    
    → You should see this file listed as "modified"
    → Notice it's in RED (not yet staged)

STEP 2: See what you changed
    $ git diff exercises/solo/exercise_1.py
    
    → Lines starting with + are additions
    → Lines starting with - are deletions

STEP 3: Stage your changes
    $ git add exercises/solo/exercise_1.py
    
STEP 4: Check status again
    $ git status
    
    → Now the file should be GREEN (staged)

STEP 5: Commit your changes
    $ git commit -m "Exercise 1: Implement reverse_string function"
    
    → Notice the commit message describes WHAT you did

STEP 6: Push to GitHub
    $ git push origin main
    
    → Your changes are now on GitHub!

STEP 7: Check GitHub Actions
    → Go to your repo on GitHub
    → Click the "Actions" tab
    → Watch your tests run!

=============================================================================
REFLECTION QUESTIONS (think about these):
- What's the difference between git add and git commit?
- Why do we write descriptive commit messages?
- What does "staged" mean in Git?
=============================================================================
"""
