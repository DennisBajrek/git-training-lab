"""
Exercise 15: Git Tags - Marking Releases
=========================================

GIT LEARNING GOALS:
- git tag (create tags)
- Lightweight vs annotated tags
- git tag -a (annotated tags)
- Pushing tags to remote
- Using tags for releases

CODING TASK: Semantic Version Parser
Difficulty: ⭐⭐ Medium

INSTRUCTIONS:
1. Learn to create and manage tags
2. Understand semantic versioning
3. Use tags to mark release points
"""


def parse_version(version: str) -> dict:
    """
    Parse a semantic version string into its components.

    Semantic Versioning format: MAJOR.MINOR.PATCH
    - MAJOR: Breaking changes
    - MINOR: New features (backwards compatible)
    - PATCH: Bug fixes (backwards compatible)

    Examples:
        parse_version("1.2.3") -> {"major": 1, "minor": 2, "patch": 3}
        parse_version("0.1.0") -> {"major": 0, "minor": 1, "patch": 0}
        parse_version("10.20.30") -> {"major": 10, "minor": 20, "patch": 30}

    Args:
        version: Version string in "X.Y.Z" format

    Returns:
        Dictionary with major, minor, patch as integers

    Raises:
        ValueError: If version string is invalid
    """
    # TODO: Implement parse_version
    #
    # Approach:
    # 1. Split the version string by '.'
    # 2. Check that there are exactly 3 parts
    # 3. Convert each part to an integer
    # 4. Return as dictionary
    #
    # Handle errors gracefully with ValueError
    pass


def compare_versions(v1: str, v2: str) -> int:
    """
    Compare two version strings.

    Examples:
        compare_versions("1.2.3", "1.2.4") -> -1 (v1 < v2)
        compare_versions("2.0.0", "1.9.9") -> 1  (v1 > v2)
        compare_versions("1.0.0", "1.0.0") -> 0  (equal)

    Args:
        v1: First version string
        v2: Second version string

    Returns:
        -1 if v1 < v2, 0 if equal, 1 if v1 > v2
    """
    # TODO: Implement compare_versions
    #
    # Approach:
    # 1. Parse both versions
    # 2. Compare major, then minor, then patch
    # 3. Return appropriate value
    pass


# Don't modify below this line - used for local testing
if __name__ == "__main__":
    print("Testing parse_version...")
    parse_tests = [
        ("1.2.3", {"major": 1, "minor": 2, "patch": 3}),
        ("0.1.0", {"major": 0, "minor": 1, "patch": 0}),
        ("10.20.30", {"major": 10, "minor": 20, "patch": 30}),
    ]
    for version, expected in parse_tests:
        result = parse_version(version)
        status = "+" if result == expected else "x"
        print(f"  {status} parse_version('{version}') = {result}")

    print("\nTesting compare_versions...")
    compare_tests = [
        ("1.2.3", "1.2.4", -1),
        ("2.0.0", "1.9.9", 1),
        ("1.0.0", "1.0.0", 0),
        ("1.0.0", "1.0.1", -1),
        ("1.1.0", "1.0.9", 1),
    ]
    for v1, v2, expected in compare_tests:
        result = compare_versions(v1, v2)
        status = "+" if result == expected else "x"
        print(f"  {status} compare_versions('{v1}', '{v2}') = {result} (expected {expected})")


