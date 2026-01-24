# Pull Request & Code Review Etiquette 🤝

Code review is a collaborative process, not a critique. Here's how to do it well.

---

## Creating Good Pull Requests

### 1. Keep PRs Small

| PR Size | Lines Changed | Review Time | Quality |
|---------|---------------|-------------|---------|
| Small ✅ | < 200 | 15-30 min | Thorough |
| Medium ⚠️ | 200-500 | 30-60 min | Decent |
| Large ❌ | 500+ | Hours | Often rushed |

**Smaller PRs get better reviews.** Split large features into multiple PRs.

### 2. Write a Good PR Description

```markdown
## Summary
Brief description of what this PR does.

## Changes
- Added user authentication endpoint
- Created JWT token generation
- Added password hashing with bcrypt

## Testing
- [ ] Unit tests pass
- [ ] Manual testing done
- [ ] Tested edge cases (empty password, long username)

## Screenshots (if UI changes)
[Add screenshots here]

## Related
- Jira: PROJ-123
- Depends on: PR #45
```

### 3. Self-Review First

Before requesting review:
- [ ] Read through your own diff
- [ ] Remove debug code (`console.log`, `print`)
- [ ] Check for commented-out code
- [ ] Ensure tests pass
- [ ] Update documentation if needed

---

## Reviewing Others' Code

### The Right Mindset

- **You're reviewing code, not the person**
- **Assume good intentions**
- **Be curious, not critical**
- **Remember: You'll be reviewed too**

### How to Review

1. **Understand the context first**
   - Read the PR description
   - Check the linked Jira ticket
   - Understand WHAT and WHY before judging HOW

2. **Look for the big picture**
   - Does this approach make sense?
   - Are there architectural concerns?
   - Is this the right place for this code?

3. **Then look at details**
   - Logic errors
   - Edge cases
   - Naming clarity
   - Test coverage

### What to Comment On

✅ **Good things to flag:**
- Bugs or logic errors
- Security issues
- Missing error handling
- Unclear naming
- Missing tests for important cases
- Simpler alternatives

❌ **Avoid nitpicking:**
- Minor style preferences (let formatters handle this)
- Subjective "I would do it differently"
- Tiny optimizations that don't matter

---

## Writing Good Review Comments

### Be Specific

```
❌ Bad:  "This is confusing"
✅ Good: "I'm having trouble following the logic here. 
         Could you add a comment explaining why we check 
         for null before the length check?"
```

### Suggest, Don't Demand

```
❌ Bad:  "Change this to use a map"
✅ Good: "Consider using a map here for O(1) lookup 
         instead of filtering the array each time. 
         What do you think?"
```

### Explain Why

```
❌ Bad:  "Don't use var"
✅ Good: "Let's use const here since this value 
         isn't reassigned. It signals intent to 
         future readers."
```

### Use Prefixes to Signal Intent

```
[Nit] Minor thing, take it or leave it
[Question] I'm curious about this, not blocking
[Suggestion] Consider this approach
[Blocking] This needs to change before merge
```

Examples:
```
[Nit] Could rename 'data' to 'userData' for clarity

[Question] Is there a reason we're not using the 
existing helper function here?

[Blocking] This SQL query is vulnerable to injection. 
Let's use parameterized queries.
```

### Praise Good Work

Don't only leave critical comments:
```
Nice solution! I like how you handled the edge case here.

TIL about this API - thanks for introducing me to it!

This refactor really cleans things up 👍
```

---

## Receiving Feedback

### Stay Open

- **Don't take it personally** — It's about the code
- **Assume good intent** — They're trying to help
- **Ask questions** — If you don't understand feedback, ask

### Respond to Every Comment

- Resolved it? Say so: "Fixed!" or "Good catch, updated"
- Disagree? Explain your reasoning politely
- Need discussion? Say "Let's chat about this" and move offline

### When You Disagree

```
✅ Good: "I see your point about readability. I went with 
         this approach because [reason]. Do you think 
         the performance benefit is worth the trade-off?"

❌ Bad:  "No, this way is better."
```

---

## Common Scenarios

### "Approve, but..."

If the PR is good but has minor issues:
- Leave suggestions
- Approve anyway
- Trust the author to address (or not) minor nits

### Lots of Back-and-Forth

If discussion is getting long:
- Hop on a quick call
- Pair on the code together
- Sometimes a 5-minute conversation beats 10 comments

### Blocking Issues Found

- Be clear it's blocking: "This needs to change before we can merge"
- Explain the impact: "This could cause data loss if..."
- Offer to help if it's complex

### You're Unsure

It's okay to say:
- "I'm not sure about this, could someone else take a look?"
- "This is outside my expertise, but it looks reasonable to me"

---

## Review Checklist

When reviewing, consider:

**Functionality**
- [ ] Does it do what the ticket asks?
- [ ] Are edge cases handled?
- [ ] Error handling in place?

**Code Quality**
- [ ] Is it readable?
- [ ] Are names clear?
- [ ] Is there duplication?
- [ ] Is it in the right place architecturally?

**Testing**
- [ ] Are there tests?
- [ ] Do tests cover the important cases?
- [ ] Would you trust these tests to catch regressions?

**Security**
- [ ] No hardcoded secrets?
- [ ] Input validation?
- [ ] SQL/injection vulnerabilities?

**Performance** (when relevant)
- [ ] Obvious inefficiencies?
- [ ] N+1 queries?
- [ ] Unnecessary network calls?

---

## Team Norms to Establish

Discuss with your team:

1. **Response time** — How quickly should reviews happen? (e.g., within 4 hours)
2. **Approval count** — How many approvals needed? (usually 1-2)
3. **Who can merge** — Author or reviewer?
4. **Nitpicks** — Are they expected to be fixed?

---

## Summary

| As Author | As Reviewer |
|-----------|-------------|
| Keep PRs small | Understand context first |
| Write good descriptions | Comment on substance, not style |
| Self-review before requesting | Be specific and suggest |
| Respond to all comments | Explain the "why" |
| Don't take feedback personally | Praise good work too |

**The goal is better code AND a better team.**

---

*Back to [main README](../README.md)*
