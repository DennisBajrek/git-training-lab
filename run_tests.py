"""
Run this script to see your progress locally.
Usage: python run_tests.py
"""

import subprocess
import sys


def run_tests():
    print("\n🧪 Running tests...\n")

    # Run pytest quietly and capture output (only test_exercises.py for progress report)
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/test_exercises.py", "-v", "--tb=no"],
        capture_output=True,
        text=True,
    )

    output = result.stdout

    # Count results per exercise, organized by section
    sections = {
        "Fundamentals:": {
            "Exercise 1 (Reverse String)": "TestExercise1",
            "Exercise 2 (FizzBuzz)": "TestExercise2",
            "Exercise 3 (Find Max)": "TestExercise3",
            "Exercise 4 (Count Vowels)": "TestExercise4",
            "Exercise 5 (Palindrome)": "TestExercise5",
            "Exercise 6 (Two Sum)": "TestExercise6",
            "Exercise 7 (Merge Arrays)": "TestExercise7",
        },
        "Collaborative:": {
            "Exercise 8 (Group Anagrams)": "TestExercise8",
            "Exercise 9 (Valid Parentheses)": "TestExercise9",
        },
        "Advanced:": {
            "Exercise 10 (Binary Search)": "TestExercise10",
            "Exercise 11 (Email Validation)": "TestExercise11",
            "Exercise 12 (Flatten List)": "TestExercise12",
            "Exercise 13 (Remove Duplicates)": "TestExercise13",
            "Exercise 14 (Word Frequency)": "TestExercise14",
            "Exercise 15 (Version Parser)": "TestExercise15",
        },
    }

    total_passed = 0
    total_tests = 0

    results = []

    for section_name, exercises in sections.items():
        results.append(section_name)
        for label, test_class in exercises.items():
            lines = output.split("\n")
            # Use "::" suffix to avoid matching TestExercise1 with TestExercise10, etc.
            # Check for "%" to only count main test output, not summary section
            class_pattern = f"{test_class}::"
            passed = sum(
                1
                for line in lines
                if class_pattern in line and " PASSED" in line and "%" in line
            )
            failed = sum(
                1
                for line in lines
                if class_pattern in line and " FAILED" in line and "%" in line
            )
            total = passed + failed

            total_passed += passed
            total_tests += total

            if passed == total and total > 0:
                results.append(f"✅ {label:<35} - COMPLETE ({passed}/{total})")
            else:
                results.append(f"⬜ {label:<35} - {passed}/{total} passing")
        results.append("")  # Empty line after section

    print(f"📊 Overall: {total_passed} / {total_tests} tests passing")
    print()

    for r in results:
        print(r)

    print("─────────────────────────────────────────────────────────────────")

    if total_passed == total_tests and total_tests > 0:
        print("🎉 CONGRATULATIONS! All exercises complete!")
    else:
        print("💪 Keep going! Complete the exercises marked with ⬜")

    print()


if __name__ == "__main__":
    run_tests()
