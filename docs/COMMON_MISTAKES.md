# Common Git Mistakes and How to Fix Them

Every developer makes these mistakes. Here's how to fix them.

---

## Table of Contents

1. [I committed to the wrong branch](#1-i-committed-to-the-wrong-branch)
2. [I need to undo my last commit](#2-i-need-to-undo-my-last-commit)
3. [I committed sensitive data](#3-i-committed-sensitive-data)
4. [I made a typo in my commit message](#4-i-made-a-typo-in-my-commit-message)
5. [I forgot to add a file to my commit](#5-i-forgot-to-add-a-file-to-my-commit)
6. [I accidentally deleted a branch](#6-i-accidentally-deleted-a-branch)
7. [I'm stuck in a merge conflict](#7-im-stuck-in-a-merge-conflict)
8. [I need to undo changes to a file](#8-i-need-to-undo-changes-to-a-file)
9. [My push was rejected](#9-my-push-was-rejected)
10. [I accidentally ran git reset --hard](#10-i-accidentally-ran-git-reset---hard)
11. [I need to undo a pushed commit](#11-i-need-to-undo-a-pushed-commit)
12. [I'm in detached HEAD state](#12-im-in-detached-head-state)
13. [I have too many messy commits](#13-i-have-too-many-messy-commits)
14. [My local branch is behind remote](#14-my-local-branch-is-behind-remote)
15. [I staged files I didn't want to stage](#15-i-staged-files-i-didnt-want-to-stage)

---

## 1. I committed to the wrong branch

**Scenario:** You made commits on `main` but meant to commit on `feature-branch`.

**Fix (if NOT pushed yet):**

```bash
# Move commits to the correct branch
git branch feature-branch          # Create branch at current position
git reset --hard HEAD~1            # Move main back (adjust number as needed)
git checkout feature-branch        # Switch to feature branch
```

**Fix (if already pushed):**

```bash
# On main, revert the commits
git checkout main
git revert <commit-hash>
git push

# Then cherry-pick to correct branch
git checkout feature-branch
git cherry-pick <commit-hash>
```

---

## 2. I need to undo my last commit

**Keep changes (unstaged):**
```bash
git reset HEAD~1
```

**Keep changes (staged):**
```bash
git reset --soft HEAD~1
```

**Discard changes completely:**
```bash
git reset --hard HEAD~1
```

**Undo multiple commits:**
```bash
git reset HEAD~3    # Undo last 3 commits
```

---

## 3. I committed sensitive data

**IMPORTANT:** If pushed, consider the data compromised. Rotate credentials immediately!

**If NOT pushed:**
```bash
git reset --soft HEAD~1     # Undo commit
# Remove sensitive file or data
git add .
git commit -m "message"
```

**If pushed (removes from history):**
```bash
# WARNING: Rewrites history - coordinate with team!
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch <file>" \
  --prune-empty --tag-name-filter cat -- --all

git push origin --force --all
```

Better alternative - use [BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/):
```bash
bfg --delete-files <filename>
git push --force
```

---

## 4. I made a typo in my commit message

**If NOT pushed:**
```bash
git commit --amend -m "Corrected message"
```

**If pushed:**
```bash
# WARNING: Rewrites history
git commit --amend -m "Corrected message"
git push --force-with-lease
```

Note: `--force-with-lease` is safer than `--force` as it fails if someone else pushed.

---

## 5. I forgot to add a file to my commit

**If NOT pushed:**
```bash
git add forgotten_file.py
git commit --amend --no-edit    # Adds to last commit, keeps message
```

**If pushed:**
Either make a new commit (preferred) or amend + force push (if team agrees).

---

## 6. I accidentally deleted a branch

**Find the commit:**
```bash
git reflog
```

**Look for output like:**
```
abc1234 HEAD@{5}: commit: Important work
def5678 HEAD@{6}: checkout: moving from deleted-branch to main
```

**Restore the branch:**
```bash
git branch recovered-branch abc1234
```

---

## 7. I'm stuck in a merge conflict

**See conflicted files:**
```bash
git status
```

**Option 1: Resolve manually**
1. Open each conflicted file
2. Look for conflict markers: `<<<<<<<`, `=======`, `>>>>>>>`
3. Edit to keep desired changes
4. Remove conflict markers
5. Stage and commit:
```bash
git add .
git commit -m "Resolve merge conflicts"
```

**Option 2: Abort the merge**
```bash
git merge --abort
```

**Option 3: Keep one side entirely**
```bash
git checkout --ours <file>     # Keep your version
git checkout --theirs <file>   # Keep their version
git add <file>
```

---

## 8. I need to undo changes to a file

**Discard unstaged changes:**
```bash
git checkout -- <file>        # Old way
git restore <file>            # Modern way (Git 2.23+)
```

**Discard ALL unstaged changes:**
```bash
git checkout -- .
git restore .
```

**Restore file from specific commit:**
```bash
git checkout <commit> -- <file>
git restore --source <commit> <file>
```

---

## 9. My push was rejected

**Error: "Updates were rejected because the remote contains work..."**

**Cause:** Someone else pushed commits you don't have.

**Fix (preferred):**
```bash
git pull --rebase origin <branch>
git push
```

**Fix (merge approach):**
```bash
git pull origin <branch>      # Creates merge commit
git push
```

**Error: "Updates were rejected because the tip of your current branch is behind"**

You probably amended or rebased a pushed commit.

**If you're SURE no one else is working on the branch:**
```bash
git push --force-with-lease
```

---

## 10. I accidentally ran git reset --hard

**DON'T PANIC!** Commits are recoverable for ~30 days via reflog.

```bash
git reflog                    # Find your lost commit
git reset --hard <commit>     # Go back to it
```

**Example:**
```bash
$ git reflog
abc1234 HEAD@{0}: reset: moving to HEAD~3
def5678 HEAD@{1}: commit: My important work    # <- This one!

$ git reset --hard def5678    # Recovered!
```

---

## 11. I need to undo a pushed commit

**Safe way (creates new "undo" commit):**
```bash
git revert <commit-hash>
git push
```

**Revert multiple commits:**
```bash
git revert <oldest-commit>..<newest-commit>
```

**Revert a merge commit:**
```bash
git revert -m 1 <merge-commit-hash>
```

---

## 12. I'm in detached HEAD state

**What happened:** You checked out a commit or tag instead of a branch.

**If you made commits you want to keep:**
```bash
git branch my-new-branch      # Create branch at current position
git checkout my-new-branch    # Switch to it
```

**If you just want to go back to a branch:**
```bash
git checkout main             # Or whatever branch
```

---

## 13. I have too many messy commits

**Clean up before pushing with interactive rebase:**
```bash
git rebase -i HEAD~5          # Last 5 commits
```

**In the editor, you can:**
- `pick` - keep commit as-is
- `squash` (or `s`) - combine with previous commit
- `fixup` (or `f`) - combine, discard this message
- `reword` (or `r`) - change commit message
- `drop` (or `d`) - delete commit

**Example:**
```
pick abc1234 Add feature
squash def5678 Fix typo
squash 789abcd More fixes
pick 111222 Add tests
```

This combines the first 3 commits into one.

---

## 14. My local branch is behind remote

**Update with rebase (cleaner history):**
```bash
git fetch origin
git rebase origin/main
```

**Update with merge:**
```bash
git pull origin main
```

**If you have local changes you want to keep:**
```bash
git stash
git pull origin main
git stash pop
```

---

## 15. I staged files I didn't want to stage

**Unstage specific file:**
```bash
git reset HEAD <file>         # Old way
git restore --staged <file>   # Modern way
```

**Unstage everything:**
```bash
git reset HEAD
git restore --staged .
```

---

## Prevention Tips

1. **Use `.gitignore`** - Prevent committing unwanted files
2. **Review before commit** - `git diff --staged`
3. **Commit often** - Small commits are easier to undo
4. **Use branches** - Don't work directly on main
5. **Pull before push** - Stay updated with team
6. **Use `--force-with-lease`** - Safer than `--force`

---

## Quick Decision Tree

```
Need to undo something?
│
├── Commit not pushed yet?
│   ├── Keep changes? → git reset --soft HEAD~1
│   └── Discard changes? → git reset --hard HEAD~1
│
├── Commit already pushed?
│   ├── Safe undo (new commit)? → git revert <commit>
│   └── Must rewrite history? → git reset + git push --force-with-lease
│
├── Lost commits/branch?
│   └── git reflog → find commit → git reset or git branch
│
└── Merge conflict?
    ├── Want to resolve? → Edit files, git add, git commit
    └── Want to abort? → git merge --abort
```

---

*Remember: Git almost never truly loses data. Stay calm and check the reflog!*
