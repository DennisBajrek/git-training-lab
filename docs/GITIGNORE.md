# Understanding .gitignore 🙈

Not everything should be tracked by Git. The `.gitignore` file tells Git which files to ignore.

---

## Why Ignore Files?

Some files should **never** be committed:

| Type | Examples | Why Ignore |
|------|----------|------------|
| **Secrets** | `.env`, API keys, passwords | Security risk! |
| **Dependencies** | `node_modules/`, `venv/` | Huge, can be regenerated |
| **Build output** | `dist/`, `*.pyc`, `__pycache__/` | Generated from source |
| **IDE settings** | `.idea/`, `.vscode/` | Personal preference |
| **OS files** | `.DS_Store`, `Thumbs.db` | System junk |
| **Logs** | `*.log`, `logs/` | Not source code |

---

## How .gitignore Works

Create a file named `.gitignore` in your repo root:

```bash
touch .gitignore
```

Add patterns for files to ignore:

```gitignore
# This is a comment

# Ignore a specific file
secrets.txt

# Ignore all files with an extension
*.log
*.pyc

# Ignore a directory (and everything in it)
node_modules/
__pycache__/
dist/

# Ignore files in any directory with this name
**/temp/

# Ignore all .txt files in the docs folder
docs/*.txt

# But DON'T ignore this specific file (exception)
!important.log
```

---

## Common .gitignore Patterns

### Python Projects
```gitignore
# Byte-compiled files
__pycache__/
*.py[cod]
*$py.class

# Virtual environment
venv/
env/
.env/

# Environment variables (SECRETS!)
.env
.env.local

# IDE
.idea/
.vscode/
*.swp

# pytest
.pytest_cache/
.coverage
htmlcov/

# Jupyter
.ipynb_checkpoints/
```

### JavaScript/Node Projects
```gitignore
# Dependencies
node_modules/

# Build output
dist/
build/

# Environment variables
.env
.env.local
.env.*.local

# Logs
npm-debug.log*
yarn-error.log*

# IDE
.idea/
.vscode/
```

### General (Add to Any Project)
```gitignore
# OS files
.DS_Store
Thumbs.db

# Editor backups
*~
*.swp
*.swo

# Secrets - ALWAYS IGNORE THESE
.env
*.pem
*.key
secrets/
```

---

## ⚠️ Critical: Never Commit Secrets

**NEVER** commit files containing:
- API keys
- Passwords
- Database credentials
- Private keys
- Tokens

Even if you delete them later, they remain in Git history forever!

### What To Do Instead

1. Use environment variables:
   ```python
   import os
   api_key = os.environ.get('API_KEY')
   ```

2. Create a `.env` file (and add `.env` to `.gitignore`):
   ```
   API_KEY=your-secret-key
   DATABASE_URL=postgres://...
   ```

3. Provide a template for others:
   ```bash
   # Create .env.example (this IS committed)
   API_KEY=your-api-key-here
   DATABASE_URL=your-database-url-here
   ```

---

## Already Committed Something You Shouldn't Have?

If you accidentally committed a secret:

### If You Haven't Pushed Yet
```bash
# Remove from staging and history
git reset --soft HEAD~1
# Add the file to .gitignore
echo "secrets.txt" >> .gitignore
# Recommit without the file
git add .
git commit -m "Your message"
```

### If You Already Pushed
The secret is now public. You must:
1. **Rotate the secret immediately** (generate new API key, change password)
2. Remove it from future commits (add to .gitignore)
3. Consider using `git filter-branch` or BFG Repo-Cleaner to remove from history

**Assume the secret is compromised and rotate it!**

---

## Check What's Being Ignored

```bash
# See which files are ignored
git status --ignored

# Check if a specific file is ignored
git check-ignore -v filename.txt

# See what WOULD be committed (ignoring .gitignore)
git status --ignored --porcelain
```

---

## Global .gitignore

For files you ALWAYS want to ignore (OS junk, IDE settings):

```bash
# Create global gitignore
touch ~/.gitignore_global

# Tell Git to use it
git config --global core.excludesfile ~/.gitignore_global
```

Add to `~/.gitignore_global`:
```gitignore
# OS
.DS_Store
Thumbs.db

# Editors
.idea/
.vscode/
*.swp
*~
```

Now these are ignored in ALL your repos.

---

## .gitignore Templates

Don't write from scratch! Use templates:

### GitHub's Collection
https://github.com/github/gitignore

Has templates for:
- Python
- Node
- Java
- Go
- And many more...

### Generate Online
https://www.toptal.com/developers/gitignore

Select your tech stack → Get a complete .gitignore

### When Creating a Repo on GitHub
GitHub offers to add a .gitignore template when you create a new repo.

---

## Common Mistakes

### 1. Adding .gitignore After Committing Files

If files are already tracked, .gitignore won't help:

```bash
# Remove from Git (but keep local file)
git rm --cached filename.txt

# Or for a directory
git rm -r --cached node_modules/

# Then commit
git commit -m "Remove accidentally tracked files"
```

### 2. Forgetting the Slash for Directories

```gitignore
# This ignores a FILE named "logs"
logs

# This ignores a DIRECTORY named "logs"
logs/
```

### 3. Ignoring Files You Need

Using `*` too broadly:
```gitignore
# Bad - ignores ALL .json files
*.json

# Better - only ignore specific ones
package-lock.json
config.local.json
```

---

## Quick Reference

```gitignore
# File
secret.txt

# Extension
*.log

# Directory
node_modules/

# All matching directories
**/temp/

# Exception (don't ignore)
!important.txt

# Wildcard
*.py[cod]    # matches .pyc, .pyo, .pyd
```

---

## This Repo's .gitignore

Check out the [.gitignore](../.gitignore) in this training lab for a working example!

---

*Next: Learn how to recover from mistakes in [Git First Aid](GIT_FIRST_AID.md)*