"""
=============================================================================
GIT EXERCISE - Tags: Marking Releases
=============================================================================

SCENARIO:
Your project is ready for release! You want to mark this point in history
with a version number. Later, you (or anyone) can easily check out exactly
what was in v1.0.0.

Tags are like bookmarks in your commit history.

=============================================================================
PART A: Understanding Tags
=============================================================================

Two types of tags:

LIGHTWEIGHT TAG:
- Just a pointer to a commit
- Like a branch that doesn't move
- Created with: git tag v1.0.0

ANNOTATED TAG (Recommended):
- Full object in Git database
- Contains tagger name, email, date, message
- Can be signed with GPG
- Created with: git tag -a v1.0.0 -m "Release v1.0.0"

=============================================================================
PART B: Create Your First Release
=============================================================================

STEP 1: Make sure you're on main with clean state
    $ git checkout main
    $ git status

STEP 2: Implement the version functions and commit
    -> Complete both TODOs above
    $ git add exercises/solo/exercise_15.py
    $ git commit -m "Exercise 15: Implement version parsing and comparison"

STEP 3: Create a lightweight tag
    $ git tag v0.1.0

STEP 4: View your tags
    $ git tag

    -> Lists all tags

STEP 5: View tag details
    $ git show v0.1.0

    -> For lightweight tags, shows the commit it points to

=============================================================================
PART C: Create an Annotated Tag
=============================================================================

STEP 6: Make another improvement
    -> Add a comment or small improvement to the code
    $ git add exercises/solo/exercise_15.py
    $ git commit -m "Improve version comparison"

STEP 7: Create an annotated tag with message
    $ git tag -a v0.2.0 -m "Release v0.2.0 - Improved version comparison"

STEP 8: View the annotated tag
    $ git show v0.2.0

    -> Shows tagger info, date, message, AND the commit

=============================================================================
PART D: Tagging Past Commits
=============================================================================

STEP 9: Find a past commit to tag
    $ git log --oneline -5

    -> Pick a commit hash from the past

STEP 10: Tag that past commit
    $ git tag -a v0.0.1 <commit-hash> -m "Initial version"

STEP 11: Verify all tags
    $ git tag -l

    -> Should show v0.0.1, v0.1.0, v0.2.0

STEP 12: View tags with their commits
    $ git log --oneline --decorate

    -> Tags appear next to their commits

=============================================================================
PART E: Pushing Tags to Remote
=============================================================================

STEP 13: Push a single tag
    $ git push origin v0.2.0

STEP 14: Push all tags at once
    $ git push origin --tags

STEP 15: Verify tags on GitHub
    -> Go to your repo on GitHub
    -> Click "Releases" or "Tags" section
    -> You should see your tags!

=============================================================================
PART F: Working with Tags
=============================================================================

STEP 16: Checkout a specific tag
    $ git checkout v0.1.0

    -> You're now in "detached HEAD" state
    -> You're viewing the code exactly as it was at v0.1.0

STEP 17: Return to main
    $ git checkout main

STEP 18: Create a branch from a tag
    $ git checkout -b hotfix/v0.1.1 v0.1.0

    -> Creates a branch starting from the tagged commit
    -> Useful for hotfixes on old releases

STEP 19: Return to main
    $ git checkout main
    $ git branch -d hotfix/v0.1.1

=============================================================================
PART G: Deleting Tags
=============================================================================

STEP 20: Delete a local tag
    $ git tag -d v0.0.1

STEP 21: Delete a remote tag
    $ git push origin --delete v0.0.1

    -> Or: git push origin :refs/tags/v0.0.1

=============================================================================

TAG COMMANDS REFERENCE:

# Create tags
git tag v1.0.0                        # Lightweight tag
git tag -a v1.0.0 -m "Message"        # Annotated tag
git tag -a v1.0.0 <commit>            # Tag a specific commit

# List tags
git tag                               # List all tags
git tag -l "v1.*"                     # List tags matching pattern
git tag -n                            # List tags with messages

# View tags
git show v1.0.0                       # Show tag details
git log --oneline --decorate          # Show commits with tags

# Push tags
git push origin v1.0.0                # Push specific tag
git push origin --tags                # Push all tags

# Delete tags
git tag -d v1.0.0                     # Delete local tag
git push origin --delete v1.0.0       # Delete remote tag

# Checkout tags
git checkout v1.0.0                   # View code at tag (detached HEAD)
git checkout -b branch v1.0.0         # Create branch from tag

=============================================================================

SEMANTIC VERSIONING RECAP:

Version format: MAJOR.MINOR.PATCH

Increment MAJOR when: Breaking changes (not backwards compatible)
Increment MINOR when: New features (backwards compatible)
Increment PATCH when: Bug fixes (backwards compatible)

Pre-release: v1.0.0-alpha, v1.0.0-beta.1
Build metadata: v1.0.0+build.123

Example progression:
v0.1.0 -> v0.1.1 (bug fix)
v0.1.1 -> v0.2.0 (new feature)
v0.2.0 -> v1.0.0 (first stable release, or breaking change)

=============================================================================

RELEASE WORKFLOW:

1. Finish all features for the release
2. Update version number in code (if applicable)
3. Update CHANGELOG
4. Commit: "Prepare release v1.0.0"
5. Create annotated tag: git tag -a v1.0.0 -m "Release v1.0.0"
6. Push commits and tags: git push origin main --tags
7. Create GitHub Release (optional, links to tag)

=============================================================================
REFLECTION QUESTIONS:
- Why use annotated tags instead of lightweight?
- When would you tag a past commit?
- How do tags differ from branches?
=============================================================================
"""
