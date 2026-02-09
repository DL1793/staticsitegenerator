from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if children is not None and not isinstance(children, list):
            children = [children]
        super().__init__(tag, None, children, props)
        

    def to_html(self):
        if self.tag is None:
            raise ValueError("Node has no tag.")
        if self.children is None or len(self.children) == 0:
            raise ValueError("Node children are None")
        parent_start = f"<{self.tag}{self.props_to_html()}>"
        parent_end = f"</{self.tag}>"
        for child in self.children:
            child_html = child.to_html()
            parent_start += child_html
        final = parent_start + parent_end
        return final