# Git Training Lab 🎓

Welcome to the Git Training Lab! This hands-on environment will teach you Git fundamentals through practical exercises. Take your time—this is about learning, not speed.

**Estimated time:** ~2 hours (but go at your own pace)

---

## 🎯 Learning Objectives

By the end of this lab, you will:

- Understand what Git is and why distributed version control matters
- Confidently use core Git commands in daily development
- Create and manage branches
- Handle merge conflicts without panic
- Collaborate with teammates using Git workflows
- Understand how to undo mistakes (we all make them!)

---

## 🚀 Quick Start (Do This First)

1. **Fork this repo** — Click the "Fork" button on GitHub (top right)
2. **Clone your fork:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/git-training-lab.git
   cd git-training-lab
   ```
3. **Set up Git** (if you haven't):
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```
4. **Install pytest:**
   ```bash
   pip install pytest
   ```
5. **Verify setup:**
   ```bash
   python run_tests.py
   ```
   You should see all exercises at 0/X — that's expected!
6. **Start with Exercise 1** in `exercises/solo/exercise_1.py`

---

## 📚 Before You Start

> **💡 New to Markdown files?** If these `.md` files look like messy plain text, see the [Viewing Markdown section in Setup](docs/SETUP.md#viewing-markdown-files) or just **read them on GitHub** where they render automatically!

**📖 Recommended reading order:**
1. [Setup Guide](docs/SETUP.md) — Git installation, authentication, configuration
2. [Git Guide](docs/GIT_GUIDE.md) — How Git works + fixing common mistakes
3. [Workflow Guide](docs/WORKFLOW.md) — Jira, Slack, and code review practices

**📋 Quick References:**
- [Git Cheat Sheet](docs/GIT_CHEATSHEET.md) — One-page command reference
- [Common Mistakes](docs/COMMON_MISTAKES.md) — How to fix Git mistakes
- [Visual Guide](docs/GIT_VISUAL_GUIDE.md) — ASCII diagrams for Git concepts

**🆘 Having issues?** Check the [Troubleshooting](docs/SETUP.md#troubleshooting) section.

### Prerequisites

- Python 3.8+ installed
- Git installed (`git --version` to check)
- A GitHub account
- A code editor (VS Code recommended)

### Setup

1. **Fork this repository** (click "Fork" button on GitHub)
2. **Clone your fork:**
   ```bash
   git clone https://github.com/RubyHawk/git-training-lab.git
   cd git-training-lab
   ```
3. **Verify setup:**
   ```bash
   python --version  # Should show 3.8+
   git status        # Should show "On branch main"
   ```

---

## 🏗️ Structure

```
git-training-lab/
├── exercises/
│   ├── solo/           # Part 1: Individual exercises (1-7)
│   └── collaborative/  # Part 2: Team exercises (8-9)
├── tests/              # Automated tests (run via GitHub Actions)
├── docs/               # Learning materials
└── .github/workflows/  # CI pipeline
```

---

## 📝 Part 1: Solo Exercises (Fundamentals 1-7)

Complete these individually. Each exercise has a Python file with TODOs and a corresponding Git task.

| Exercise | Git Focus | Coding Task | Difficulty |
|----------|-----------|-------------|------------|
| 1 | `clone`, `status`, `add`, `commit`, `push` | Reverse a string | ⭐ Easy |
| 2 | `log`, `diff`, `show` | FizzBuzz | ⭐ Easy |
| 3 | `branch`, `checkout`, `switch` | Find max in list | ⭐ Easy |
| 4 | `pull`, remote tracking | Count vowels | ⭐ Easy |
| 5 | `stash`, `stash pop` | Palindrome check | ⭐⭐ Medium |
| 6 | `reset`, `revert` | Two Sum | ⭐⭐ Medium |
| 7 | `checkout` (files), `restore` | Merge sorted arrays | ⭐⭐ Medium |

## 📝 Part 2: Advanced Solo Exercises (10-15)

These exercises cover advanced Git concepts that are essential in real-world workflows.

| Exercise | Git Focus | Coding Task | Difficulty |
|----------|-----------|-------------|------------|
| 10 | `cherry-pick` | Binary Search | ⭐⭐ Medium |
| 11 | `bisect` | Email Validation | ⭐⭐ Medium |
| 12 | `reflog` (recovery) | Flatten Nested List | ⭐⭐ Medium |
| 13 | `commit --amend`, `rebase -i` (squash) | Remove Duplicates | ⭐⭐ Medium |
| 14 | `blame`, `log -p` | Word Frequency | ⭐⭐ Medium |
| 15 | `tag` | Version Parser | ⭐⭐ Medium |

### How to Complete Solo Exercises

1. Navigate to the exercise file (e.g., `exercises/solo/exercise_1.py`)
2. Read the instructions in the file
3. Complete the Python TODO
4. Follow the Git instructions in each exercise
5. Push your changes
6. Check GitHub Actions to see if tests pass ✅

---

## 👥 Part 3: Collaborative Exercises (8-9)

Complete these with a partner or simulate teamwork using the pre-made branches.

| Exercise | Git Focus | Task | Difficulty |
|----------|-----------|------|------------|
| 8 | `merge`, conflict resolution | Group anagram checker | ⭐⭐ Medium |
| 9 | `rebase`, `fetch`, Pull Requests | Valid parentheses | ⭐⭐⭐ Harder |

### How to Complete Collaborative Exercises

These exercises simulate real team scenarios. You'll work with pre-existing branches that represent "teammate" work.

---

## ✅ Validation

Every time you push, GitHub Actions automatically runs tests:

1. Go to the "Actions" tab in your GitHub repo
2. Click on the latest workflow run
3. See which tests passed/failed
4. Green checkmark = success! 🎉

You can also run tests locally:
```bash
pip install pytest
python run_tests.py
```

---

## 🆘 Getting Help

- **Stuck on Git?** Check the [Git Guide](docs/GIT_GUIDE.md) or [Common Mistakes](docs/COMMON_MISTAKES.md)
- **Stuck on code?** The coding is intentionally simple—focus on Git
- **Something broken?** Check GitHub Actions output for hints
- **Still stuck?** Ask a teammate or mentor

### Useful Commands Reference

```bash
# Check what's happening
git status
git log --oneline

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Discard all local changes (careful!)
git checkout -- .

# See what changed
git diff
git diff --staged
```

---

## 🏁 Completion Checklist

### Fundamentals (1-7)
- [ ] Exercise 1: First commit and push
- [ ] Exercise 2: Explored history
- [ ] Exercise 3: Branching basics
- [ ] Exercise 4: Working with remotes
- [ ] Exercise 5: Used stash
- [ ] Exercise 6: Reset and revert
- [ ] Exercise 7: Restored files

### Collaborative (8-9)
- [ ] Exercise 8: Resolved merge conflict
- [ ] Exercise 9: Rebased and created PR

### Advanced (10-15)
- [ ] Exercise 10: Cherry-picked commits
- [ ] Exercise 11: Used bisect to find bugs
- [ ] Exercise 12: Recovered with reflog
- [ ] Exercise 13: Amended and squashed commits
- [ ] Exercise 14: Investigated with blame/log
- [ ] Exercise 15: Created tags for releases

**All tests passing? Congratulations!** You now have comprehensive Git skills for any development team.

---

## 📖 Additional Resources

- [Pro Git Book (free)](https://git-scm.com/book/en/v2)
- [GitHub Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Oh Shit, Git!?!](https://ohshitgit.com/) — Fixing common mistakes
- [Learn Git Branching (interactive)](https://learngitbranching.js.org/)

---

*Created for new engineer onboarding. Happy learning!*
