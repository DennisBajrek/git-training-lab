# Git Authentication Setup 🔐

Before you can push code to GitHub, you need to authenticate. This guide covers both methods.

---

## Quick Decision: SSH vs HTTPS

| Method | Best For | Setup Time |
|--------|----------|------------|
| **HTTPS** | Quick start, less config | 2 minutes |
| **SSH** | Long-term, no repeated logins | 10 minutes |

**Recommendation:** Start with HTTPS, switch to SSH later if you want.

---

## Option 1: HTTPS (Easier)

HTTPS uses your GitHub username + a Personal Access Token (PAT) instead of your password.

### Step 1: Create a Personal Access Token

1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
   - Direct link: https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Give it a name (e.g., "My Laptop")
4. Set expiration (90 days is reasonable)
5. Select scopes:
   - ✅ `repo` (full control of repositories)
6. Click "Generate token"
7. **COPY THE TOKEN NOW** — you won't see it again!

### Step 2: Use the Token

When you `git push` for the first time, you'll be prompted:

```
Username: your-github-username
Password: <paste your token here, NOT your GitHub password>
```

### Step 3: Save Token (So You Don't Re-enter It)

**Mac:**
```bash
git config --global credential.helper osxkeychain
```

**Windows:**
```bash
git config --global credential.helper manager
```

**Linux:**
```bash
# Cache for 8 hours (28800 seconds)
git config --global credential.helper 'cache --timeout=28800'

# Or store permanently (less secure)
git config --global credential.helper store
```

After this, Git remembers your credentials.

---

## Option 2: SSH (More Secure, No Repeated Logins)

SSH uses a key pair: a private key (stays on your computer) and a public key (uploaded to GitHub).

### Step 1: Check for Existing SSH Keys

```bash
ls -la ~/.ssh
```

If you see `id_ed25519.pub` or `id_rsa.pub`, you might already have keys.

### Step 2: Generate a New SSH Key

```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
```

When prompted:
- **File location:** Press Enter for default
- **Passphrase:** Optional but recommended (extra security)

### Step 3: Start the SSH Agent

**Mac/Linux:**
```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

**Mac (add to Keychain so it persists):**
```bash
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```

**Windows (Git Bash):**
```bash
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_ed25519
```

### Step 4: Add SSH Key to GitHub

1. Copy your public key:
   ```bash
   # Mac
   pbcopy < ~/.ssh/id_ed25519.pub
   
   # Windows (Git Bash)
   clip < ~/.ssh/id_ed25519.pub
   
   # Linux
   cat ~/.ssh/id_ed25519.pub
   # Then manually copy the output
   ```

2. Go to GitHub → Settings → SSH and GPG keys
   - Direct link: https://github.com/settings/keys
3. Click "New SSH key"
4. Title: "My Laptop" (or something descriptive)
5. Paste your public key
6. Click "Add SSH key"

### Step 5: Test the Connection

```bash
ssh -T git@github.com
```

You should see:
```
Hi username! You've successfully authenticated...
```

### Step 6: Clone Using SSH

When cloning, use the SSH URL (not HTTPS):
```bash
# SSH (use this)
git clone git@github.com:username/repo.git

# HTTPS (not this)
git clone https://github.com/username/repo.git
```

---

## Switching a Repo from HTTPS to SSH

If you already cloned with HTTPS:

```bash
# Check current remote
git remote -v

# Change to SSH
git remote set-url origin git@github.com:username/repo.git

# Verify
git remote -v
```

---

## Common Authentication Errors

### "Permission denied (publickey)"
- Your SSH key isn't set up correctly
- Run `ssh-add -l` to check if your key is loaded
- Make sure you added the public key to GitHub

### "Authentication failed"
- For HTTPS: You might be using your password instead of a token
- Generate a new Personal Access Token

### "remote: Repository not found"
- Check you have access to the repo
- Check for typos in the URL
- Make sure you're using the right protocol (SSH vs HTTPS)

### "Please tell me who you are"
- You haven't set up your Git identity yet
- See [GITCONFIG_SETUP.md](GITCONFIG_SETUP.md)

---

## Quick Reference

```bash
# Check how you cloned (SSH or HTTPS)
git remote -v

# SSH URL format
git@github.com:username/repo.git

# HTTPS URL format  
https://github.com/username/repo.git

# Test SSH connection
ssh -T git@github.com

# Check loaded SSH keys
ssh-add -l
```

---

*Next: Set up your [Git identity](GITCONFIG_SETUP.md)*
