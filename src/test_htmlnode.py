import unittest

from htmlnode import HTMLNode


class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("h1","HELLLO")
        node2 = HTMLNode("h1","HELLLO")
        self.assertEqual(node, node2)

    def test_eq(self):
        node = HTMLNode("h1","HELLLO")
        node2 = HTMLNode("h1","HELLLO")
        self.assertEqual(node, node2)

    def test_props_to_html_with_href(self):
        node = HTMLNode("a", "Click me", None, {"href": "https://www.reddit.com/r/pcgaming/"})
        self.assertEqual(node.props_to_html(), ' href="https://www.reddit.com/r/pcgaming/"')
    
    def test_props1(self):
        node = HTMLNode("a", "Click me", None)
        self.assertEqual(node.props_to_html(), '')
    
    def test_props2(self):
        node = HTMLNode("a", "Click me", None, {"href": "https://www.reddit.com/r/pcgaming/","target": "_blank",})
        self.assertEqual(node.props_to_html(), ' href="https://www.reddit.com/r/pcgaming/" target="_blank"')

    def test_props3(self):
        node = HTMLNode("a", "Click me", None, {"aria": "@@@","target": "_blank",})
        self.assertEqual(node.props_to_html(), ' aria="@@@" target="_blank"')



if __name__ == "__main__":
    unittest.main()