# Git Configuration Setup ⚙️

Before your first commit, Git needs to know who you are. This takes 2 minutes.

---

## Required: Set Your Identity

Git attaches your name and email to every commit. Set this up **once** per computer:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

**Use the same email as your GitHub account** — this links commits to your profile.

### Verify Your Settings

```bash
git config --global user.name
git config --global user.email
```

---

## Recommended Settings

These make Git easier to use:

```bash
# Set default branch name to 'main' (modern standard)
git config --global init.defaultBranch main

# Set VS Code as your default editor (for commit messages, rebase, etc.)
git config --global core.editor "code --wait"

# Or use other editors:
# git config --global core.editor "vim"
# git config --global core.editor "nano"
# git config --global core.editor "notepad"   # Windows

# Enable colored output
git config --global color.ui auto

# Set pull behavior to merge (avoids surprises)
git config --global pull.rebase false
```

---

## Useful Aliases

Aliases let you create shortcuts for common commands:

```bash
# Short status
git config --global alias.st status

# Short commit
git config --global alias.cm commit

# Pretty log
git config --global alias.lg "log --oneline --graph --all"

# See last commit
git config --global alias.last "log -1 HEAD"

# Undo last commit (keep changes)
git config --global alias.undo "reset --soft HEAD~1"
```

Now you can use:
```bash
git st        # instead of git status
git lg        # pretty branch graph
git undo      # undo last commit
```

---

## View All Settings

```bash
# See all global settings
git config --global --list

# See where settings come from
git config --list --show-origin
```

---

## Per-Repository Settings

Sometimes you want different settings for work vs personal projects:

```bash
# Inside a specific repo (omit --global)
cd ~/work/company-project
git config user.email "your.name@company.com"
```

This overrides global settings for just that repo.

---

## The .gitconfig File

All global settings are stored in `~/.gitconfig`. You can edit it directly:

```bash
# Open in your editor
code ~/.gitconfig    # VS Code
vim ~/.gitconfig     # Vim
nano ~/.gitconfig    # Nano
```

Example `.gitconfig`:
```ini
[user]
    name = Your Name
    email = your.email@example.com

[init]
    defaultBranch = main

[core]
    editor = code --wait

[color]
    ui = auto

[alias]
    st = status
    cm = commit
    lg = log --oneline --graph --all
    undo = reset --soft HEAD~1

[pull]
    rebase = false
```

---

## "Please tell me who you are" Error

If you see this error:
```
*** Please tell me who you are.

Run
  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"
```

Just run those commands with your info:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Then retry your commit.

---

## Quick Setup Script

Run all recommended settings at once:

```bash
# Replace with your info
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Recommended settings
git config --global init.defaultBranch main
git config --global core.editor "code --wait"
git config --global color.ui auto
git config --global pull.rebase false

# Handy aliases
git config --global alias.st status
git config --global alias.lg "log --oneline --graph --all"
git config --global alias.undo "reset --soft HEAD~1"

# Verify
echo "Settings configured:"
git config --global --list
```

---

*Next: Learn about [.gitignore](GITIGNORE.md)*
