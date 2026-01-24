# How to View & Edit Markdown Files 📄

The documentation in this training lab uses **Markdown** (`.md` files). Here's how to read them properly depending on your setup.

---

## What is Markdown?

Markdown is a simple text format that can be rendered as nice-looking documents. This file you're reading is Markdown!

Raw Markdown looks like this:
```
# This is a heading
**This is bold**
- This is a bullet point
```

When rendered, it looks like formatted text with headings, bold, and bullets.

---

## Option 1: View on GitHub (Easiest)

GitHub automatically renders Markdown files beautifully.

1. Go to the repository on GitHub
2. Click on any `.md` file
3. It displays formatted automatically ✅

**This is the recommended way to read the guides before starting.**

---

## Option 2: VS Code (Recommended IDE)

VS Code has excellent built-in Markdown support.

### To Preview a Markdown File:

1. Open the `.md` file
2. Use one of these methods:
   - Press `Cmd + Shift + V` (Mac) or `Ctrl + Shift + V` (Windows/Linux)
   - Or click the "Open Preview" icon in the top-right corner (looks like a split window with a magnifying glass)
   - Or right-click the file tab → "Open Preview"

### Side-by-Side View (Edit + Preview):

- Press `Cmd + K V` (Mac) or `Ctrl + K V` (Windows/Linux)
- This shows the raw file on the left, rendered preview on the right

### Helpful VS Code Extensions:

- **Markdown All in One** — Adds shortcuts and table of contents
- **Markdown Preview Enhanced** — Better preview with more features

To install: `Cmd/Ctrl + Shift + X` → Search → Install

---

## Option 3: JetBrains IDEs (IntelliJ, PyCharm, WebStorm)

### To Preview:

1. Open the `.md` file
2. Look for the split-view icons in the top-right of the editor:
   - 📝 Editor only
   - 📝|👁️ Split (editor + preview)
   - 👁️ Preview only

3. Or: Right-click the file → "Open in" → "Preview"

### Enable Markdown Plugin (if not working):

1. Go to `Preferences/Settings` → `Plugins`
2. Search for "Markdown"
3. Enable the built-in Markdown plugin
4. Restart IDE

---

## Option 4: Terminal/Command Line

If you're SSH'd into a server or prefer the terminal:

### Basic Reading with `cat` or `less`:
```bash
# Shows raw markdown (not rendered)
cat README.md

# Scrollable view
less README.md
```

### Rendered Markdown in Terminal:

Install `glow` (a terminal Markdown renderer):
```bash
# Mac
brew install glow

# Ubuntu/Debian
sudo apt install glow

# Then use it
glow README.md
```

Or use `bat` (like `cat` but with syntax highlighting):
```bash
# Mac
brew install bat

# Ubuntu/Debian
sudo apt install bat

# Usage
bat README.md
```

---

## Option 5: Other Text Editors

### Sublime Text
- Install "MarkdownPreview" package via Package Control
- `Cmd/Ctrl + Shift + P` → "Markdown Preview: Preview in Browser"

### Vim/Neovim
- Install `vim-markdown` plugin
- Or use `:!glow %` if glow is installed

### Notepad++ (Windows)
- Install "Markdown Viewer++" plugin
- Plugins → Markdown Viewer++ → Open Preview

---

## Option 6: Browser-Based Viewers

If all else fails, use an online viewer:

1. Copy the Markdown content
2. Paste into one of these:
   - [StackEdit](https://stackedit.io/)
   - [Dillinger](https://dillinger.io/)
   - [Markdown Live Preview](https://markdownlivepreview.com/)

---

## Quick Reference

| Your Setup | How to View Markdown |
|------------|---------------------|
| GitHub | Just click the file |
| VS Code | `Cmd/Ctrl + Shift + V` |
| PyCharm/IntelliJ | Click split-view icon |
| Terminal | Install `glow` → `glow file.md` |
| Any browser | Use online viewer |

---

## Still Stuck?

If you can't get Markdown to render nicely, you can still read the raw files — they're written to be readable as plain text too. The `#` symbols are headings, `**text**` is bold, and `-` items are bullets.

Or just **read the docs on GitHub first** before cloning the repo!

---

*Now head back to the [README](../README.md) to get started with the exercises.*
