# Setup Guide 🛠️

Everything you need to get Git working on your machine.

---

## 1. Install Git

**Windows:**
- Download from [git-scm.com](https://git-scm.com/download/win)
- Run installer, use default options
- Restart your terminal

**Mac:**
```bash
xcode-select --install
```

**Linux:**
```bash
sudo apt install git  # Ubuntu/Debian
sudo dnf install git  # Fedora
```

**Verify installation:**
```bash
git --version
```

---

## 2. Configure Your Identity

Git needs to know who you are (attached to every commit):

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

**Use the same email as your GitHub account** — this links commits to your profile.

### Recommended Settings

```bash
# Set default branch to 'main'
git config --global init.defaultBranch main

# Set VS Code as your editor
git config --global core.editor "code --wait"

# Enable colors
git config --global color.ui auto

# Helpful aliases
git config --global alias.st status
git config --global alias.lg "log --oneline --graph --all"
```

### Verify Settings

```bash
git config --global --list
```

---

## 3. GitHub Authentication

You need to authenticate to push code to GitHub.

### Option A: HTTPS with Personal Access Token (Easier)

1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
   - Direct link: https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Name it (e.g., "My Laptop"), set expiration, check `repo` scope
4. Click "Generate token"
5. **Copy the token immediately** — you won't see it again!

When you push, use:
- Username: your GitHub username
- Password: paste your token (not your GitHub password)

**Save credentials so you don't re-enter:**
```bash
# Windows
git config --global credential.helper manager

# Mac
git config --global credential.helper osxkeychain

# Linux
git config --global credential.helper 'cache --timeout=28800'
```

### Option B: SSH Keys (More Secure)

```bash
# Generate key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Start SSH agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Copy public key
# Mac:
pbcopy < ~/.ssh/id_ed25519.pub
# Windows (Git Bash):
clip < ~/.ssh/id_ed25519.pub
# Linux:
cat ~/.ssh/id_ed25519.pub  # then copy manually
```

Then add to GitHub:
1. Go to GitHub → Settings → SSH and GPG keys
2. Click "New SSH key"
3. Paste your public key
4. Click "Add SSH key"

**Test it:**
```bash
ssh -T git@github.com
```

---

## 4. Understanding .gitignore

Some files should **never** be committed:

| Type | Examples | Why |
|------|----------|-----|
| Secrets | `.env`, API keys | Security risk! |
| Dependencies | `node_modules/`, `venv/` | Can be regenerated |
| Build output | `dist/`, `*.pyc` | Generated from source |
| IDE settings | `.idea/`, `.vscode/` | Personal preference |

Create a `.gitignore` file in your repo:

```gitignore
# Environment
.env
venv/

# Python
__pycache__/
*.pyc

# IDE
.idea/
.vscode/

# OS
.DS_Store
Thumbs.db
```

### ⚠️ Never Commit Secrets

If you accidentally commit a password or API key:
1. **Rotate the secret immediately** (generate a new one)
2. Add the file to `.gitignore`
3. The secret is compromised — assume it's been seen

---

## Troubleshooting

### "python is not recognized"

Python isn't in your PATH.

**Windows fix:**
1. Reinstall Python from [python.org](https://python.org)
2. ✅ Check "Add Python to PATH" during installation
3. Restart terminal

Or try `python3` instead of `python`.

### "git is not recognized"

Git isn't in your PATH.

**Windows fix:**
1. Reinstall Git from [git-scm.com](https://git-scm.com)
2. Restart terminal

### "Please tell me who you are"

Run:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### "Permission denied (publickey)"

SSH key issue. Either:
- Use HTTPS instead (Option A above)
- Or fix SSH: `ssh-add ~/.ssh/id_ed25519`

### "Authentication failed" when pushing

For HTTPS: You might be using your password instead of a Personal Access Token. Generate a new token.

### "fatal: not a git repository"

You're not inside a Git repo. Either:
- `cd` into your project folder
- Or run `git init` to create a new repo

### "Updates were rejected" / "failed to push"

Someone else pushed changes. Pull first:
```bash
git pull origin main
# Then push again
git push origin main
```

### "CRLF will be replaced by LF" warning

Line ending differences (Windows vs Mac/Linux). Fix:
```bash
git config --global core.autocrlf true   # Windows
git config --global core.autocrlf input  # Mac/Linux
```

### VS Code not using correct Git account

Clear cached credentials:
1. Open "Credential Manager" (Windows search)
2. Click "Windows Credentials"
3. Remove entries with `github`
4. Push again — it will prompt for login

---

## Quick Reference

```bash
# Check Git version
git --version

# Check config
git config --global --list

# Check current repo status
git status

# Check remote URL
git remote -v

# Test GitHub SSH connection
ssh -T git@github.com
```

---

---

## Viewing Markdown Files

The documentation uses **Markdown** (`.md` files). Here's how to view them:

### On GitHub (Easiest)
GitHub automatically renders Markdown beautifully. Just click any `.md` file.

### In VS Code
- **Preview:** `Cmd/Ctrl + Shift + V`
- **Side-by-side:** `Cmd/Ctrl + K V`

### In JetBrains IDEs (PyCharm, IntelliJ)
Look for split-view icons in the top-right of the editor.

### In Terminal
Install `glow` for rendered Markdown:
```bash
brew install glow  # Mac
sudo apt install glow  # Ubuntu
glow README.md
```

### Can't Render?
The docs are written to be readable as plain text too. `#` = heading, `**text**` = bold, `-` = bullet.

---

*Next: Read the [Git Guide](GIT_GUIDE.md) to understand how Git works.*
