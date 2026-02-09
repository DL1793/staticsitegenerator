class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None:
            return ""
        props = ""
        for key, item in self.props.items():
           props += f' {key}="{item}"'
        return props
    
    def __repr__(self):
        return f"HTMLNode(Tag={self.tag}, Value={self.value}, children={self.children}, props={self.props_to_html()})"