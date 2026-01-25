# Git Visual Guide

ASCII diagrams to help understand Git concepts.

---

## The Three States

```
+-------------------+     +-------------------+     +-------------------+
|  Working         |     |   Staging Area    |     |   Repository      |
|  Directory       |     |   (Index)         |     |   (.git)          |
|                  |     |                   |     |                   |
|  Your files as   |     |  Snapshot of      |     |  Permanent        |
|  you see them    |     |  next commit      |     |  history          |
+-------------------+     +-------------------+     +-------------------+
         |                        |                        |
         |     git add            |      git commit        |
         |----------------------->|----------------------->|
         |                        |                        |
         |<-----------------------|------------------------|
         |     git checkout       |      git reset         |
         |                        |                        |
```

---

## Basic Workflow

```
1. Edit files in working directory

   file.py  [modified]
       |
       v

2. Stage changes (git add)

   file.py  -->  staging area
       |
       v

3. Commit (git commit)

   staging area  -->  new commit in repository
       |
       v

4. Push to remote (git push)

   local repo  -->  remote repo (GitHub)
```

---

## Branching

### Creating a Branch

```
Before:
                    main
                      |
                      v
    A---B---C---D---E (HEAD)


After: git checkout -b feature

                    main
                      |
                      v
    A---B---C---D---E
                      ^
                      |
                   feature (HEAD)
```

### Working on a Branch

```
After making commits on feature branch:

                    main
                      |
                      v
    A---B---C---D---E
                      \
                       F---G---H
                               ^
                               |
                            feature (HEAD)
```

---

## Merging vs Rebasing

### Merge (preserves history)

```
Before merge:
                    main
                      |
                      v
    A---B---C---D---E
                      \
                       F---G---H
                               ^
                               |
                            feature

After: git checkout main && git merge feature

                          main (HEAD)
                            |
                            v
    A---B---C---D---E-------M  (merge commit)
                      \    /
                       F--G--H
                             ^
                             |
                          feature
```

### Rebase (linear history)

```
Before rebase:
                    main
                      |
                      v
    A---B---C---D---E
                      \
                       F---G---H
                               ^
                               |
                            feature

After: git checkout feature && git rebase main

                              main
                                |
                                v
    A---B---C---D---E---F'---G'---H'
                                  ^
                                  |
                               feature (HEAD)

Note: F', G', H' are NEW commits (different hashes)
      Original F, G, H still exist but are orphaned
```

---

## Reset Modes

```
                     HEAD
                       |
                       v
    A---B---C---D---E---F


git reset --soft HEAD~1:

    - HEAD moves back to E
    - F's changes stay STAGED
    - Working directory unchanged

                   HEAD
                     |
                     v
    A---B---C---D---E   [F's changes in staging area]


git reset HEAD~1 (mixed, default):

    - HEAD moves back to E
    - F's changes are UNSTAGED
    - Working directory unchanged

                   HEAD
                     |
                     v
    A---B---C---D---E   [F's changes in working directory, not staged]


git reset --hard HEAD~1:

    - HEAD moves back to E
    - F's changes are DISCARDED
    - Working directory reset to E

                   HEAD
                     |
                     v
    A---B---C---D---E   [F is gone!]
```

---

## Cherry-Pick

```
Before cherry-pick:

    main:     A---B---C---D
                          ^
                          HEAD

    feature:  A---B---E---F---G
                              ^
                          (commit we want)


After: git cherry-pick <hash-of-G>

    main:     A---B---C---D---G'
                              ^
                              HEAD

    feature:  A---B---E---F---G

Note: G' is a COPY of G with a new hash
      Original G still exists on feature branch
```

---

## Stash

```
Working state:

    file.py [modified, not committed]


After: git stash

    file.py [clean, matches last commit]

    Stash stack:
    +------------------+
    | stash@{0}: WIP   |  <-- Your changes are here
    +------------------+


After more stashes:

    Stash stack:
    +------------------+
    | stash@{0}: WIP   |  <-- Most recent
    +------------------+
    | stash@{1}: WIP   |
    +------------------+
    | stash@{2}: WIP   |  <-- Oldest
    +------------------+


git stash pop:
    - Applies stash@{0}
    - Removes it from stack

git stash apply:
    - Applies stash@{0}
    - Keeps it in stack
```

