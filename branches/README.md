# Branches Folder

This folder contains reference files that represent the content of special branches used in collaborative exercises.

## Purpose

These files simulate "teammate" work without requiring actual team coordination. They help you practice:
- Merge conflict resolution
- Rebasing with upstream changes
- Real-world collaboration scenarios

## Files

### `teammate-exercise-8.py`

**Used in:** Exercise 8 (Merge Conflicts)

This file contains a teammate's implementation of the `group_anagrams` function using a different approach. When you merge the `teammate/exercise-8` branch, you'll encounter conflicts with your own implementation.

**Branch:** `origin/teammate/exercise-8`

### `main-updated-content.py`

**Used in:** Exercise 9 (Rebase)

This file simulates updates to `main` that happened while you were working on your feature branch. It demonstrates why rebasing is useful to incorporate upstream changes.

**Branch:** `origin/main-updated`

## How These Are Used

### Exercise 8 Flow:
```bash
# You implement group_anagrams your way
git checkout -b my-anagrams
# ... implement ...
git commit -m "My implementation"

# Your "teammate" already pushed their version
git fetch origin
git merge origin/teammate/exercise-8

# CONFLICT! Resolve it to complete the exercise
```

### Exercise 9 Flow:
```bash
# You're working on a feature branch
git checkout -b my-feature

# Meanwhile, main received updates (main-updated branch simulates this)
git fetch origin
git rebase origin/main-updated

# Your feature now includes the latest main changes
```

## Note

You don't need to edit these files directly. They exist as reference material and to create the pre-made branches in the remote repository.

The actual branches (`teammate/exercise-8` and `main-updated`) are already set up in the remote repository for you to fetch and work with.
