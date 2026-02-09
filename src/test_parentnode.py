import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        child = LeafNode("b", "Hello, world!")
        node = ParentNode("p",child)
        self.assertEqual(node.to_html(), "<p><b>Hello, world!</b></p>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_no_children(self):
        node = ParentNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_to_html_empty_children(self):
        node = ParentNode("p", [])
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_to_html_with_props(self):
        child = LeafNode("span", "hi")
        node = ParentNode("div", [child], {"class": "container"})
        self.assertEqual(node.to_html(),
                         '<div class="container"><span>hi</span></div>')
    def test_to_html_no_tag(self):
        child = LeafNode("span","hi")
        node = ParentNode(None, [child])
        with self.assertRaises(ValueError):
            node.to_html()