---

## Merge Conflicts

```
When Git can't auto-merge:

<<<<<<< HEAD
Your changes (current branch)
=======
Their changes (incoming branch)
>>>>>>> feature-branch


Resolution:
1. Edit file to keep what you want
2. Remove conflict markers (<<<<, ====, >>>>)
3. git add <file>
4. git commit
```

---

## Remote Tracking

```
Local Repository                    Remote (origin)
+------------------+               +------------------+
|                  |               |                  |
|  main            |               |  main            |
|    |             |               |    |             |
|    v             |               |    v             |
|  A---B---C       |               |  A---B---C---D   |
|                  |               |                  |
|  origin/main     |               |                  |
|    |             |               |                  |
|    v             |               |                  |
|  A---B---C       |  git fetch    |                  |
|                  |<--------------|                  |
+------------------+               +------------------+


After fetch:

Local Repository
+------------------+
|                  |
|  main            |
|    |             |
|    v             |
|  A---B---C       |
|                  |
|  origin/main     |  (updated!)
|    |             |
|    v             |
|  A---B---C---D   |
|                  |
+------------------+

Now you can:
- git merge origin/main  (merge remote changes)
- git rebase origin/main (rebase onto remote)
```

---

## Git Bisect (Binary Search)

```
Finding the bug-introducing commit:

    A---B---C---D---E---F---G---H
    ^                           ^
    |                           |
   GOOD                        BAD
   (works)                   (broken)


Step 1: Git checks middle commit (D)

    A---B---C---D---E---F---G---H
    ^           ^               ^
    GOOD      TEST?            BAD

    You test D: "It works!" -> mark GOOD


Step 2: Git checks middle of D-H (F)

    A---B---C---D---E---F---G---H
                ^       ^       ^
              GOOD    TEST?    BAD

    You test F: "It's broken!" -> mark BAD


Step 3: Git checks middle of D-F (E)

    A---B---C---D---E---F---G---H
                ^   ^   ^
              GOOD TEST BAD

    You test E: "It works!" -> mark GOOD


Result: F is the first bad commit!

    A---B---C---D---E---F---G---H
                    ^   ^
                  GOOD  FIRST BAD

Only 3 tests instead of 8!
```

---

## Reflog (Safety Net)

```
Your actions are recorded:

$ git reflog

abc1234 HEAD@{0}: commit: Add feature
def5678 HEAD@{1}: checkout: moving from main to feature
111aaaa HEAD@{2}: reset: moving to HEAD~1
222bbbb HEAD@{3}: commit: Oops wrong code
333cccc HEAD@{4}: commit: Good code

Even after reset --hard, the old commits exist!

To recover 222bbbb:
    git checkout -b recovery 222bbbb

    or

    git reset --hard 222bbbb
```

---

## Tags

```
Repository with tags:

    A---B---C---D---E---F---G
            ^       ^       ^
            |       |       |
          v1.0    v1.1    v2.0

Tags are permanent markers that don't move.
Branches move forward with new commits.
Tags stay fixed at their commit.


Lightweight tag:
    Just a pointer to a commit

Annotated tag:
    Full object with:
    - Tagger name/email
    - Date
    - Message
    - Optional GPG signature
```

---

## Pull Request Flow

```
1. Fork repository (GitHub)

   upstream/repo  -->  your-fork/repo


2. Clone your fork

   your-fork/repo  -->  local machine


3. Create feature branch

   main
     |
     v
   A---B---C
             \
              D---E---F (feature)


4. Push to your fork

   local feature  -->  your-fork/repo feature


5. Create Pull Request

   your-fork/feature  -->  upstream/main

   [Code Review Happens]


6. Merge (after approval)

   upstream/main now includes your changes
```

---

*These diagrams show the conceptual model. Use them to visualize what Git commands do!*
