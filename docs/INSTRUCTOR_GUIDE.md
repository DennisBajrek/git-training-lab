# Instructor / Setup Guide 📋

How to set up and manage the Git Training Lab.

---

## Quick Setup for New Cohort

### 1. Create GitHub Repository

Create a new repo or use an existing one.

### 2. Push Training Lab

```bash
git init
git add .
git commit -m "Initial commit: Git Training Lab"
git remote add origin https://github.com/YOUR-ORG/git-training-lab.git
git push -u origin main
```

### 3. Create Special Branches

The lab requires two special branches for exercises 8 and 9:

```bash
# Branch for Exercise 8 (merge conflict)
# This branch has a DIFFERENT implementation that conflicts with student solutions
git checkout -b teammate/exercise-8 main
# Edit exercises/collaborative/exercise_8.py with alternate implementation
# (Use Counter-based approach instead of sorting)
git add exercises/collaborative/exercise_8.py
git commit -m "Teammate implementation of group_anagrams"
git push origin teammate/exercise-8
git checkout main

# Branch for Exercise 9 (rebase practice)
# This branch simulates "main getting updates" while student works
git checkout -b main-updated main
echo "# Changelog" > CHANGELOG.md
git add CHANGELOG.md
git commit -m "Add CHANGELOG.md"
# Add another small commit
git add README.md  # (after small edit)
git commit -m "Update README"
git push origin main-updated
git checkout main
```

**Important:** These branches should:
- `teammate/exercise-8`: Have the SAME base files as main, but with a different `group_anagrams` implementation
- `main-updated`: Be a few commits AHEAD of main with non-conflicting changes

### 4. Have Engineers Fork

Each engineer forks the repo to their own GitHub account, then clones their fork.

---

## Documentation Structure

| File | Contents |
|------|----------|
| `SETUP.md` | Git install, config, auth, troubleshooting, viewing markdown |
| `GIT_GUIDE.md` | How Git works + fixing mistakes |
| `WORKFLOW.md` | Jira, Slack, code review practices |
| `GIT_CHEATSHEET.md` | Quick command reference |
| `COMMON_MISTAKES.md` | 15 common mistakes and fixes |
| `GIT_VISUAL_GUIDE.md` | ASCII diagrams for visual learners |
| `SOLUTIONS.md` | Answer key for all 15 exercises (spoilers!)

---

## Solutions

Solutions are in `docs/SOLUTIONS.md`. Engineers should try themselves first!

Alternatively, create a `solutions` branch:

```bash
git checkout -b solutions
# Implement all exercises
git push origin solutions
```

---

## Resetting Between Cohorts

```bash
# Tag initial state (do this once after setup)
git tag initial-state
git push origin initial-state

# Reset for new cohort
git checkout main
git reset --hard initial-state
git push --force origin main
```

---

## Common Issues

### "Tests fail but code is correct"
- Check function names match exactly
- Check return types (`None` vs empty list)

### "Can't push"
- They should push to their fork, not the original
- Check: `git remote -v`

### "Merge conflict is confusing"
- Walk through the conflict markers with them
- Both versions are shown between `<<<<<<<` and `>>>>>>>`

### "Accidentally committed to main"
```bash
git branch feature/my-work
git checkout main
git reset --hard origin/main
git checkout feature/my-work
```

---

## Assessment Checklist

### Fundamentals (Exercises 1-7)

| Exercise | Git Skill | Code Works | Est. Time |
|----------|-----------|------------|-----------|
| 1 | add, commit, push | ☐ | 15 min |
| 2 | log, diff, show | ☐ | 15 min |
| 3 | branch, checkout, merge | ☐ | 20 min |
| 4 | remote, pull, fetch | ☐ | 15 min |
| 5 | stash | ☐ | 20 min |
| 6 | reset, revert | ☐ | 25 min |
| 7 | restore, checkout files | ☐ | 15 min |

### Collaborative (Exercises 8-9)

| Exercise | Git Skill | Code Works | Est. Time |
|----------|-----------|------------|-----------|
| 8 | merge conflicts | ☐ | 30 min |
| 9 | rebase, PR | ☐ | 30 min |

### Advanced (Exercises 10-15)

| Exercise | Git Skill | Code Works | Est. Time |
|----------|-----------|------------|-----------|
| 10 | cherry-pick | ☐ | 25 min |
| 11 | bisect | ☐ | 25 min |
| 12 | reflog | ☐ | 20 min |
| 13 | amend, squash | ☐ | 30 min |
| 14 | blame, log -p | ☐ | 20 min |
| 15 | tag | ☐ | 20 min |

**Total estimated time:** ~5-6 hours (go at your own pace)

---

## Common Student Mistakes & How to Help

### Exercise 1-4 (Basics)

| Mistake | Symptom | Solution |
|---------|---------|----------|
| Not staging files | "nothing to commit" | `git add <file>` before commit |
| Wrong remote URL | Push fails with 403/404 | `git remote set-url origin <correct-url>` |
| Committed to wrong branch | Changes on main instead of feature | See "Accidentally committed to main" below |
| Forgetting to pull | "rejected...non-fast-forward" | `git pull --rebase origin main` |

### Exercise 5-7 (Intermediate)

| Mistake | Symptom | Solution |
|---------|---------|----------|
| Lost stash | Can't find stashed work | `git stash list`, check `git reflog` |
| reset --hard panic | "I lost my work!" | `git reflog` to find lost commits |
| Confusing reset modes | Wrong result after reset | Explain: --soft (staged), none (unstaged), --hard (gone) |

### Exercise 8-9 (Collaborative)

| Mistake | Symptom | Solution |
|---------|---------|----------|
| Conflict markers left in | Tests fail, weird output | Search file for `<<<<<<<` markers |
| Rebase on wrong branch | Complex merge issues | `git rebase --abort`, start over |
| Forgot to fetch | Can't find remote branch | `git fetch origin` first |

### Exercise 10-15 (Advanced)

| Mistake | Symptom | Solution |
|---------|---------|----------|
| Cherry-pick conflicts | Stuck in conflict state | `git cherry-pick --abort` or resolve manually |
| Bisect confusion | Lost track of good/bad | `git bisect log` to see history, `git bisect reset` to restart |
| Amending pushed commits | Force push needed | Explain dangers, use `--force-with-lease` |
| Can't find in reflog | Entry expired | Reflog keeps entries ~30 days, may be gone |

---

## Discussion Questions for Each Section

### After Fundamentals (1-7)
- Why do we stage files before committing?
- When would you use `reset --soft` vs `reset --hard`?
- What's the difference between `checkout` and `switch`?

### After Collaborative (8-9)
- Why is rebasing considered "rewriting history"?
- When should you merge vs rebase?
- What makes a good PR description?

### After Advanced (10-15)
- When is cherry-pick better than merge?
- How would you use bisect in a real debugging scenario?
- Why is the reflog called Git's "safety net"?

---

Happy teaching!
