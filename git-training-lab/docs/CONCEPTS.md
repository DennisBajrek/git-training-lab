# Git Concepts Guide 📖

Before diving into exercises, let's understand what Git is and why it matters.

---

## What is Git?

Git is a **distributed version control system**. Let's break that down:

- **Version control**: Tracks changes to files over time, letting you go back to any previous version
- **Distributed**: Every developer has a complete copy of the project history on their machine

### Why Does This Matter?

1. **No single point of failure** — If a server dies, every developer has a full backup
2. **Work offline** — Commit, branch, view history without internet
3. **Fast operations** — Most actions happen locally (no network latency)
4. **Easy branching** — Create experimental branches freely

---

## How Git Stores Data

Unlike other version control systems, Git thinks of data as **snapshots**, not differences.

```
Traditional VCS:  File1: v1 → Δ1 → Δ2 → Δ3
                  (stores changes)

Git:              Commit1 → Commit2 → Commit3
                  (stores complete snapshots)
```

Each commit is a snapshot of ALL your files at that moment. Git is smart about this—if a file hasn't changed, it just links to the previous version.

### The Three States

Files in Git exist in three states:

```
┌─────────────────────────────────────────────────────────┐
│                    Your Computer                         │
│                                                          │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐ │
│  │   Working    │   │   Staging    │   │    Local     │ │
│  │  Directory   │──▶│    Area      │──▶│  Repository  │ │
│  │              │   │  (Index)     │   │   (.git)     │ │
│  └──────────────┘   └──────────────┘   └──────────────┘ │
│        │                  │                   │          │
│     git add           git commit          git push       │
│                                               │          │
└───────────────────────────────────────────────│──────────┘
                                                ▼
                                    ┌──────────────────┐
                                    │  Remote (GitHub)  │
                                    └──────────────────┘
```

1. **Working Directory**: Your actual files that you edit
2. **Staging Area** (Index): Files marked to go into the next commit
3. **Repository**: The committed history (stored in `.git` folder)

### The Staging Area — Why?

This is Git's killer feature. It lets you:

- Commit only SOME of your changes
- Review exactly what you're about to commit
- Build commits thoughtfully (atomic commits)

```bash
# Made changes to 3 files, but only want to commit 2:
git add file1.py file2.py    # Stage these two
git commit -m "Add feature"  # Commit only staged files
# file3.py changes remain in working directory
```

---

## Commits

A commit is a snapshot with metadata:

```
commit a1b2c3d4e5f6...
Author: Jane Doe <jane@example.com>
Date:   Mon Oct 23 10:30:00 2024

    Add user authentication feature
    
    - Implement login/logout
    - Add password hashing
    - Create session management
```

Each commit has:
- A unique SHA hash (like `a1b2c3d4...`)
- Author info
- Timestamp
- Commit message
- Pointer to parent commit(s)

### Good Commit Messages

```bash
# Bad ❌
git commit -m "fix"
git commit -m "updates"
git commit -m "asdfasdf"

# Good ✅
git commit -m "Fix null pointer exception in user login"
git commit -m "Add input validation to registration form"
git commit -m "Refactor database connection pooling"
```

**Rule of thumb**: If someone reads only your commit message, can they understand what changed and why?

---

## Branches

A branch is just a **pointer to a commit**. That's it.

```
        main
          ↓
    A ← B ← C
              ↖
                D ← E
                    ↑
                feature
```

### Why Branching is "Cheap" in Git

Creating a branch = creating a 41-byte file (the pointer). It doesn't copy any files.

This means you can:
- Create branches freely for experiments
- Have many parallel features in development
- Delete branches without losing history (commits remain)

### Common Branch Workflow

```bash
# Start new feature
git checkout -b feature/user-profile

# Work, commit, work, commit...
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

Your local repo can connect to remote repos (like GitHub):

```
Your Machine                     GitHub
┌─────────────┐                ┌─────────────┐
│ Local Repo  │ ◄── pull ───── │   Remote    │
│             │ ─── push ────▶ │    Repo     │
└─────────────┘                └─────────────┘
```

### Key Commands

```bash
git remote -v              # See connected remotes
git fetch origin           # Download updates (don't merge)
git pull origin main       # Fetch + merge
git push origin feature    # Upload your branch
```

### Fetch vs Pull

- `git fetch`: Downloads updates but doesn't change your files
- `git pull`: Downloads AND merges (fetch + merge)

When unsure, `fetch` first to see what changed.

---

## Merging vs Rebasing

Two ways to integrate changes:

### Merge
Creates a "merge commit" that combines two histories:

```
Before:
    A ← B ← C (main)
         ↖
           D ← E (feature)

After git merge:
    A ← B ← C ← F (main)  ← merge commit
         ↖     ↗
           D ← E
```

### Rebase
Replays your commits on top of another branch:

```
Before:
    A ← B ← C (main)
         ↖
           D ← E (feature)

After git rebase main (from feature):
    A ← B ← C (main)
              ↖
                D' ← E' (feature)  ← commits "moved"
```

### When to Use Which?

- **Merge**: Preserves history exactly as it happened (good for shared branches)
- **Rebase**: Creates cleaner linear history (good for feature branches before merging)

**Golden rule**: Never rebase commits that others have based work on.

---

## Undoing Things

Git has multiple ways to undo, depending on what you need:

### Uncommitted Changes

```bash
# Discard changes in working directory
git checkout -- filename.py
# or (newer syntax)
git restore filename.py

# Unstage a file (keep changes)
git reset HEAD filename.py
# or
git restore --staged filename.py
```

### Committed Changes

```bash
# Undo last commit, keep changes staged
git reset --soft HEAD~1

# Undo last commit, keep changes unstaged
git reset HEAD~1

# Undo last commit, discard changes (careful!)
git reset --hard HEAD~1

# Create new commit that undoes a previous commit (safe for shared branches)
git revert <commit-hash>
```

### The Difference: Reset vs Revert

- `reset`: Moves the branch pointer backward (rewrites history)
- `revert`: Creates a NEW commit that undoes changes (preserves history)

**Use `revert` on shared branches** — never rewrite history others depend on.

---

## Stashing

Temporarily save uncommitted changes:

```bash
# Save current changes
git stash

# Do other work, switch branches, etc.

# Bring changes back
git stash pop
```

Useful when you need to quickly switch context but aren't ready to commit.

---

## Quick Reference

| Command | What it does |
|---------|--------------|
| `git init` | Create new repo |
| `git clone <url>` | Copy remote repo |
| `git status` | See current state |
| `git add <file>` | Stage changes |
| `git commit -m "msg"` | Save snapshot |
| `git push` | Upload to remote |
| `git pull` | Download & merge |
| `git branch <name>` | Create branch |
| `git checkout <name>` | Switch branch |
| `git merge <branch>` | Combine branches |
| `git log` | View history |
| `git diff` | See changes |
| `git stash` | Temporarily save |
| `git reset` | Undo commits |
| `git revert` | Undo with new commit |

---

## Next Steps

Now that you understand the concepts, head back to the [main README](../README.md) and start the exercises!

Remember: The best way to learn Git is by using it. Don't worry about making mistakes—Git makes it hard to truly lose work.

*Happy learning! 🚀*
