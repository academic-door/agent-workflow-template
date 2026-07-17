import tempfile
import unittest
from pathlib import Path

from scripts.check_repository_hygiene import scan


class RepositoryHygieneTest(unittest.TestCase):
    def test_clean_markdown_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "README.md").write_text("No secrets here.\n", encoding="utf-8")

            self.assertEqual(scan(root), [])

    def test_windows_user_path_is_blocked(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path_text = "Path: " + "C:" + "\\Users" + "\\Name" + "\\Desktop" + "\\data.csv"
            (root / "note.md").write_text(path_text, encoding="utf-8")

            self.assertTrue(scan(root))

    def test_github_token_is_blocked(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            token_text = "ghp_" + "abcdefghijklmnopqrstuvwxyz"
            (root / "config.txt").write_text(token_text, encoding="utf-8")

            self.assertTrue(scan(root))
