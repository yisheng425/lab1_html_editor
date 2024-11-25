from html.parser import HTMLParser
from html_model import HTMLElement, HTMLModel
from display import render_indented

class HTMLFileParser(HTMLParser):
    """
    Custom HTML parser to convert an HTML file into an HTMLModel.
    """
    def __init__(self):
        super().__init__()
        self.model = HTMLModel()
        self.current_element = None
        self.element_stack = []

    def handle_starttag(self, tag, attrs):
        element_id = None
        for attr_name, attr_value in attrs:
            if attr_name == "id":
                element_id = attr_value
        
        # Create new HTMLElement
        new_element = HTMLElement(tag, element_id)
        
        if self.element_stack:
            parent = self.element_stack[-1]
            parent.add_child(new_element)
        else:
            # Handle root elements directly
            if tag == "html":
                self.model.root = new_element
            elif tag == "head":
                self.model.head = new_element
                self.model.root.add_child(new_element)
            elif tag == "body":
                self.model.body = new_element
                self.model.root.add_child(new_element)
        
        # Map the ID
        if element_id:
            self.model.id_map[element_id] = new_element

        # Push to stack
        self.element_stack.append(new_element)

    def handle_endtag(self, tag):
        if self.element_stack and self.element_stack[-1].tag == tag:
            self.element_stack.pop()

    def handle_data(self, data):
        if self.element_stack:
            self.element_stack[-1].text_content += data.strip()

def read_html_file(filepath):
    """
    Reads an HTML file and parses it into an HTMLModel.
    
    Args:
        filepath (str): Path to the HTML file.
    
    Returns:
        HTMLModel: The constructed HTMLModel object.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        parser = HTMLFileParser()
        parser.feed(content)
        return parser.model
    except FileNotFoundError:
        raise ValueError(f"File not found: {filepath}")
    except Exception as e:
        raise ValueError(f"Error reading file '{filepath}': {e}")

def write_html_file(filepath, model):
    """
    Writes the current HTMLModel to an HTML file in indented format.
    
    Args:
        filepath (str): Path to save the HTML file.
        model (HTMLModel): The HTML model to write.
    """
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(render_indented(model.root))
        print(f"HTML saved to {filepath}")
    except Exception as e:
        raise ValueError(f"Error writing file '{filepath}': {e}")
