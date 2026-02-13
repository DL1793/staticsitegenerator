from markdowntoblock import markdown_to_blocks

def extract_title(markdown):
    if markdown is None:
        raise ValueError("File is empty.")
    if not isinstance(markdown, str):
        raise ValueError("Not a string.")
    title = ""
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        content = block.lstrip("#")
        count = len(block) - len(content)
        if count == 1:
            if content.startswith(" "):
                title = content
            break
    if title == "":
        raise SyntaxError("No h1 header found in file.")
    return title.strip()