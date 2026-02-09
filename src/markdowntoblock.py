def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    new_blocks = []
    for i in range(len(blocks)):
        my_block = blocks[i].strip()
        if my_block != "":
            new_blocks.append(my_block)
    return new_blocks