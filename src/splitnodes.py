from textnode import TextNode, TextType
from extractimages import extract_markdown_links, extract_markdown_images

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    if old_nodes is None:
        return []
    if not isinstance(old_nodes, list):
        old_nodes = [old_nodes]
    for node in old_nodes:
        if(node.text_type != TextType.TEXT):
            new_nodes.append(node)
        else:
            split_nodes = node.text.split(delimiter)
            if len(split_nodes) % 2 == 0:
                raise SyntaxError("Unmatched delimiter.")
            for i in range(len(split_nodes)):
                if split_nodes[i] != "":
                    if i % 2 != 0:
                        my_node = TextNode(split_nodes[i], text_type)
                        new_nodes.append(my_node)
                    else:
                        my_node = TextNode(split_nodes[i], TextType.TEXT)
                        new_nodes.append(my_node)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    if old_nodes is None:
        return []
    if not isinstance(old_nodes, list):
        old_nodes = [old_nodes]
    for node in old_nodes:
        if(node.text_type != TextType.TEXT):
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        original_text = node.text
        if not images:
            new_nodes.append(node)
            continue
        for image_text, image_url in images:
            before, after = original_text.split(f"![{image_text}]({image_url})", 1)
            if before != "":
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(image_text,TextType.IMAGE,image_url))
            original_text = after
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    if old_nodes is None:
        return []
    if not isinstance(old_nodes, list):
        old_nodes = [old_nodes]
    for node in old_nodes:
        if(node.text_type != TextType.TEXT):
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        original_text = node.text
        if not links:
            new_nodes.append(node)
            continue
        for link_text, link_url in links:
            before, after = original_text.split(f"[{link_text}]({link_url})", 1)
            if before != "":
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(link_text,TextType.LINK,link_url))
            original_text = after
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    new_nodes = split_nodes_delimiter(node, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes