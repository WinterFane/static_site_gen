from textnode import TextNode,TextType

class HTMLNode:
    def __init__(self, tag=None, value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HtmlNode(tag:{self.tag},value:{self.value},children:{self.children},props:{self.props})"
    
    def __eq__(self,target):
        return (
            self.tag == target.tag
            and self.value == target.value
            and self.children == target.children
            and self.props == target.props
        )

    def to_html(self):
        raise NotImplementedError("TO DO")
    
    def props_to_html(self):
        str = ""
        if(self.props == None):
            return str
        
        for key in self.props:
            str = f"{str} {key}=\"{self.props[key]}\""
        return str
