import unittest
from gencontent import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_eq(self):
        actual = extract_title("# This is a title")
        self.assertEqual(actual, "This is a title")

    def test_eq_double(self):
        actual = extract_title(
            "# This is a title\n\n# This is a second title that should be ignored"
        )
        self.assertEqual(actual, "This is a title")

    def test_eq_long(self):
        actual = extract_title(
            "## title\n\n# This is a title\n\nThis is a paragraph"
        )
        self.assertEqual(actual, "This is a title")

    def test_none(self):
        with self.assertRaises(ValueError):
            extract_title("no title here\n## only h2")


if __name__ == "__main__":
    unittest.main()
