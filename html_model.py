class HTMLElement:
    """Represents an HTML element."""
    def __init__(self, tag, element_id=None, text_content=""):
        self.tag = tag
        self.id = element_id if element_id else tag
        self.text_content = text_content
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def to_dict(self):
        return {
            "tag": self.tag,
            "id": self.id,
            "text": self.text_content,
            "children": [child.to_dict() for child in self.children]
        }

    def __repr__(self):
        return f"<{self.tag} id='{self.id}'>: {self.text_content}"


class HTMLModel:
    """Manages the HTML object model."""
    def __init__(self):
        self.root = HTMLElement("html")
        self.head = HTMLElement("head")
        self.title = HTMLElement("title")
        self.body = HTMLElement("body")
        self.root.add_child(self.head)
        self.head.add_child(self.title)
        self.root.add_child(self.body)
        self.id_map = {"html": self.root, "head": self.head, "title": self.title, "body": self.body}

    def add_element(self, tag, element_id, parent_id, text_content=""):
        if element_id in self.id_map:
            raise ValueError(f"ID '{element_id}' already exists.")
        parent = self.id_map.get(parent_id)
        if not parent:
            raise ValueError(f"Parent ID '{parent_id}' not found.")
        new_element = HTMLElement(tag, element_id, text_content)
        parent.add_child(new_element)
        self.id_map[element_id] = new_element

    def delete_element(self, element_id):
        element = self.id_map.pop(element_id, None)
        if not element or not element.parent:
            raise ValueError(f"Element ID '{element_id}' not found or is a root element.")
        element.parent.remove_child(element)

    def edit_text(self, element_id, new_text):
        element = self.id_map.get(element_id)
        if not element:
            raise ValueError(f"Element ID '{element_id}' not found.")
        element.text_content = new_text

    def edit_id(self, old_id, new_id):
        if new_id in self.id_map:
            raise ValueError(f"New ID '{new_id}' already exists.")
        element = self.id_map.pop(old_id, None)
        if not element:
            raise ValueError(f"Element ID '{old_id}' not found.")
        element.id = new_id
        self.id_map[new_id] = element
