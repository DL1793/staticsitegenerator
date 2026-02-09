import unittest
from markdowntoblock import markdown_to_blocks

class TestMarkdownToBlock(unittest.TestCase):
        def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
                """
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

        def test_markdown_to_blocks_with_spaces(self):
            md = """



This is **bolded** paragraph



This is a paragraph after a few newlines.
This is the same paragraph on a new line

- This is a list
- with items
                """
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is a paragraph after a few newlines.\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

        def test_markdown_empty(self):
            md = """



                    """ 
            blocks = markdown_to_blocks(md)
            self.assertEqual(blocks, [])