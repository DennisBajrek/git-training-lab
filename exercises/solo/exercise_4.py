"""
Exercise 4: Working with Remotes
=================================

GIT LEARNING GOALS:
- git remote (manage remote connections)
- git fetch (download without merging)
- git pull (download and merge)
- Understanding remote tracking branches

CODING TASK: Count Vowels
Difficulty: ⭐ Easy

INSTRUCTIONS:
1. Before coding, simulate pulling updates from a teammate
2. Implement the function
3. Push your changes
"""


def count_vowels(text: str) -> int:

    """
    Count the number of vowels (a, e, i, o, u) in a string.
    Case-insensitive.
    
    Examples:
        count_vowels("hello") → 2
        count_vowels("AEIOU") → 5
        count_vowels("rhythm") → 0
        count_vowels("") → 0
        count_vowels("Python Programming") → 4
    
    Args:
        text: The input string
        
    Returns:
        Number of vowels in the string
    """
    # TODO: Implement this function
    # Hint: Convert to lowercase first, then count vowels

    vowels = "aeiou"

    text = text.lower()

    count = 0

    for letter in text:
        if letter in vowels:
            count += 1


    return count

    


# Don't modify below this line
if __name__ == "__main__":
    test_cases = [
        ("hello", 2),
        ("AEIOU", 5),
        ("rhythm", 0),
        ("", 0),
        ("Python Programming", 4),
        ("aEiOu", 5),
    ]
    
    print("Testing count_vowels...")
    for text, expected in test_cases:
        result = count_vowels(text)
        status = "✅" if result == expected else "❌"
        print(f"  {status} count_vowels('{text}') = {result} (expected {expected})")


"""
=============================================================================
GIT EXERCISE - Understanding Remotes
=============================================================================

BACKGROUND:
When you cloned this repo, Git automatically set up a "remote" called "origin"
pointing to the GitHub repository. Let's explore this.

STEP 1: See your configured remotes
    $ git remote -v
    
    → You should see "origin" with fetch and push URLs
    → These point to your GitHub fork

STEP 2: See remote branches
    $ git branch -a
    
    → Local branches don't have a prefix
    → Remote branches start with "remotes/origin/"

STEP 3: Fetch updates from the remote (without merging)
    $ git fetch origin
    
    → This downloads any new commits from GitHub
    → Your local files DON'T change yet
    → This is safe to run anytime

STEP 4: See if you're behind the remote
    $ git status
    
    → If GitHub has new commits, it will tell you:
      "Your branch is behind 'origin/main' by X commits"

STEP 5: Now implement count_vowels above!

STEP 6: Commit your changes
    $ git add exercises/solo/exercise_4.py
    $ git commit -m "Exercise 4: Implement count_vowels function"

STEP 7: Before pushing, always pull first (good habit!)
    $ git pull origin main
    
    → This is equivalent to: git fetch + git merge
    → If someone pushed changes while you worked, this merges them

STEP 8: Push your changes
    $ git push origin main

BONUS: Understanding origin/main vs main

    "main" = your local branch
    "origin/main" = your local COPY of what's on GitHub
    
    When you fetch: origin/main updates to match GitHub
    When you merge origin/main into main: your local branch updates
    When you push: GitHub updates to match your local main
    
    $ git log --oneline main           # Your local commits
    $ git log --oneline origin/main    # What GitHub has (as of last fetch)

=============================================================================
REFLECTION QUESTIONS:
- What's the difference between fetch and pull?
- Why might you fetch before pull?
- What happens if you push without pulling first and someone else pushed?
=============================================================================
"""
