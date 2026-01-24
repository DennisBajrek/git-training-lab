# Workflow Guide 🔄

How Git fits into your daily work with Jira, Slack, and code review.

---

# Part 1: Jira & Slack

## The Typical Stack

| Tool | Purpose |
|------|---------|
| **Slack** | Real-time communication |
| **Jira** | Task/issue tracking |
| **Git/GitHub** | Code versioning |

These integrate with each other.

---

## Jira Basics

Jira tracks work as "tickets" (also called "issues").

### Key Concepts

- **Ticket**: A single unit of work (bug fix, feature, task)
- **Sprint**: A time-boxed period (usually 2 weeks)
- **Board**: Visual view (To Do → In Progress → Done)

### Ticket Example

```
PROJ-123: Add user authentication
Status: In Progress
Assignee: You

Description:
Implement login/logout with JWT tokens.
```

### Workflow

1. Pick a ticket from the sprint board
2. Move to "In Progress"
3. Create a Git branch named after the ticket: `PROJ-123-user-auth`
4. Do the work, commit, push
5. Create a Pull Request
6. Move ticket to "In Review"
7. After merge, move to "Done"

---

## Slack Basics

Slack is organized chat for teams.

### Key Concepts

- **Channels**: Topic-based rooms (`#engineering`, `#project-x`)
- **DMs**: Direct messages
- **Threads**: Replies to a specific message

### Tips

- **Use threads** — keeps channels clean
- **@mention sparingly** — `@channel` notifies everyone
- **Search first** — someone may have asked before

---

## How They Connect

### Branch Naming

Include the ticket ID:
```bash
git checkout -b PROJ-123-user-auth
```

### Commit Messages

Start with ticket ID:
```bash
git commit -m "PROJ-123: Add login endpoint"
```

This automatically links your code to the Jira ticket!

### Integrations

- Jira → Slack: Ticket updates post to channels
- GitHub → Slack: PR notifications
- GitHub → Jira: Commits link to tickets

---

## A Typical Day

**Morning**
- Check Slack for overnight messages
- Check Jira for your assigned tickets
- Pick a ticket, move to "In Progress"
- Create branch: `git checkout -b PROJ-123-feature`

**During the day**
- Code, commit, push
- Respond to Slack threads
- Review teammate PRs

**End of day**
- Push your work
- Update Jira ticket with progress
- Slack team if blocked

---

# Part 2: Pull Requests & Code Review

## Creating Good PRs

### Keep PRs Small

| Size | Lines | Review Quality |
|------|-------|----------------|
| Small ✅ | < 200 | Thorough |
| Medium ⚠️ | 200-500 | Decent |
| Large ❌ | 500+ | Often rushed |

### Write a Good Description

```markdown
## Summary
Brief description of what this PR does.

## Changes
- Added user authentication endpoint
- Created JWT token generation
- Added password hashing

## Testing
- [ ] Unit tests pass
- [ ] Manual testing done

## Related
- Jira: PROJ-123
```

### Self-Review First

Before requesting review:
- Read your own diff
- Remove debug code (`console.log`, `print`)
- Ensure tests pass

---

## Reviewing Others' Code

### The Right Mindset

- Review code, not the person
- Assume good intentions
- Be curious, not critical

### What to Comment On

✅ **Good:**
- Bugs or logic errors
- Security issues
- Missing error handling
- Unclear naming

❌ **Avoid:**
- Minor style preferences
- "I would do it differently"

---

## Writing Good Comments

### Be Specific

```
❌ "This is confusing"
✅ "Could you add a comment explaining why we check null before length?"
```

### Suggest, Don't Demand

```
❌ "Change this to use a map"
✅ "Consider using a map here for O(1) lookup. What do you think?"
```

### Use Prefixes

```
[Nit] Minor thing, take it or leave it
[Question] I'm curious, not blocking
[Blocking] This needs to change before merge
```

### Praise Good Work

```
Nice solution! I like how you handled the edge case.
TIL about this API — thanks!
```

---

## Receiving Feedback

### Stay Open

- Don't take it personally
- Ask questions if unclear
- Respond to every comment

### When You Disagree

```
✅ "I see your point. I went with this because [reason]. 
    Do you think the trade-off is worth it?"

❌ "No, this way is better."
```

---

## Review Checklist

**Functionality**
- [ ] Does it do what the ticket asks?
- [ ] Edge cases handled?
- [ ] Error handling in place?

**Code Quality**
- [ ] Readable?
- [ ] Clear names?
- [ ] No duplication?

**Testing**
- [ ] Tests exist?
- [ ] Tests cover important cases?

**Security**
- [ ] No hardcoded secrets?
- [ ] Input validated?

---

## Summary

| As Author | As Reviewer |
|-----------|-------------|
| Keep PRs small | Understand context first |
| Write good descriptions | Be specific and suggest |
| Self-review first | Explain the "why" |
| Respond to all comments | Praise good work too |

**The goal is better code AND a better team.**

---

*Back to [main README](../README.md)*
