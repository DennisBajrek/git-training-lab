"""
Exercise 14: Git Blame and Log - Understanding Code History
============================================================

GIT LEARNING GOALS:
- git blame (see who changed each line)
- git log -p (see patches in log)
- git log --follow (track file renames)
- git show (examine specific commits)
- Understanding code archaeology

CODING TASK: Word Frequency Counter
Difficulty: ⭐⭐ Medium

INSTRUCTIONS:
1. Learn to investigate code history
2. Understand who wrote what and why
3. Use history to understand code decisions
"""


def word_frequency(text: str) -> dict:
    """
    Count the frequency of each word in a text.

    Words are case-insensitive and split by whitespace.
    Punctuation attached to words should be stripped.

    Examples:
        word_frequency("hello world hello") -> {"hello": 2, "world": 1}
        word_frequency("The the THE") -> {"the": 3}
        word_frequency("Hello, World!") -> {"hello": 1, "world": 1}
        word_frequency("") -> {}

    Args:
        text: Input text string

    Returns:
        Dictionary mapping words to their counts
    """
    # TODO: Implement word_frequency
    #
    # Approach:
    # 1. Convert text to lowercase
    # 2. Split into words by whitespace
    # 3. Strip punctuation from each word
    # 4. Count occurrences using a dictionary
    #
    # Hint: Use str.strip() with punctuation chars, or str.isalnum()
    pass


# Don't modify below this line - used for local testing
if __name__ == "__main__":
    test_cases = [
        ("hello world hello", {"hello": 2, "world": 1}),
        ("The the THE", {"the": 3}),
        ("Hello, World!", {"hello": 1, "world": 1}),
        ("", {}),
        ("one", {"one": 1}),
        ("a a a b b c", {"a": 3, "b": 2, "c": 1}),
        ("Hello... World!!!", {"hello": 1, "world": 1}),
    ]

    print("Testing word_frequency...")
    for text, expected in test_cases:
        result = word_frequency(text)
        status = "+" if result == expected else "x"
        print(f"  {status} word_frequency('{text}') = {result}")


"""
=============================================================================
GIT EXERCISE - Blame and Log: Code Archaeology
=============================================================================

SCENARIO:
You're debugging an issue and need to understand:
- Who wrote this code?
- What was the original intention?
- When and why was it changed?

Git blame and log are your tools for investigating code history.

=============================================================================
PART A: Setup - Create some history to explore
=============================================================================

STEP 1: Make sure you're on main
    $ git checkout main

STEP 2: Implement word_frequency and commit
    -> Complete the TODO above
    $ git add exercises/solo/exercise_14.py
    $ git commit -m "Exercise 14: Implement word_frequency"

STEP 3: Add a modification
    -> Change the function slightly (maybe add a comment or improve it)
    $ git add exercises/solo/exercise_14.py
    $ git commit -m "Improve word_frequency implementation"

STEP 4: Add another modification
    -> Add or modify a docstring
    $ git add exercises/solo/exercise_14.py
    $ git commit -m "Update word_frequency documentation"

=============================================================================
PART B: Using Git Blame
=============================================================================

STEP 5: See who wrote each line
    $ git blame exercises/solo/exercise_14.py

    Output shows:
    - Commit hash (short)
    - Author
    - Date
    - Line number
    - Line content

STEP 6: Blame with better formatting
    $ git blame -w exercises/solo/exercise_14.py

    -> -w ignores whitespace changes

    $ git blame -L 20,40 exercises/solo/exercise_14.py

    -> Only show lines 20-40

STEP 7: Blame a specific function
    $ git blame -L :word_frequency exercises/solo/exercise_14.py

    -> Shows only the word_frequency function!

=============================================================================
PART C: Using Git Log for History
=============================================================================

STEP 8: See commit history for this file
    $ git log exercises/solo/exercise_14.py

    -> Shows all commits that touched this file

STEP 9: See the actual changes (patches)
    $ git log -p exercises/solo/exercise_14.py

    -> Shows the diff for each commit

STEP 10: See a summary of changes
    $ git log --stat exercises/solo/exercise_14.py

    -> Shows files changed and lines added/deleted

STEP 11: Search for commits mentioning a term
    $ git log --grep="word_frequency"

    -> Finds commits with "word_frequency" in the message

STEP 12: Search for commits changing specific code
    $ git log -S "def word_frequency" -- exercises/solo/exercise_14.py

    -> Finds commits that added or removed "def word_frequency"
    -> This is called "pickaxe" search

=============================================================================
PART D: Using Git Show
=============================================================================

STEP 13: Examine a specific commit
    $ git show HEAD

    -> Shows the most recent commit with full diff

STEP 14: Show just the message and stats
    $ git show HEAD --stat

STEP 15: Show a file at a specific commit
    $ git show HEAD~2:exercises/solo/exercise_14.py

    -> Shows the file as it was 2 commits ago

=============================================================================
PART E: Advanced History Investigation
=============================================================================

STEP 16: Find when a line was added
    $ git log -p -S "specific text" -- exercises/solo/exercise_14.py

    -> Find when "specific text" was introduced

STEP 17: Follow file renames
    $ git log --follow exercises/solo/exercise_14.py

    -> Tracks history even if file was renamed

STEP 18: Show commits by author
    $ git log --author="Your Name" exercises/solo/exercise_14.py

    -> Only shows your commits

STEP 19: Show commits in date range
    $ git log --since="1 week ago" exercises/solo/exercise_14.py

=============================================================================
PART F: Push your work
=============================================================================

STEP 20: Push all your commits
    $ git push origin main

=============================================================================

BLAME AND LOG REFERENCE:

# Git Blame
git blame <file>                  # Basic blame
git blame -w <file>               # Ignore whitespace
git blame -L 10,20 <file>         # Lines 10-20 only
git blame -L :function <file>     # Specific function
git blame -C <file>               # Detect code moved from other files
git blame <commit> -- <file>      # Blame at specific commit

# Git Log
git log <file>                    # History of file
git log -p <file>                 # With diffs
git log --stat <file>             # With change stats
git log --follow <file>           # Track renames
git log --grep="text"             # Search messages
git log -S "code"                 # Search code changes
git log --author="name"           # Filter by author
git log --since="date"            # Filter by date
git log --oneline                 # Compact format

# Git Show
git show <commit>                 # Show commit details
git show <commit>:<file>          # Show file at commit
git show <commit> --stat          # Show with stats

=============================================================================

REAL-WORLD USE CASES:

1. Bug Investigation
   -> Use blame to find who introduced problematic code
   -> Use log -p to understand the context of changes

2. Code Review Preparation
   -> Use log to understand history before reviewing

3. Understanding Legacy Code
   -> Use blame to find the original author to ask questions
   -> Use log --grep to find related commits

4. Finding When Something Broke
   -> Use log -S to find when specific code was changed

=============================================================================
REFLECTION QUESTIONS:
- When would you use blame vs log?
- Why is --follow important for renamed files?
- How does -S (pickaxe) differ from --grep?
=============================================================================
"""
