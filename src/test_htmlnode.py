import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node1 = HTMLNode(tag="a", value="Boot.dev", props={ "href": "https://boot.dev", "target": "_blank" })
        self.assertEqual(node1.props_to_html(), ' href="https://boot.dev" target="_blank"')
        node2 = HTMLNode(tag="img", props = { "src": "fish.jpg", "width": "1280", "height": "720" })
        self.assertEqual(node2.props_to_html(), ' src="fish.jpg" width="1280" height="720"')
        node3 = HTMLNode(tag="p", props = { "style": "color:yellow;" })
        self.assertEqual(node3.props_to_html(), ' style="color:yellow;"')

    def test_repr(self):
        node1 = HTMLNode(tag="a", value="Boot.dev", props={ "href": "https://boot.dev", "target": "_blank" })
        self.assertEqual(node1.__repr__(), "HTMLNode(a, Boot.dev, None, {'href': 'https://boot.dev', 'target': '_blank'})")
    
    def test_leaf_to_html(self):
        node1 = LeafNode("p", "Hello, world!")
        self.assertEqual(node1.to_html(), "<p>Hello, world!</p>")
        node2 = LeafNode(tag=None, value="Tagless node")
        self.assertEqual(node2.to_html(), "Tagless node")
        node3 = LeafNode("a", "Very suspicious link", { "href": "http://virus.com", "target": "_blank" })
        self.assertEqual(node3.to_html(), '<a href="http://virus.com" target="_blank">Very suspicious link</a>')

if __name__ == "__main__":
    unittest.main()