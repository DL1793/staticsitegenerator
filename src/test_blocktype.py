import unittest
from BlockType import BlockType, block_to_blocktype

class TestBlockTypes(unittest.TestCase):
    def test_heading(self):
        block = '''
# This is a heading
'''
        self.assertEqual(block_to_blocktype(block), BlockType.HEADING)

    def test_six_heading(self):
        block = '''
###### This is a heading 6
'''
        self.assertEqual(block_to_blocktype(block), BlockType.HEADING)

    def test_broken_space_heading(self):
        block = '''
###This is not a heading
'''

    def test_empty_heading(self):
        block = '''
####
'''
        self.assertEqual(block_to_blocktype(block), BlockType.PARAGRAPH)

        self.assertEqual(block_to_blocktype(block), BlockType.PARAGRAPH)

    def test_broken_heading(self):
        block = '''
###90# This is not a heading
'''
        self.assertEqual(block_to_blocktype(block), BlockType.PARAGRAPH)

    def test_long_broken_heading(self):
        block = '''
####### This is not a heading
'''
        self.assertEqual(block_to_blocktype(block),BlockType.PARAGRAPH)

    def test_code(self):
        block = '''
```
This is a code block```
'''
        self.assertEqual(block_to_blocktype(block), BlockType.CODE)
    def test_quote(self):
        block = '''
>This is a quote block
'''
        self.assertEqual(block_to_blocktype(block), BlockType.QUOTE)
    def test_quote_with_space(self):
        block = '''
> This is a quote block
'''
        self.assertEqual(block_to_blocktype(block), BlockType.QUOTE)    

    def test_unordered(self):
        block = '''
- item 1
- item 2
- item 3
'''
        self.assertEqual(block_to_blocktype(block), BlockType.UNORDERED)
    
    def test_broken_unordered(self):
        block = '''
- item 1
- item 2
1. not an item
'''
        self.assertEqual(block_to_blocktype(block), BlockType.PARAGRAPH)

    def test_ordered(self):
        block = '''
1. First item
2. Second Item
3. Third item
'''
        self.assertEqual(block_to_blocktype(block), BlockType.ORDERED)

    def test_broken_ordered(self):
        block = '''
1. First Item
2. Second Item
3.Forgot space
'''
        self.assertEqual(block_to_blocktype(block), BlockType.PARAGRAPH)
    
    def test_paragraph(self):
        block = '''
This is just a paragraph.
'''
        self.assertEqual(block_to_blocktype(block), BlockType.PARAGRAPH)