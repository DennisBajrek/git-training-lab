"""
Run this script to see your progress locally.
Usage: python run_tests.py
"""

import subprocess
import sys


def run_tests():
    print("\n🧪 Running tests...\n")

    # Run pytest quietly and capture output
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/", "-v", "--tb=no"],
        capture_output=True,
        text=True,
    )

    output = result.stdout

    # Count results per exercise
    exercises = {
        "Exercise 1 (Reverse String)": "TestExercise1",
        "Exercise 2 (FizzBuzz)": "TestExercise2",
        "Exercise 3 (Find Max)": "TestExercise3",
        "Exercise 4 (Count Vowels)": "TestExercise4",
        "Exercise 5 (Palindrome)": "TestExercise5",
        "Exercise 6 (Two Sum)": "TestExercise6",
        "Exercise 7 (Merge Arrays)": "TestExercise7",
        "Exercise 8 (Group Anagrams)": "TestExercise8",
        "Exercise 9 (Valid Parentheses)": "TestExercise9",
        "Exercise 10 (Binary Search)": "TestExercise10",
        "Exercise 11 (Email Validation)": "TestExercise11",
        "Exercise 12 (Flatten List)": "TestExercise12",
        "Exercise 13 (Remove Duplicates)": "TestExercise13",
        "Exercise 14 (Word Frequency)": "TestExercise14",
        "Exercise 15 (Version Parser)": "TestExercise15",
    }

    total_passed = 0
    total_tests = 0

    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║           🎓 GIT TRAINING LAB - PROGRESS REPORT 🎓            ║")
    print("╚═══════════════════════════════════════════════════════════════╝")
    print()

    results = []

    for label, test_class in exercises.items():
        lines = output.split("\n")
        passed = sum(1 for line in lines if test_class in line and "PASSED" in line)
        failed = sum(1 for line in lines if test_class in line and "FAILED" in line)
        total = passed + failed

        total_passed += passed
        total_tests += total

        if passed == total and total > 0:
            results.append(f"✅ {label:<35} - COMPLETE ({passed}/{total})")
        else:
            results.append(f"⬜ {label:<35} - {passed}/{total} passing")

    print(f"📊 Overall: {total_passed} / {total_tests} tests passing")
    print()

    for r in results:
        print(r)

    print()
    print("─────────────────────────────────────────────────────────────────")

    if total_passed == total_tests and total_tests > 0:
        print("🎉 CONGRATULATIONS! All exercises complete!")
    else:
        print("💪 Keep going! Complete the exercises marked with ⬜")
        print()
        print("Tip: Run 'python run_tests.py' anytime to check progress!")

    print()


if __name__ == "__main__":
    run_tests()
