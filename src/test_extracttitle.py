import unittest
from extracttitle import extract_title

class test_extracttitle(unittest.TestCase):
    def test_simple_heading(self):
        title = '''
# This is a header.
'''
        self.assertEqual(extract_title(title), "This is a header.")

    def test_later_heading(self):
        title = '''
## This is the header 2.

This is just a paragraph.

# This is a header.
'''
        self.assertEqual(extract_title(title), "This is a header.")

    def test_empty_string(self):
        title = ""

        self.assertRaises(SyntaxError)

    def test_false_header(self):
        title = "#This is not a header."

        self.assertRaises(SyntaxError)

    def test_invalid_title(self):
        title = None

        self.assertRaises(ValueError)

    def test_invalid_type_title(self):
        title = 42

        self.assertRaises(ValueError)