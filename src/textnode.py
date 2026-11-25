from enum import Enum

class TextType(Enum):
    PLAIN_TEXT = "plain"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"


class TextNode:
    def __init__(self, text:str, text_type:TextType, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, compare_textnode):
        if self.text == compare_textnode.text:
            if self.text_type == compare_textnode.text_type:
                if self.url == compare_textnode.url:
                    return True
        return False

    def __repr__(self):
        return(f"TextNode({self.text}, {self.text_type}, {self.url})")
