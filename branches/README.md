# Branches Folder

This folder contains reference files for the special branches used in collaborative exercises.

## Purpose

These files help simulate "teammate" work without requiring actual team coordination. They're used for:
- Merge conflict resolution (Exercise 8)
- Rebase practice (Exercise 9)

## Special Branches

### `teammate/exercise-8` Branch

**Used in:** Exercise 8 (Merge Conflicts)

This branch contains a DIFFERENT implementation of `group_anagrams` using a Counter-based approach (instead of sorting). When students implement their own version and try to merge, they'll encounter a conflict.

**Key differences:**
- Student's approach: Sort characters as key (`sorted(word)`)
- Teammate's approach: Counter signature as key (`tuple(sorted(Counter(word).items()))`)

Both are valid solutions, but they'll conflict in the function body.

### `main-updated` Branch

**Used in:** Exercise 9 (Rebase)

This branch simulates updates to `main` that happened while students work on their feature branch. It contains simple, non-conflicting changes like:
- Adding a CHANGELOG.md
- Minor README updates

This teaches students to rebase their work onto updated upstream branches.

## Reference Files

### `teammate-exercise-8.py`
Reference implementation showing the teammate's Counter-based approach. This is NOT copied wholesale - only the function implementation differs on the actual branch.

### `main-updated-content.py`
Example content that simulates updates to main. The actual branch may contain different non-conflicting changes.

## How These Are Used

### Exercise 8 Flow:
```bash
# Student implements group_anagrams their way
git checkout -b my-exercise-8
# ... implement using sorted() approach ...
git commit -m "My implementation of group_anagrams"

# Try to merge teammate's branch
git merge teammate/exercise-8

# CONFLICT in exercises/collaborative/exercise_8.py!
# Resolve by choosing one approach or combining both
```

### Exercise 9 Flow:
```bash
# Student works on feature branch
git checkout -b feature/valid-parentheses
# ... implement ...
git commit -m "Implement valid parentheses"

# Simulate main getting updates
git checkout main
git merge main-updated  # Now main has new commits

# Rebase feature branch onto updated main
git checkout feature/valid-parentheses
git rebase main
```

## Updating These Branches

If you need to recreate or update these branches, see `docs/INSTRUCTOR_GUIDE.md` for instructions.
