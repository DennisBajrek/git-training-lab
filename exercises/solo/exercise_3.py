"""
Exercise 3: Branching Basics
=============================

GIT LEARNING GOALS:
- git branch (list/create branches)
- git checkout (switch branches) 
- git switch (newer way to switch branches)
- git checkout -b (create and switch in one command)
- git branch -d (delete branch)
- git merge (combine branches)

CODING TASK: Find Maximum in List
Difficulty: ⭐ Easy

INSTRUCTIONS:
1. Create a new branch for this exercise
2. Implement the function on that branch
3. Merge it back to main
"""


def find_max(numbers: list) -> int | None:
    if len(numbers) == 0:
        return None
    
    biggestNumber = numbers[0]

    for number in range (1, len(numbers)):
        tempNumber = number
        if tempNumber > biggestNumber:
           biggestNumber = tempNumber

        return biggestNumber
    

    """
    Find the maximum value in a list of numbers.
    
    Examples:
        find_max([1, 5, 3, 9, 2]) → 9
        find_max([-1, -5, -3]) → -1
        find_max([42]) → 42
        find_max([]) → None
    
    Args:
        numbers: List of integers
        
    Returns:
        The maximum value, or None if list is empty
    """
    # TODO: Implement this function
    # Hint: Handle the empty list case first!
    # You could use Python's built-in max(), or write your own loop
    pass


# Don't modify below this line
if __name__ == "__main__":
    test_cases = [
        ([1, 5, 3, 9, 2], 9),
        ([-1, -5, -3], -1),
        ([42], 42),
        ([], None),
        ([0, 0, 0], 0),
        ([-10, 10], 10),
    ]
    
    print("Testing find_max...")
    for numbers, expected in test_cases:
        result = find_max(numbers)
        status = "✅" if result == expected else "❌"
        print(f"  {status} find_max({numbers}) = {result} (expected {expected})")


"""
=============================================================================
GIT EXERCISE - Follow these steps:
=============================================================================

STEP 1: Make sure you're on main and up to date
    $ git checkout main
    $ git pull origin main

STEP 2: Create a new branch for this exercise
    $ git checkout -b feature/exercise-3
    
    → This creates AND switches to the new branch
    → Alternative: git branch feature/exercise-3 && git checkout feature/exercise-3
    → Modern alternative: git switch -c feature/exercise-3

STEP 3: Verify you're on the new branch
    $ git branch

    
    → The asterisk (*) shows your current branch
    → You should see: * feature/exercise-3

STEP 4: Implement the find_max function above
    (Write your code now!)

STEP 5: Commit your work on this branch
    $ git add exercises/solo/exercise_3.py
    $ git commit -m "Exercise 3: Implement find_max function"

STEP 6: See the branch structure
    $ git log --oneline --graph --all
    
    → Notice your feature branch has diverged from main

STEP 7: Switch back to main
    $ git checkout main
    
    → Or: git switch main

STEP 8: Look at the file - your changes are "gone"!
    $ cat exercises/solo/exercise_3.py | head -40
    
    → Don't worry! They're safe on your feature branch.

STEP 9: Merge your feature branch into main
    $ git merge feature/exercise-3
    
    → This brings your changes into main
    → It should say "Fast-forward" (we'll explain this later)

STEP 10: Verify the merge
    $ git log --oneline -5
    
    → Your commit is now on main

STEP 11: Delete the feature branch (it's merged, we don't need it)
    $ git branch -d feature/exercise-3
    
    → -d is safe delete (only works if merged)
    → -D is force delete (use carefully!)

STEP 12: Push to GitHub
    $ git push origin main

=============================================================================
REFLECTION QUESTIONS:
- Why work on a branch instead of directly on main?
- What does "Fast-forward" mean in a merge?
- When might you NOT delete a branch after merging?
=============================================================================
"""
