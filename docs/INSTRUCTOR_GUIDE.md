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

### 3. Create Teammate Branches

```bash
# Branch for Exercise 8 (merge conflict)
git checkout -b teammate/exercise-8
cp branches/teammate-exercise-8.py exercises/collaborative/exercise_8.py
git add exercises/collaborative/exercise_8.py
git commit -m "Teammate implementation of group_anagrams"
git push origin teammate/exercise-8
git checkout main

# Branch for Exercise 9 (rebase)
git checkout -b main-updated
mkdir -p utils
cp branches/main-updated-content.py utils/changelog.py
git add utils/
git commit -m "Add changelog and utility functions"
git push origin main-updated
git checkout main
```

### 4. Have Engineers Fork

Each engineer forks the repo to their own GitHub account, then clones their fork.

---

## Documentation Structure

The docs are consolidated into 3 main guides:

| File | Contents |
|------|----------|
| `SETUP.md` | Git install, config, auth, troubleshooting |
| `GIT_GUIDE.md` | How Git works + fixing mistakes |
| `WORKFLOW.md` | Jira, Slack, code review practices |

Plus:
- `SOLUTIONS.md` — Answer key (spoilers!)
- `VIEWING_MARKDOWN.md` — Help for viewing .md files

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

| Exercise | Git Skill | Code Works |
|----------|-----------|------------|
| 1 | add, commit, push | ☐ |
| 2 | log, diff, show | ☐ |
| 3 | branch, checkout, merge | ☐ |
| 4 | remote, pull, fetch | ☐ |
| 5 | stash | ☐ |
| 6 | reset, revert | ☐ |
| 7 | restore, checkout files | ☐ |
| 8 | merge conflicts | ☐ |
| 9 | rebase, PR | ☐ |

---

Happy teaching! 🎓
