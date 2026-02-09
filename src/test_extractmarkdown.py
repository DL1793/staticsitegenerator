import unittest
from extractimages import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "![img](https://ex.com/i.png)[link](https://ex.com)"
        )
        self.assertListEqual([("link", "https://ex.com")], matches)
    
    def test_false_link(self):
        matches = extract_markdown_links(
            "This is not a link: [just text] and this is: [real link](https://real.com)"
        )
        self.assertListEqual([("real link", "https://real.com")], matches)