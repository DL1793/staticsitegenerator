import unittest
from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(props={"href": "https://google.com", "target": "_blank"})
        node_props = node.props_to_html()
        result = ' href="https://google.com" target="_blank"'
        self.assertEqual(node_props, result)

    def test_no_props(self):
        node = HTMLNode()
        node_props = node.props_to_html()
        self.assertEqual(node_props, "")
    
    def test_repr(self):
        node = HTMLNode("p", "Hello, World!", None, props={"href": "https://google.com", "target": "_blank"})
        result = repr(node)
        expected = 'HTMLNode(Tag=p, Value=Hello, World!, children=None, props= href="https://google.com" target="_blank")'
        self.assertEqual(result, expected)