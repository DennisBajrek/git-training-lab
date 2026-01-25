"""
Git Command Verification Utilities

These utilities help verify that students have actually run git commands
as part of their exercises, not just implemented the Python code.

Usage:
    from git_verification import GitVerifier

    verifier = GitVerifier()

    # Check if a commit message exists
    assert verifier.has_commit_message("Exercise 1")

    # Check if a branch exists
    assert verifier.branch_exists("feature/my-branch")

    # Check commit count
    assert verifier.commit_count() >= 5
"""

import subprocess
import os
from typing import List, Optional


class GitVerifier:
    """Utility class for verifying git operations."""

    def __init__(self, repo_path: Optional[str] = None):
        """
        Initialize the GitVerifier.

        Args:
            repo_path: Path to the git repository. Defaults to current directory.
        """
        self.repo_path = repo_path or os.getcwd()

    def _run_git(self, *args) -> str:
        """Run a git command and return output."""
        try:
            result = subprocess.run(
                ["git", *args],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                timeout=10
            )
            return result.stdout.strip()
        except subprocess.TimeoutExpired:
            return ""
        except Exception:
            return ""

    def has_commit_message(self, message_substring: str, limit: int = 50) -> bool:
        """
        Check if any recent commit message contains the given substring.

        Args:
            message_substring: Text to search for in commit messages
            limit: Number of recent commits to check

        Returns:
            True if a matching commit is found
        """
        output = self._run_git("log", f"-{limit}", "--oneline")
        return message_substring.lower() in output.lower()

    def has_commit_with_file(self, filepath: str, limit: int = 50) -> bool:
        """
        Check if any recent commit modified the given file.

        Args:
            filepath: Path to the file (relative to repo root)
            limit: Number of recent commits to check

        Returns:
            True if a commit touching this file is found
        """
        output = self._run_git("log", f"-{limit}", "--oneline", "--", filepath)
        return bool(output)

    def branch_exists(self, branch_name: str, include_remote: bool = True) -> bool:
        """
        Check if a branch exists.

        Args:
            branch_name: Name of the branch
            include_remote: Also check remote branches

        Returns:
            True if branch exists
        """
        # Check local branches
        local = self._run_git("branch", "--list", branch_name)
        if local:
            return True

        if include_remote:
            remote = self._run_git("branch", "-r", "--list", f"*/{branch_name}")
            if remote:
                return True

        return False

    def get_branches(self, include_remote: bool = False) -> List[str]:
        """
        Get list of all branches.

        Args:
            include_remote: Include remote branches

        Returns:
            List of branch names
        """
        if include_remote:
            output = self._run_git("branch", "-a")
        else:
            output = self._run_git("branch")

        branches = []
        for line in output.split('\n'):
            line = line.strip().lstrip('* ')
            if line and not line.startswith('remotes/'):
                branches.append(line)
            elif line.startswith('remotes/') and include_remote:
                branches.append(line.replace('remotes/', ''))

        return branches

    def commit_count(self, branch: str = "HEAD") -> int:
        """
        Get the number of commits in a branch.

        Args:
            branch: Branch name or ref

        Returns:
            Number of commits
        """
        output = self._run_git("rev-list", "--count", branch)
        try:
            return int(output)
        except ValueError:
            return 0

    def tag_exists(self, tag_name: str) -> bool:
        """
        Check if a tag exists.

        Args:
            tag_name: Name of the tag

        Returns:
            True if tag exists
        """
        output = self._run_git("tag", "-l", tag_name)
        return bool(output)

    def get_tags(self) -> List[str]:
        """
        Get list of all tags.

        Returns:
            List of tag names
        """
        output = self._run_git("tag", "-l")
        return [t.strip() for t in output.split('\n') if t.strip()]

    def has_merge_commit(self, limit: int = 20) -> bool:
        """
        Check if there are any merge commits in recent history.

        Args:
            limit: Number of recent commits to check

        Returns:
            True if a merge commit is found
        """
        output = self._run_git("log", f"-{limit}", "--merges", "--oneline")
        return bool(output)

    def file_was_modified_in_commit(self, filepath: str, commit: str = "HEAD") -> bool:
        """
        Check if a file was modified in a specific commit.

        Args:
            filepath: Path to the file
            commit: Commit reference

        Returns:
            True if file was modified in that commit
        """
        output = self._run_git("show", "--name-only", "--format=", commit)
        return filepath in output

    def get_current_branch(self) -> str:
        """
        Get the name of the current branch.

        Returns:
            Current branch name
        """
        return self._run_git("rev-parse", "--abbrev-ref", "HEAD")

    def is_clean(self) -> bool:
        """
        Check if the working directory is clean.

        Returns:
            True if no uncommitted changes
        """
        output = self._run_git("status", "--porcelain")
        return not bool(output)

    def get_last_commit_message(self) -> str:
        """
        Get the message of the last commit.

        Returns:
            Last commit message
        """
        return self._run_git("log", "-1", "--format=%s")

    def has_remote(self, remote_name: str = "origin") -> bool:
        """
        Check if a remote exists.

        Args:
            remote_name: Name of the remote

        Returns:
            True if remote exists
        """
        output = self._run_git("remote")
        return remote_name in output.split('\n')

    def reflog_contains(self, action_substring: str, limit: int = 50) -> bool:
        """
        Check if reflog contains a specific action.

        Args:
            action_substring: Text to search for in reflog
            limit: Number of recent entries to check

        Returns:
            True if found in reflog
        """
        output = self._run_git("reflog", f"-{limit}")
        return action_substring.lower() in output.lower()


# Convenience functions for quick checks
def verify_exercise_committed(exercise_num: int) -> bool:
    """Check if an exercise has been committed."""
    verifier = GitVerifier()
    return verifier.has_commit_message(f"Exercise {exercise_num}")


def verify_branch_created(branch_name: str) -> bool:
    """Check if a branch was created."""
    verifier = GitVerifier()
    return verifier.branch_exists(branch_name)


def verify_tag_created(tag_name: str) -> bool:
    """Check if a tag was created."""
    verifier = GitVerifier()
    return verifier.tag_exists(tag_name)
