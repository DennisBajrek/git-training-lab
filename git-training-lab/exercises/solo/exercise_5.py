"""
Exercise 5: Git Stash - Save Work for Later
============================================

GIT LEARNING GOALS:
- git stash (temporarily save uncommitted changes)
- git stash list (see stashed changes)
- git stash pop (restore and remove from stash)
- git stash apply (restore but keep in stash)
- git stash drop (discard a stash)

CODING TASK: Palindrome Check
Difficulty: ⭐⭐ Medium

INSTRUCTIONS:
1. Start implementing the function
2. STOP HALFWAY (don't finish!)
3. Use stash to save your incomplete work
4. Do something else (simulate urgent task)
5. Come back and restore your work
"""


def is_palindrome(text: str) -> bool:
    """
    Check if a string is a palindrome.
    Ignore case and non-alphanumeric characters.
    
    Examples:
        is_palindrome("racecar") → True
        is_palindrome("hello") → False
        is_palindrome("A man, a plan, a canal: Panama") → True
        is_palindrome("") → True
        is_palindrome("Was it a car or a cat I saw?") → True
    
    Args:
        text: The string to check
        
    Returns:
        True if palindrome, False otherwise
    """
    # TODO: Implement this function
    # Hint: 
    # 1. Clean the string (remove non-alphanumeric, lowercase)
    # 2. Compare the cleaned string with its reverse
    # 
    # Useful: ''.join(c for c in text if c.isalnum())
    pass


# Don't modify below this line
if __name__ == "__main__":
    test_cases = [
        ("racecar", True),
        ("hello", False),
        ("A man, a plan, a canal: Panama", True),
        ("", True),
        ("Was it a car or a cat I saw?", True),
        ("No lemon, no melon", True),
        ("Python", False),
        ("a", True),
    ]
    
    print("Testing is_palindrome...")
    for text, expected in test_cases:
        result = is_palindrome(text)
        status = "✅" if result == expected else "❌"
        print(f"  {status} is_palindrome('{text}') = {result} (expected {expected})")


"""
=============================================================================
GIT EXERCISE - Learning to Stash
=============================================================================

SCENARIO:
You're working on this exercise when suddenly your teammate needs urgent help.
You need to switch branches, but you have uncommitted changes. What do you do?

Option 1: Commit incomplete work (bad - clutters history)
Option 2: Lose your work (very bad!)
Option 3: Use git stash (perfect! ✅)

STEP 1: Start implementing is_palindrome
    → Write PART of the solution (maybe just the cleaning step)
    → DON'T finish it yet!

STEP 2: Check your status
    $ git status
    
    → You should see modified file(s)

STEP 3: Stash your incomplete work
    $ git stash
    
    → Or with a description: git stash push -m "WIP: palindrome exercise"

STEP 4: Check status again
    $ git status
    
    → Working directory is clean! Your changes are safely stashed.

STEP 5: Look at the file - your changes are "gone"
    $ cat exercises/solo/exercise_5.py | grep -A5 "# TODO"
    
    → The file is back to its original state

STEP 6: See your stash list
    $ git stash list
    
    → Shows stash@{0}, stash@{1}, etc.

STEP 7: Simulate doing urgent work on another branch
    $ git checkout -b urgent-fix
    $ echo "# Urgent fix" > urgent.txt
    $ git add urgent.txt
    $ git commit -m "Urgent fix for teammate"
    $ git checkout main
    $ git branch -D urgent-fix  # Clean up

STEP 8: Restore your stashed work
    $ git stash pop
    
    → Your incomplete code is back!
    → "pop" restores AND removes from stash

STEP 9: Finish implementing is_palindrome
    → Complete your code now

STEP 10: Commit the finished work
    $ git add exercises/solo/exercise_5.py
    $ git commit -m "Exercise 5: Implement is_palindrome function"
    $ git push origin main

BONUS COMMANDS:

    # Stash including untracked files
    $ git stash -u
    
    # Apply stash without removing it from the list
    $ git stash apply
    
    # Apply a specific stash
    $ git stash apply stash@{1}
    
    # Delete a stash without applying
    $ git stash drop stash@{0}
    
    # Clear all stashes (careful!)
    $ git stash clear

=============================================================================
REFLECTION QUESTIONS:
- When would you use 'stash apply' instead of 'stash pop'?
- What happens if you stash multiple times?
- Why is stash better than committing incomplete work?
=============================================================================
"""
