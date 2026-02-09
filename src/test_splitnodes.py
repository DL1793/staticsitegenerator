import unittest
from textnode import TextNode, TextType
from splitnodes import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes

class TestSplitNodes(unittest.TestCase):
    def test_splitbold(self):
        node = TextNode("This is a **bold** text", TextType.TEXT)
        result = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ]
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), result)

    def test_multiple(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        node2 = TextNode("Another **bold** text", TextType.TEXT)
        result = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
            TextNode("Another ",TextType.TEXT),
            TextNode("bold",TextType.BOLD),
            TextNode(" text",TextType.TEXT)
        ]
        self.assertEqual(split_nodes_delimiter([node, node2], "**", TextType.BOLD), result)

    def test_empty(self):
        result = []
        self.assertEqual(split_nodes_delimiter(None, "**", TextType.BOLD), result)

    def test_multiple_markdown(self):
        node = TextNode("This is **very** much **bold**", TextType.TEXT)
        result = [
            TextNode("This is ", TextType.TEXT),
            TextNode("very", TextType.BOLD),
            TextNode(" much ", TextType.TEXT),
            TextNode("bold", TextType.BOLD)
        ]
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), result)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_one_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_start(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) at the start.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" at the start.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_no_images(self):
        node = TextNode(
            "This is text with no images",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with no images", TextType.TEXT)
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with [a link](https://www.google.com) and another [one](https://www.linkedin.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with ", TextType.TEXT),
                TextNode("a link", TextType.LINK, "https://www.google.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "one", TextType.LINK, "https://www.linkedin.com"
                ),
            ],
            new_nodes,
        )
    
    def test_split_link_start(self):
        node = TextNode(
            "[a link](https://www.google.com) at the beginning",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("a link", TextType.LINK, "https://www.google.com"),
                TextNode(" at the beginning", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_link_end(self):
        node = TextNode(
            "This ends with [a link](https://www.google.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This ends with ", TextType.TEXT),
                TextNode("a link", TextType.LINK, "https://www.google.com"),
            ],
            new_nodes,
        )
    
    def test_split_full(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertListEqual(nodes, [
        TextNode("This is ", TextType.TEXT),
        TextNode("text", TextType.BOLD),
        TextNode(" with an ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word and a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" and an ", TextType.TEXT),
        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.TEXT),
        TextNode("link", TextType.LINK, "https://boot.dev"),
        ])

    def test_split_simple(self):
        text = "Just plain text"
        nodes = text_to_textnodes(text)
        self.assertListEqual(nodes,
                             [
                                 TextNode("Just plain text", TextType.TEXT)
                             ])
    def test_split_bold(self):
        text = "Some **bold** text"
        nodes = text_to_textnodes(text)
        self.assertListEqual(nodes,
                             [
                                 TextNode("Some ", TextType.TEXT),
                                 TextNode("bold", TextType.BOLD),
                                 TextNode(" text", TextType.TEXT)
                             ])
    def test_split_raise_valueerror(self):
        text = "Some **broken text"
        with self.assertRaises(SyntaxError):
            text_to_textnodes(text)