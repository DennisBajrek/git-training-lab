# Jira & Slack: Your Daily Workflow Tools 🛠️

As a developer, you'll use Git for code — but you'll also need tools for **communication** (Slack) and **task tracking** (Jira). Here's a quick overview.

---

## The Typical Stack

| Tool | Purpose | You'll Use It For |
|------|---------|-------------------|
| **Slack** | Real-time communication | Quick questions, team updates, alerts |
| **Jira** | Project/issue tracking | Tickets, sprints, tracking what you're working on |
| **Git/GitHub** | Code versioning | Commits, branches, pull requests |

These three tools work together and integrate with each other.

---

## Jira Basics

### What is Jira?

Jira is where your team tracks work. Every task becomes a "ticket" (also called an "issue").

### Key Concepts

- **Ticket/Issue**: A single unit of work (bug fix, feature, task)
- **Project**: A collection of related tickets (e.g., "Backend API")
- **Sprint**: A time-boxed period (usually 2 weeks) where you complete a set of tickets
- **Board**: Visual view of tickets (To Do → In Progress → Done)

### Ticket Anatomy

```
┌─────────────────────────────────────────────────┐
│ PROJ-123: Add user authentication               │
├─────────────────────────────────────────────────┤
│ Status: In Progress                             │
│ Assignee: You                                   │
│ Sprint: Sprint 5                                │
│ Story Points: 3                                 │
│                                                 │
│ Description:                                    │
│ Implement login/logout functionality using      │
│ JWT tokens. See design doc for details.         │
│                                                 │
│ Acceptance Criteria:                            │
│ - User can log in with email/password           │
│ - User can log out                              │
│ - Session persists across page refresh          │
└─────────────────────────────────────────────────┘
```

### Common Workflow

1. Pick a ticket from the sprint board
2. Move it to "In Progress"
3. Create a Git branch (often named after the ticket: `PROJ-123-user-auth`)
4. Do the work, commit, push
5. Create a Pull Request
6. Move ticket to "In Review"
7. After PR is merged, move ticket to "Done"

---

## Slack Basics

### What is Slack?

Slack is your team's chat tool. Think of it as organized group messaging.

### Key Concepts

- **Workspace**: Your company's Slack (e.g., `yourcompany.slack.com`)
- **Channels**: Topic-based chat rooms (e.g., `#engineering`, `#project-x`, `#random`)
- **DMs**: Direct messages to individuals or small groups
- **Threads**: Replies to a specific message (keeps conversations organized)

### Channel Etiquette

```
#general          → Company-wide announcements
#engineering      → Engineering team discussions
#team-backend     → Your specific team
#proj-user-auth   → Project-specific channel
#alerts-prod      → Automated alerts (errors, deploys)
#random           → Fun stuff, off-topic
```

### Tips for New Engineers

- **Use threads** — Don't clutter channels with back-and-forth
- **@mention sparingly** — `@channel` notifies everyone; use only when necessary
- **Search first** — Someone may have asked your question before
- **Status updates** — Set your status when in meetings or away

---

## How They Work Together

### Jira ↔ Slack Integration

Most teams connect Jira to Slack:

```
┌─────────────────┐         ┌─────────────────┐
│      Jira       │ ──────▶ │     Slack       │
│                 │         │                 │
│ Ticket updated  │ ──────▶ │ #proj-channel   │
│ Sprint started  │ ──────▶ │ notification    │
│ PR linked       │ ──────▶ │ appears         │
└─────────────────┘         └─────────────────┘
```

**Common integrations:**
- Ticket status changes post to project channel
- You can create Jira tickets from Slack messages
- Daily standups can pull from Jira automatically

### GitHub ↔ Slack Integration

```
┌─────────────────┐         ┌─────────────────┐
│     GitHub      │ ──────▶ │     Slack       │
│                 │         │                 │
│ PR opened       │ ──────▶ │ #code-review    │
│ PR merged       │ ──────▶ │ notification    │
│ CI failed       │ ──────▶ │ #alerts         │
└─────────────────┘         └─────────────────┘
```

### GitHub ↔ Jira Integration

```
┌─────────────────┐         ┌─────────────────┐
│     GitHub      │ ──────▶ │      Jira       │
│                 │         │                 │
│ Branch: PROJ-123│ ──────▶ │ Links to ticket │
│ PR merged       │ ──────▶ │ Auto-transition │
│ Commit message  │ ──────▶ │ Shows in ticket │
└─────────────────┘         └─────────────────┘
```

**Pro tip:** Include the Jira ticket ID in your branch name and commits:
```bash
git checkout -b PROJ-123-add-user-auth
git commit -m "PROJ-123: Implement login endpoint"
```

This automatically links your code to the Jira ticket!

---

## A Day in the Life

Here's how these tools fit into a typical day:

**9:00 AM** — Check Slack
- Read overnight messages in team channel
- Check if any alerts fired

**9:15 AM** — Check Jira
- Look at your assigned tickets
- See what's in the current sprint

**9:30 AM** — Start work
- Pick a ticket, move to "In Progress"
- Create a branch: `git checkout -b PROJ-456-fix-login-bug`

**12:00 PM** — Lunch, check Slack
- Reply to any questions in threads
- Quick sync with teammate via DM

**3:00 PM** — Code review
- Slack notification: PR ready for review
- Review teammate's code on GitHub
- Leave comments, approve

**5:00 PM** — Wrap up
- Push your work
- Update Jira ticket with progress
- Quick Slack message to team if blocked on anything

---

## Quick Reference

### Jira Shortcuts
- `g` then `g` → Quick search
- `c` → Create new issue
- `.` → Open command palette

### Slack Shortcuts
- `Cmd/Ctrl + K` → Quick switch channels
- `Cmd/Ctrl + Shift + \` → React with emoji
- `↑` → Edit last message
- `/remind` → Set a reminder

### Branch Naming Convention
```bash
# Include ticket ID for automatic linking
PROJ-123-short-description
feature/PROJ-123-user-auth
bugfix/PROJ-456-fix-login
```

### Commit Message Convention
```bash
# Start with ticket ID
git commit -m "PROJ-123: Add login endpoint"
git commit -m "PROJ-123: Fix password validation"
```

---

## Summary

| Need to... | Use |
|------------|-----|
| Track what you're working on | Jira |
| Ask a quick question | Slack |
| Have a longer discussion | Slack thread or meeting |
| Store and version code | Git/GitHub |
| Review code | GitHub Pull Request |
| Get notified about code/tickets | Slack (via integrations) |

These tools will become second nature quickly. Don't worry about mastering them immediately — just start using them and you'll pick up the workflows from your team.

---

*Next: Head back to the [main README](../README.md) and continue with the Git exercises!*
