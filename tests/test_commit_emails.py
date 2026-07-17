import unittest

from scripts.check_commit_emails import is_allowed


class CommitEmailPolicyTest(unittest.TestCase):
    def test_github_numeric_noreply_is_allowed(self):
        self.assertTrue(is_allowed("123456+user@users.noreply.github.com"))

    def test_github_plain_noreply_is_allowed(self):
        self.assertTrue(is_allowed("user@users.noreply.github.com"))

    def test_codex_noreply_is_allowed(self):
        self.assertTrue(is_allowed("noreply@openai.com"))

    def test_claude_noreply_is_allowed(self):
        self.assertTrue(is_allowed("noreply@anthropic.com"))

    def test_personal_email_is_blocked(self):
        self.assertFalse(is_allowed("person@example.com"))


if __name__ == "__main__":
    unittest.main()

