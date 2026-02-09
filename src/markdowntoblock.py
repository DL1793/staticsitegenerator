from parentnode import ParentNode
from leafnode import LeafNode
from BlockType import BlockType, block_to_blocktype
from splitnodes import text_to_textnodes
from textnode import TextType, TextNode, text_node_to_html_node

def markdown_to_blocks(markdown):
    if not markdown:
        return []
    blocks = markdown.split("\n\n")
    new_blocks = []
    for i in range(len(blocks)):
        my_block = blocks[i].strip()
        if my_block != "":
            new_blocks.append(my_block)
    return new_blocks

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    root = ParentNode(
        tag="div",
        children=[]
    )
    for block in blocks:
        blockType = block_to_blocktype(block)
        
        tag = ""
        match blockType:
            case BlockType.PARAGRAPH:
                tag = "p"
                block = " ".join(block.splitlines())
            case BlockType.HEADING:
                content = block.lstrip("#")
                count = len(block) - len(content)
                tag = f"h{count}"
                block = strip_header(block)

            case BlockType.CODE:
                inner = strip_code(block)
                code_leaf = LeafNode("code", inner)
                pre_node = ParentNode("pre",[code_leaf])
                root.children.append(pre_node)
                continue

            case BlockType.QUOTE:
                tag = "blockquote"
                block= strip_quote(block)

            case BlockType.UNORDERED:
                block = block.split("\n")
                parent = ParentNode("ul", [])
                for line in block:
                    line = line[2:]
                    nodes = text_to_textnodes(line)
                    list_node = ParentNode("li",[])
                    for node in nodes:
                        html_node = text_node_to_html_node(node)
                        list_node.children.append(html_node)
                    parent.children.append(list_node)
                root.children.append(parent)
                continue

            case BlockType.ORDERED:
                block = block.split("\n")
                parent = ParentNode("ol", [])
                for i in range(len(block)):
                    line = block[i][len(f"{i+1}. "):]
                    nodes = text_to_textnodes(line)
                    list_node = ParentNode("li", [])
                    for node in nodes:
                        html_node = text_node_to_html_node(node)
                        list_node.children.append(html_node)
                    parent.children.append(list_node)
                root.children.append(parent)
                continue

        nodes = text_to_textnodes(block)
        html_nodes = []
        for node in nodes:
            html_nodes.append(text_node_to_html_node(node))
        blockNode = ParentNode(tag,html_nodes)
        root.children.append(blockNode)
    return root

def strip_header(block):
    return block.lstrip("#").lstrip()

def strip_quote(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        quote = line.lstrip("> ")
        new_lines.append(quote)
    new_block = "\n".join(new_lines)
    return new_block

def strip_code(block):
    return block[block.find('\n')+1:block.rfind('\n')+1]
