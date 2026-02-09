from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED = "unordered list"
    ORDERED = "ordered list"

def block_to_blocktype(block):
    block = block.strip()
    if not block:
        return BlockType.PARAGRAPH

    content = block.lstrip("#")
    count = len(block) - len(content)

    if 0 < count <= 6 and content.startswith(" "):
        return BlockType.HEADING

    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    
    if block.startswith(">"):
        return BlockType.QUOTE
    
    lines = block.split("\n")
    unordered = True
    ordered = True
    for i in range(len(lines)):
        if lines[i] != "":
            if not lines[i].startswith("- "):
                unordered = False
            if not lines[i].startswith(f"{i+1}. "):
                ordered = False

    if unordered:
        return BlockType.UNORDERED
    
    if ordered:
        return BlockType.ORDERED
    
    return BlockType.PARAGRAPH