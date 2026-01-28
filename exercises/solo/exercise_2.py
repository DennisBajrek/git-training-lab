"""
Exercise 2: Exploring Git History
==================================

GIT LEARNING GOALS:
- git log (view commit history)
- git log --oneline (compact history)
- git show (inspect a specific commit)
- git diff (compare changes)

CODING TASK: FizzBuzz
Difficulty: ⭐ Easy

INSTRUCTIONS:
1. Complete the FizzBuzz function below
2. Make your commit in MULTIPLE small commits (practice atomic commits)
3. Then explore the history using git log
"""


def fizzbuzz(n: int) -> list:
    """
    Generate FizzBuzz sequence from 1 to n.
    
    Rules:
    - For multiples of 3, use "Fizz"
    - For multiples of 5, use "Buzz"  
    - For multiples of both 3 and 5, use "FizzBuzz"
    - Otherwise, use the number as a string
    
    Examples:
        fizzbuzz(5) → ["1", "2", "Fizz", "4", "Buzz"]
        fizzbuzz(15) → ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
    
    Args:
        n: Generate sequence from 1 to n (inclusive)
        
    Returns:
        List of strings following FizzBuzz rules
    """
    # TODO: Implement FizzBuzz
    # Hint: Use a loop and check divisibility with the modulo operator (%)
    def fizzbuzz(n: int) -> list:
        result = []
        for i in range(1, n + 1):
            result.append(str(i))
            return result


# Don't modify below this line
if __name__ == "__main__":
    print("Testing fizzbuzz...")
    result = fizzbuzz(15)
    expected = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
    
    if result == expected:
        print("✅ fizzbuzz(15) is correct!")
    else:
        print("❌ fizzbuzz(15) failed")
        print(f"   Got:      {result}")
        print(f"   Expected: {expected}")
    
    # Edge cases
    print(f"  fizzbuzz(1) = {fizzbuzz(1)}")
    print(f"  fizzbuzz(3) = {fizzbuzz(3)}")


"""
=============================================================================
GIT EXERCISE - Follow these steps:
=============================================================================

PART A: Make atomic commits (commit small, logical pieces)

Instead of one big commit, let's practice making smaller commits:

1. First, implement just the basic number case (no Fizz/Buzz logic)
    $ git add exercises/solo/exercise_2.py
    $ git commit -m "Exercise 2: Add basic loop structure for fizzbuzz"

2. Then add the Fizz logic (divisible by 3)
    $ git add exercises/solo/exercise_2.py
    $ git commit -m "Exercise 2: Add Fizz logic for multiples of 3"

3. Then add the Buzz logic (divisible by 5)
    $ git add exercises/solo/exercise_2.py
    $ git commit -m "Exercise 2: Add Buzz logic for multiples of 5"

4. Finally add the FizzBuzz case (divisible by both)
    $ git add exercises/solo/exercise_2.py
    $ git commit -m "Exercise 2: Add FizzBuzz for multiples of 3 and 5"

(If you already did it all at once, that's okay! Just make one commit and continue.)

PART B: Explore your history

5. View your commit log
    $ git log
    
    → Notice each commit has: hash, author, date, message
    → Press 'q' to exit

6. View compact log
    $ git log --oneline
    
    → Much cleaner! Shows short hash + message

7. View log with graph (useful for branches later)
    $ git log --oneline --graph

8. Inspect a specific commit (copy a hash from the log)
    $ git show <commit-hash>
    
    Example: git show a1b2c3d
    → Shows exactly what changed in that commit

9. Compare two commits
    $ git diff <older-hash> <newer-hash>

10. Push all your commits
    $ git push origin main

=============================================================================
REFLECTION QUESTIONS:
- Why might you want to make smaller, atomic commits?
- How does git log help when something breaks?
- What information does git show give you?
=============================================================================
"""
