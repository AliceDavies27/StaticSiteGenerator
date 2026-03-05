class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("Method not implemented.")

    def props_to_html(self):
        props_string = ""
        
        for attr, value in self.props.items():
            props_string += f' {attr}="{value}"'

        return props_string
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"