# Git Guide 📖

How Git works and how to fix things when they go wrong.

---

# Part 1: How Git Works

## What is Git?

Git is a **distributed version control system**:
- **Version control**: Tracks changes over time, lets you go back to any version
- **Distributed**: Everyone has a complete copy of the project history

### Why This Matters

- No single point of failure — if a server dies, everyone has a backup
- Work offline — commit, branch, view history without internet
- Fast operations — most actions happen locally

---

## The Three States

Files in Git exist in three states:

```
Working Directory → Staging Area → Repository
     (edit)           (git add)     (git commit)
```

1. **Working Directory**: Your actual files that you edit
2. **Staging Area**: Files marked to go into the next commit
3. **Repository**: The committed history (in `.git` folder)

### Why the Staging Area?

It lets you:
- Commit only SOME changes
- Review what you're about to commit
- Build commits thoughtfully

```bash
# Changed 3 files, but only commit 2:
git add file1.py file2.py
git commit -m "Add feature"
# file3.py changes stay in working directory
```

---

## Commits

A commit is a snapshot of your entire project at a moment in time.

```
commit a1b2c3d4...
Author: Jane Doe <jane@example.com>
Date:   Mon Oct 23 10:30:00 2024

    Add user authentication
```

### Good Commit Messages

```bash
# Bad ❌
git commit -m "fix"
git commit -m "updates"

# Good ✅
git commit -m "Fix null pointer exception in user login"
git commit -m "Add input validation to registration form"
```

**Rule of thumb**: Could someone understand what changed just from the message?

---

## Branches

A branch is just a pointer to a commit. Creating a branch is instant and cheap.

```
        main
          ↓
    A ← B ← C
              ↖
                D ← E
                    ↑
                feature
```

### Common Workflow

```bash
# Start new feature
git checkout -b feature/user-profile

# Work and commit
git add .
git commit -m "Add profile page"

# Done? Merge back to main
git checkout main
git merge feature/user-profile

# Clean up
git branch -d feature/user-profile
```

---

## Remote Repositories

Your local repo connects to remotes (like GitHub):

```bash
git push    # Upload your commits
git pull    # Download and merge
git fetch   # Download only (don't merge)
```

### Fetch vs Pull

- `git fetch`: Downloads updates but doesn't change your files
- `git pull`: Downloads AND merges (fetch + merge)

When unsure, fetch first to see what changed.

---

## Merge vs Rebase

Two ways to integrate changes:

**Merge** — Creates a merge commit:
```bash
git checkout main
git merge feature
```

**Rebase** — Replays commits on top:
```bash
git checkout feature
git rebase main
```

**When to use:**
- Merge: For shared branches (preserves history)
- Rebase: For your own feature branches (cleaner history)

**Rule**: Never rebase commits others have based work on.

---

# Part 2: Git First Aid 🚑

## Quick Fixes

| Problem | Solution |
|---------|----------|
| Undo last commit (keep changes) | `git reset --soft HEAD~1` |
| Discard all local changes | `git checkout -- .` |
| I'm in "detached HEAD" | `git checkout main` |
| Push was rejected | `git pull origin main` then push |

---

## "I want to undo my last commit"

### Keep the changes
```bash
git reset --soft HEAD~1
```

### Discard the changes completely
```bash
git reset --hard HEAD~1
```
⚠️ This permanently deletes those changes!

### Already pushed? Use revert
```bash
git revert HEAD
```
Creates a new commit that undoes the previous one (safe for shared branches).

---

## "I want to discard local changes"

### One file
```bash
git checkout -- filename.py
# or
git restore filename.py
```

### All changes
```bash
git checkout -- .
# or
git restore .
```

---

## "I committed to the wrong branch"

```bash
# Create the feature branch at current position
git branch feature/my-work

# Move main back
git reset --hard HEAD~1

# Switch to feature branch
git checkout feature/my-work
```

---

## "I'm in detached HEAD state"

Just get back to a branch:
```bash
git checkout main
```

If you made commits you want to keep:
```bash
git checkout -b my-recovered-work
```

---

## "My push was rejected"

Someone else pushed changes. Pull first:
```bash
git pull origin main
# Fix any conflicts
git push origin main
```

Or with rebase:
```bash
git pull --rebase origin main
git push origin main
```

---

## "I have merge conflicts"

When you see conflict markers:
```python
<<<<<<< HEAD
your code
=======
their code
>>>>>>> branch-name
```

1. Edit the file — choose what to keep, remove ALL markers
2. Stage: `git add filename.py`
3. Commit: `git commit`

### Want to abort?
```bash
git merge --abort
```

---

## "I accidentally committed a secret"

### If you haven't pushed
```bash
git reset --soft HEAD~1
# Remove the secret, add to .gitignore
git add .
git commit -m "Your message"
```

### If you already pushed
**The secret is compromised. Rotate it immediately!**

---

## "Everything is broken"

### Reset to match remote
```bash
git fetch origin
git reset --hard origin/main
```
⚠️ Discards all local changes!

### Nuclear option
```bash
cd ..
rm -rf project-folder
git clone <url>
```

---

## The Magic Undo: Reflog

`git reflog` shows everything Git has done:

```bash
git reflog
```

To go back to any point:
```bash
git reset --hard HEAD@{3}
```

Reflog entries expire after ~90 days.

---

## Command Reference

```bash
# Undo
git reset --soft HEAD~1     # Uncommit, keep staged
git reset HEAD~1            # Uncommit, keep unstaged  
git reset --hard HEAD~1     # Uncommit, delete changes

# Discard
git checkout -- <file>      # Discard file changes
git restore <file>          # Same (modern)
git clean -fd               # Remove untracked files

# Recovery
git reflog                  # See history
git checkout -b <new> <hash># Recover deleted branch

# Abort
git merge --abort
git rebase --abort
```

---

*Next: Read the [Workflow Guide](WORKFLOW.md) for Jira, Slack, and code review practices.*
