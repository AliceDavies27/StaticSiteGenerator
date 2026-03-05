import unittest

from htmlnode import HTMLNode


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

if __name__ == "__main__":
    unittest.main()