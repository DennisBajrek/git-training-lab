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

## 📚 Before You Start

> **💡 New to Markdown files?** If these `.md` files look like messy plain text, see [How to View Markdown](docs/VIEWING_MARKDOWN.md) for setup instructions. Or just **read them on GitHub** where they render automatically!

**⚙️ First-time setup (do this first!):**
- [Authentication Setup](docs/AUTH_SETUP.md) — SSH keys or HTTPS tokens for GitHub
- [Git Config Setup](docs/GITCONFIG_SETUP.md) — Set your name, email, and useful defaults

**📖 Read these before starting:**
- [Git Concepts Guide](docs/CONCEPTS.md) — How Git works under the hood
- [Understanding .gitignore](docs/GITIGNORE.md) — What NOT to commit
- [Jira & Slack Workflow](docs/JIRA_SLACK_WORKFLOW.md) — How these tools fit into your daily work

**🚑 Keep these handy:**
- [Git First Aid](docs/GIT_FIRST_AID.md) — Fixing common mistakes
- [PR Review Etiquette](docs/PR_REVIEW_ETIQUETTE.md) — How to give and receive code review

### Prerequisites

- Python 3.8+ installed
- Git installed (`git --version` to check)
- A GitHub account
- A code editor (VS Code recommended)

### Setup

1. **Fork this repository** (click "Fork" button on GitHub)
2. **Clone your fork:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/git-training-lab.git
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

## 📝 Part 1: Solo Exercises (70%)

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

### How to Complete Solo Exercises

1. Navigate to the exercise file (e.g., `exercises/solo/exercise_1.py`)
2. Read the instructions in the file
3. Complete the Python TODO
4. Follow the Git instructions in each exercise
5. Push your changes
6. Check GitHub Actions to see if tests pass ✅

---

## 👥 Part 2: Collaborative Exercises (30%)

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
pytest tests/ -v
```

---

## 🆘 Getting Help

- **Stuck on Git?** Check the [Git Concepts Guide](docs/CONCEPTS.md)
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

- [ ] Exercise 1: First commit and push
- [ ] Exercise 2: Explored history
- [ ] Exercise 3: Branching basics
- [ ] Exercise 4: Working with remotes
- [ ] Exercise 5: Used stash
- [ ] Exercise 6: Reset and revert
- [ ] Exercise 7: Restored files
- [ ] Exercise 8: Resolved merge conflict
- [ ] Exercise 9: Rebased and created PR

**All tests passing? Congratulations! 🎉** You now have the Git fundamentals to work in any development team.

---

## 📖 Additional Resources

**In this repo:**
- [Authentication Setup](docs/AUTH_SETUP.md) — SSH keys or HTTPS tokens
- [Git Config Setup](docs/GITCONFIG_SETUP.md) — Configure Git properly
- [Understanding .gitignore](docs/GITIGNORE.md) — What NOT to commit
- [Git Concepts](docs/CONCEPTS.md) — How Git works
- [Git First Aid](docs/GIT_FIRST_AID.md) — Fixing mistakes
- [PR Review Etiquette](docs/PR_REVIEW_ETIQUETTE.md) — Code review best practices
- [Jira & Slack Workflow](docs/JIRA_SLACK_WORKFLOW.md) — Daily tools

**External:**
- [Pro Git Book (free)](https://git-scm.com/book/en/v2)
- [GitHub Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Oh Shit, Git!?!](https://ohshitgit.com/) — Fixing common mistakes
- [Learn Git Branching (interactive)](https://learngitbranching.js.org/)

---

*Created for new engineer onboarding. Happy learning!*
