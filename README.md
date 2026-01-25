# Git Training Lab 🎓

Welcome to the Git Training Lab! This hands-on environment will teach you Git fundamentals through practical exercises. Take your time—this is about learning, not speed.

**Estimated time:** ~5-6 hours total (but go at your own pace)

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

## 📖 Key Terms (Glossary)

New to Git? Here's what the jargon means:

| Term | What It Means |
|------|---------------|
| **Git** | Software that tracks changes to your code over time |
| **GitHub** | A website that hosts Git repositories online |
| **Repository (repo)** | A folder containing your project + its entire history |
| **Fork** | Your personal copy of someone else's repo on GitHub |
| **Clone** | Download a repo from GitHub to your computer |
| **Commit** | A saved snapshot of your changes (like a save point) |
| **Branch** | A parallel version of your code for working on features |
| **Main** | The primary branch (the "official" version) |
| **Origin** | The default name for the remote server (GitHub) |
| **Push** | Upload your commits to GitHub |
| **Pull** | Download changes from GitHub to your computer |
| **Merge** | Combine changes from one branch into another |

---

## 🚀 Quick Start (Do This First)

**Prerequisites:** Python 3.8+, Git, a GitHub account, VS Code (recommended)

> **💡 New to the terminal?** The terminal (also called command line) is where you type commands. On Mac: open "Terminal". On Windows: open "Git Bash" (installed with Git) or "Command Prompt". The `$` symbol means "type this command" — don't type the `$` itself!

1. **Fork this repo** — Click the "Fork" button on GitHub (top right)
   - This creates YOUR personal copy on GitHub
   - You'll push your work here, not the original repo
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

---

## 🏗️ Structure

```
git-training-lab/
├── exercises/
│   ├── solo/           # Exercises 1-7 (fundamentals) and 10-15 (advanced)
│   └── collaborative/  # Exercises 8-9 (teamwork simulation)
├── tests/              # Automated tests (run via GitHub Actions)
├── docs/               # Learning materials and guides
├── branches/           # Reference files for special branches (instructor use)
└── .github/workflows/  # CI pipeline
```

---

## 📝 Part 1: Fundamentals (Exercises 1-7)

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

---

## 👥 Part 2: Collaborative (Exercises 8-9)

These exercises simulate real team scenarios. You'll work with **pre-existing branches** that represent "teammate" work.

| Exercise | Git Focus | Task | Difficulty |
|----------|-----------|------|------------|
| 8 | `merge`, conflict resolution | Group anagram checker | ⭐⭐ Medium |
| 9 | `rebase`, `fetch`, Pull Requests | Valid parentheses | ⭐⭐⭐ Harder |

> **⚠️ Important:** These exercises use special branches that exist on GitHub:
> - `teammate/exercise-8` — Contains a different implementation for Exercise 8
> - `main-updated` — Simulates "main getting updates" for Exercise 9
>
> You'll need to **fetch** these branches before you can use them. The exercise instructions will guide you through this.

---

## 📝 Part 3: Advanced (Exercises 10-15)

These exercises cover advanced Git concepts that are essential in real-world workflows.

| Exercise | Git Focus | Coding Task | Difficulty |
|----------|-----------|-------------|------------|
| 10 | `cherry-pick` | Binary Search | ⭐⭐ Medium |
| 11 | `bisect` | Email Validation | ⭐⭐ Medium |
| 12 | `reflog` (recovery) | Flatten Nested List | ⭐⭐ Medium |
| 13 | `commit --amend`, `rebase -i` (squash) | Remove Duplicates | ⭐⭐ Medium |
| 14 | `blame`, `log -p` | Word Frequency | ⭐⭐ Medium |
| 15 | `tag` | Version Parser | ⭐⭐ Medium |

---

### How to Complete Each Exercise

1. Navigate to the exercise file (e.g., `exercises/solo/exercise_1.py`)
2. **Read the entire file** — it contains both the coding task AND Git instructions
3. Complete the Python TODO
4. Follow the Git instructions step-by-step
5. Push your changes
6. Check GitHub Actions to see if tests pass ✅

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
