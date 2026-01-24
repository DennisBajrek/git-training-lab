# Git First Aid 🚑

Things go wrong. Here's how to fix common Git mistakes.

---

## Quick Fixes

| Problem | Solution |
|---------|----------|
| Undo last commit (keep changes) | `git reset --soft HEAD~1` |
| Discard all local changes | `git checkout -- .` |
| I'm in "detached HEAD" state | `git checkout main` |
| Push was rejected | `git pull --rebase origin main` then push |
| Committed to wrong branch | See [detailed fix below](#committed-to-wrong-branch) |

---

## "I want to undo my last commit"

### Keep the changes (uncommit but don't lose work)
```bash
git reset --soft HEAD~1
```
Your files stay modified, ready to edit or recommit.

### Discard the changes completely
```bash
git reset --hard HEAD~1
```
⚠️ **Warning:** This permanently deletes those changes!

### Already pushed? Use revert instead
```bash
git revert HEAD
```
Creates a new commit that undoes the previous one (safe for shared branches).

---

## "I want to discard my local changes"

### Discard changes to one file
```bash
git checkout -- filename.py
# or (modern)
git restore filename.py
```

### Discard ALL local changes
```bash
git checkout -- .
# or
git restore .
```

### Also remove untracked files
```bash
# See what would be deleted (dry run)
git clean -n

# Actually delete
git clean -f

# Delete untracked directories too
git clean -fd
```

---

## "I committed to the wrong branch"

### Scenario: Committed to `main` but meant to commit to a feature branch

**Step 1:** Create the feature branch at current position
```bash
git branch feature/my-work
```

**Step 2:** Move `main` back to where it was
```bash
git reset --hard HEAD~1  # Go back 1 commit
# or go back to where origin/main is
git reset --hard origin/main
```

**Step 3:** Switch to feature branch and continue
```bash
git checkout feature/my-work
```

Your commit is now on the feature branch, not main!

---

## "I'm in detached HEAD state"

This happens when you checkout a specific commit instead of a branch.

```
You are in 'detached HEAD' state...
```

### If you just want to get back to normal
```bash
git checkout main  # or whatever branch you were on
```

### If you made commits you want to keep
```bash
# Create a new branch at current position
git checkout -b my-detached-work

# Now you have a proper branch with your commits
```

---

## "My push was rejected"

```
! [rejected]        main -> main (fetch first)
```

This means someone else pushed changes since you last pulled.

### Solution 1: Pull and merge
```bash
git pull origin main
# Fix any merge conflicts if they occur
git push origin main
```

### Solution 2: Pull with rebase (cleaner history)
```bash
git pull --rebase origin main
# Fix any conflicts if they occur
git push origin main
```

---

## "I have merge conflicts"

When you see:
```
CONFLICT (content): Merge conflict in filename.py
```

### Step 1: Open the conflicted file
You'll see conflict markers:
```python
<<<<<<< HEAD
your code here
=======
their code here
>>>>>>> branch-name
```

### Step 2: Choose what to keep
Edit the file to keep the right code. Remove ALL conflict markers.

### Step 3: Mark as resolved
```bash
git add filename.py
```

### Step 4: Complete the merge
```bash
git commit  # or git merge --continue
```

### Want to abort and start over?
```bash
git merge --abort
```

---

## "I need to undo a rebase"

If a rebase went wrong:

### While rebase is in progress
```bash
git rebase --abort
```

### After rebase completed
Find the commit before rebase using reflog:
```bash
git reflog
# Find the entry before the rebase started
# Example: HEAD@{5}: checkout: moving from feature to main

git reset --hard HEAD@{5}
```

---

## "I accidentally committed a secret/password"

### If you haven't pushed yet
```bash
# Remove the commit, keep changes
git reset --soft HEAD~1

# Remove the secret from the file
# Add the file to .gitignore

# Recommit without the secret
git add .
git commit -m "Your message"
```

### If you already pushed
**⚠️ THE SECRET IS COMPROMISED**

1. **Immediately rotate the secret** (new API key, new password)
2. Remove from future commits:
   ```bash
   # Remove the file from Git (keep locally)
   git rm --cached secrets.txt
   echo "secrets.txt" >> .gitignore
   git commit -m "Remove secrets file"
   git push
   ```

3. For complete removal from history, use [BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/)

---

## "I want to see what I just did"

### See recent actions
```bash
git reflog
```
Shows everything you've done (commits, checkouts, rebases).

### See last commit
```bash
git show
# or
git log -1
```

### See what changed
```bash
git diff           # Unstaged changes
git diff --staged  # Staged changes
```

---

## "I accidentally deleted a branch"

### If you remember the commit hash
```bash
git checkout -b recovered-branch <commit-hash>
```

### If you don't remember the hash
```bash
# Find it in reflog
git reflog | grep "branch-name"

# Or look for your commit messages
git reflog | grep "your commit message"

# Then recover
git checkout -b recovered-branch <hash>
```

---

## "I want to change my last commit message"

### Not pushed yet
```bash
git commit --amend -m "New message"
```

### Want to edit in editor
```bash
git commit --amend
# Opens editor, change message, save
```

### Already pushed (requires force push)
```bash
git commit --amend -m "New message"
git push --force origin branch-name
```
⚠️ Only do this if no one else is working on the branch!

---

## "I want to add something to my last commit"

```bash
# Stage the forgotten file
git add forgotten-file.py

# Add it to the last commit
git commit --amend --no-edit
```

---

## "Everything is broken and I want to start over"

### Reset to match remote exactly
```bash
git fetch origin
git reset --hard origin/main
```
⚠️ **Warning:** This discards ALL local changes and commits not on remote.

### Nuclear option: Re-clone
```bash
cd ..
rm -rf project-folder
git clone <url>
```

---

## The Magic Undo: Reflog

`git reflog` is your time machine. It shows everything Git has done:

```bash
git reflog
```

Output:
```
a1b2c3d HEAD@{0}: commit: Latest commit
f4e5d6c HEAD@{1}: commit: Previous commit
g7h8i9j HEAD@{2}: checkout: moving from feature to main
k0l1m2n HEAD@{3}: commit: Work on feature
```

To go back to any point:
```bash
git reset --hard HEAD@{2}  # Go back to HEAD@{2}
```

**Reflog entries expire after ~90 days.** Don't wait too long to recover!

---

## Quick Reference Card

```bash
# Undo & Reset
git reset --soft HEAD~1     # Uncommit, keep changes staged
git reset HEAD~1            # Uncommit, keep changes unstaged
git reset --hard HEAD~1     # Uncommit, delete changes

# Discard Changes
git checkout -- <file>      # Discard file changes
git restore <file>          # Same (modern)
git clean -fd               # Remove untracked files/dirs

# Recovery
git reflog                  # See history of actions
git checkout -b <new> <hash># Recover deleted branch

# Abort Operations
git merge --abort           # Cancel merge
git rebase --abort          # Cancel rebase
git cherry-pick --abort     # Cancel cherry-pick

# Fix Last Commit
git commit --amend          # Edit last commit
```

---

## When In Doubt

1. **Don't panic** — Git rarely loses data
2. **Check reflog** — Your work is probably there
3. **Ask for help** — Show someone your `git status` and `git log`
4. **Worst case** — Clone fresh and manually copy your changes

---

*Back to [main README](../README.md)*
