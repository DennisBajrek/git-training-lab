# Git Cheat Sheet

A quick reference for the most common Git commands.

---

## Setup & Config

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --list                    # View all settings
```

---

## Getting Started

```bash
git init                             # Initialize new repo
git clone <url>                      # Clone existing repo
git clone <url> <folder>             # Clone into specific folder
```

---

## Daily Workflow

```bash
# Check status
git status                           # See changed files
git status -s                        # Short format

# Stage changes
git add <file>                       # Stage specific file
git add .                            # Stage all changes
git add -p                           # Stage interactively (patch mode)

# Commit
git commit -m "message"              # Commit with message
git commit -am "message"             # Add tracked files + commit
git commit --amend                   # Modify last commit

# Push/Pull
git push                             # Push to remote
git push -u origin <branch>          # Push and set upstream
git pull                             # Fetch + merge
git fetch                            # Fetch without merge
```

---

## Branching

```bash
# List branches
git branch                           # Local branches
git branch -r                        # Remote branches
git branch -a                        # All branches

# Create & switch
git branch <name>                    # Create branch
git checkout <name>                  # Switch to branch
git checkout -b <name>               # Create + switch
git switch <name>                    # Switch (modern)
git switch -c <name>                 # Create + switch (modern)

# Delete
git branch -d <name>                 # Delete merged branch
git branch -D <name>                 # Force delete branch
git push origin --delete <name>      # Delete remote branch

# Merge
git merge <branch>                   # Merge branch into current
git merge --no-ff <branch>           # Merge with commit (no fast-forward)
git merge --abort                    # Abort merge in progress
```

---

## Viewing History

```bash
git log                              # Full commit history
git log --oneline                    # Compact history
git log --oneline -10                # Last 10 commits
git log --graph                      # Visual branch history
git log --author="name"              # Filter by author
git log -p <file>                    # History with diffs for file
git log --since="2 weeks ago"        # Recent commits

git show <commit>                    # Show specific commit
git show HEAD                        # Show last commit

git diff                             # Unstaged changes
git diff --staged                    # Staged changes
git diff <branch1>..<branch2>        # Diff between branches
git diff <commit1>..<commit2>        # Diff between commits
```

---

## Undoing Things

```bash
# Discard working directory changes
git checkout -- <file>               # Old way
git restore <file>                   # Modern way

# Unstage files
git reset HEAD <file>                # Old way
git restore --staged <file>          # Modern way

# Undo commits
git reset --soft HEAD~1              # Undo commit, keep staged
git reset HEAD~1                     # Undo commit, keep unstaged
git reset --hard HEAD~1              # Undo commit, discard changes

# Safe undo (creates new commit)
git revert <commit>                  # Revert specific commit
git revert HEAD                      # Revert last commit
```

---

## Stashing

```bash
git stash                            # Stash changes
git stash push -m "message"          # Stash with message
git stash list                       # List stashes
git stash pop                        # Apply + delete latest stash
git stash apply                      # Apply without deleting
git stash apply stash@{2}            # Apply specific stash
git stash drop                       # Delete latest stash
git stash clear                      # Delete all stashes
```

---

## Remote Repositories

```bash
git remote -v                        # List remotes
git remote add <name> <url>          # Add remote
git remote remove <name>             # Remove remote
git remote rename <old> <new>        # Rename remote

git fetch origin                     # Fetch from origin
git fetch --all                      # Fetch from all remotes
git pull origin <branch>             # Pull specific branch
git push origin <branch>             # Push specific branch
```

---

## Advanced Commands

```bash
# Cherry-pick
git cherry-pick <commit>             # Apply specific commit
git cherry-pick --abort              # Abort cherry-pick

# Rebase
git rebase <branch>                  # Rebase onto branch
git rebase -i HEAD~3                 # Interactive rebase (last 3)
git rebase --abort                   # Abort rebase
git rebase --continue                # Continue after conflict

# Bisect (find bad commit)
git bisect start                     # Start bisect
git bisect bad                       # Mark current as bad
git bisect good <commit>             # Mark commit as good
git bisect reset                     # End bisect

# Reflog (recovery)
git reflog                           # Show HEAD history
git reflog show <branch>             # Show branch history

# Tags
git tag                              # List tags
git tag v1.0.0                       # Lightweight tag
git tag -a v1.0.0 -m "msg"           # Annotated tag
git push origin --tags               # Push all tags

# Blame
git blame <file>                     # Show who changed each line
git blame -L 10,20 <file>            # Blame lines 10-20
```

---

## Cleaning Up

```bash
git clean -n                         # Dry run - show what would be deleted
git clean -f                         # Delete untracked files
git clean -fd                        # Delete untracked files + directories
git gc                               # Garbage collection
git prune                            # Remove unreachable objects
```

---

## Useful Aliases

Add these to your `~/.gitconfig`:

```ini
[alias]
    s = status -s
    co = checkout
    br = branch
    ci = commit
    lg = log --oneline --graph --decorate
    last = log -1 HEAD
    unstage = reset HEAD --
    undo = reset --soft HEAD~1
```

---

## Quick Reference Table

| Task | Command |
|------|---------|
| Save work temporarily | `git stash` |
| Get stashed work back | `git stash pop` |
| Undo last commit (keep changes) | `git reset --soft HEAD~1` |
| Discard all local changes | `git checkout -- .` |
| See what changed | `git diff` |
| See commit history | `git log --oneline` |
| Create and switch to branch | `git checkout -b <name>` |
| Merge branch | `git merge <branch>` |
| Update from remote | `git pull` |
| Push to remote | `git push` |

---

## Emergency Commands

```bash
# "I messed up, how do I undo?"
git reflog                           # Find the commit you want
git reset --hard <commit>            # Go back to it

# "I committed to wrong branch"
git reset --soft HEAD~1              # Undo commit, keep changes
git checkout <correct-branch>        # Switch branches
git commit -m "message"              # Recommit

# "I need to undo a pushed commit"
git revert <commit>                  # Creates new "undo" commit
git push                             # Push the revert

# "I deleted a branch with important work"
git reflog                           # Find the commit
git branch <name> <commit>           # Recreate branch
```

---

*Keep this handy! Print it out or bookmark it.*
