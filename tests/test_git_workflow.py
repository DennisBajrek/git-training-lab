"""
Git Workflow Verification Tests

These tests verify that students have actually performed the git operations
described in each exercise, not just implemented the Python code.

Run with: pytest tests/test_git_workflow.py -v

Note: These tests are OPTIONAL and may be skipped if git history
doesn't match expected patterns. The main purpose is to give
feedback, not to fail students.
"""

import pytest
import os
import sys

# Add tests directory to path
sys.path.insert(0, os.path.dirname(__file__))

from git_verification import GitVerifier


# Skip all tests if not in a git repository
def is_git_repo():
    """Check if current directory is a git repository."""
    verifier = GitVerifier()
    return verifier._run_git("rev-parse", "--git-dir") != ""


pytestmark = pytest.mark.skipif(
    not is_git_repo(),
    reason="Not in a git repository"
)


class TestGitBasics:
    """Verify basic git operations (Exercises 1-4)."""

    @pytest.fixture
    def verifier(self):
        return GitVerifier()

    def test_has_commits(self, verifier):
        """Verify repository has commits."""
        count = verifier.commit_count()
        assert count > 0, "Repository should have at least one commit"

    def test_has_remote(self, verifier):
        """Verify remote is configured."""
        assert verifier.has_remote("origin"), (
            "Remote 'origin' should be configured. "
            "Run: git remote add origin <url>"
        )

    @pytest.mark.skip(reason="Exercise-specific - enable when checking Exercise 1")
    def test_exercise_1_committed(self, verifier):
        """Verify Exercise 1 was committed."""
        has_commit = (
            verifier.has_commit_message("exercise 1") or
            verifier.has_commit_message("reverse") or
            verifier.has_commit_with_file("exercises/solo/exercise_1.py")
        )
        assert has_commit, (
            "Exercise 1 should be committed. "
            "Run: git add exercises/solo/exercise_1.py && git commit -m 'Exercise 1: Implement reverse_string'"
        )


class TestBranching:
    """Verify branching operations (Exercise 3)."""

    @pytest.fixture
    def verifier(self):
        return GitVerifier()

    def test_main_branch_exists(self, verifier):
        """Verify main branch exists."""
        has_main = verifier.branch_exists("main") or verifier.branch_exists("master")
        assert has_main, "Repository should have a main or master branch"

    @pytest.mark.skip(reason="Exercise-specific - enable when checking Exercise 3")
    def test_feature_branch_was_created(self, verifier):
        """Verify a feature branch was created for Exercise 3."""
        branches = verifier.get_branches(include_remote=True)
        feature_branches = [b for b in branches if "feature" in b.lower() or "exercise" in b.lower()]
        assert len(feature_branches) > 0, (
            "You should create a feature branch for Exercise 3. "
            "Run: git checkout -b feature/find-max"
        )


class TestMergeConflicts:
    """Verify merge conflict resolution (Exercise 8)."""

    @pytest.fixture
    def verifier(self):
        return GitVerifier()

    @pytest.mark.skip(reason="Exercise-specific - enable when checking Exercise 8")
    def test_merge_was_performed(self, verifier):
        """Verify a merge was performed."""
        has_merge = verifier.has_merge_commit(limit=30)
        assert has_merge, (
            "Exercise 8 requires merging branches. "
            "Run: git merge teammate/exercise-8"
        )

    @pytest.mark.skip(reason="Exercise-specific - enable when checking Exercise 8")
    def test_teammate_branch_merged(self, verifier):
        """Verify teammate branch was merged."""
        has_merge_msg = (
            verifier.has_commit_message("merge") or
            verifier.has_commit_message("teammate") or
            verifier.has_commit_message("conflict")
        )
        assert has_merge_msg, (
            "Exercise 8: Merge the teammate/exercise-8 branch and resolve conflicts"
        )


class TestAdvancedOperations:
    """Verify advanced git operations (Exercises 10-15)."""

    @pytest.fixture
    def verifier(self):
        return GitVerifier()

    @pytest.mark.skip(reason="Exercise-specific - enable when checking Exercise 15")
    def test_tag_was_created(self, verifier):
        """Verify a tag was created for Exercise 15."""
        tags = verifier.get_tags()
        version_tags = [t for t in tags if t.startswith("v")]
        assert len(version_tags) > 0, (
            "Exercise 15 requires creating a version tag. "
            "Run: git tag -a v1.0.0 -m 'Release v1.0.0'"
        )

    @pytest.mark.skip(reason="Exercise-specific - enable when checking Exercise 12")
    def test_reflog_has_entries(self, verifier):
        """Verify reflog has entries (for Exercise 12 recovery)."""
        has_checkout = verifier.reflog_contains("checkout")
        has_commit = verifier.reflog_contains("commit")
        assert has_checkout or has_commit, (
            "Reflog should have entries showing your git activity"
        )


class TestCommitQuality:
    """Verify commit message quality and practices."""

    @pytest.fixture
    def verifier(self):
        return GitVerifier()

    def test_commits_have_messages(self, verifier):
        """Verify commits have meaningful messages."""
        last_msg = verifier.get_last_commit_message()
        assert len(last_msg) > 5, (
            "Commit messages should be descriptive. "
            "Good: 'Implement reverse_string function' "
            "Bad: 'fix'"
        )

    def test_no_wip_commits_on_main(self, verifier):
        """Warn about WIP commits on main branch."""
        current = verifier.get_current_branch()
        if current in ["main", "master"]:
            has_wip = verifier.has_commit_message("WIP", limit=5)
            if has_wip:
                pytest.skip(
                    "Note: You have 'WIP' commits on main. "
                    "Consider squashing these before pushing."
                )


class TestWorkflowProgress:
    """Track overall progress through exercises."""

    @pytest.fixture
    def verifier(self):
        return GitVerifier()

    def test_report_progress(self, verifier):
        """Report which exercises appear to be committed."""
        committed = []
        for i in range(1, 16):
            if verifier.has_commit_message(f"exercise {i}") or \
               verifier.has_commit_with_file(f"exercises/solo/exercise_{i}.py"):
                committed.append(i)

        if committed:
            print(f"\n=== Git Progress Report ===")
            print(f"Exercises with commits detected: {committed}")
            print(f"Total: {len(committed)}/15 exercises")
        else:
            print("\n=== Git Progress Report ===")
            print("No exercise commits detected yet. Get started!")

        # This test always passes - it's just for reporting
        assert True


# Helper test to show current git status
class TestGitStatus:
    """Show current git status for debugging."""

    @pytest.fixture
    def verifier(self):
        return GitVerifier()

    def test_show_status(self, verifier):
        """Display current git status."""
        print(f"\n=== Git Status ===")
        print(f"Current branch: {verifier.get_current_branch()}")
        print(f"Total commits: {verifier.commit_count()}")
        print(f"Working directory clean: {verifier.is_clean()}")
        print(f"Remote configured: {verifier.has_remote('origin')}")

        branches = verifier.get_branches()
        if branches:
            print(f"Local branches: {', '.join(branches[:5])}")

        tags = verifier.get_tags()
        if tags:
            print(f"Tags: {', '.join(tags[:5])}")

        # Always pass - this is informational
        assert True
