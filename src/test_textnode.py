import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        node = TextNode("Text node", TextType.IMAGE, "/test.jpg")
        node2 = TextNode("Text node", TextType.IMAGE, "/test.jpg")
        self.assertEqual(node, node2)

        node = TextNode("Text 1", TextType.ITALIC)
        node2 = TextNode("Text 2", TextType.ITALIC)
        self.assertNotEqual(node, node2)

        node = TextNode("Text node", TextType.CODE)
        node2 = TextNode("Text node", TextType.LINK)
        self.assertNotEqual(node, node2)

        node = TextNode("Text node", TextType.IMAGE, "test1.jpg")
        node2 = TextNode("Text node", TextType.IMAGE, "test2.jpg")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()