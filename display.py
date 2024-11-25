def render_tree(element, prefix=""):
    """Renders HTML tree in a tree-like format."""
    lines = [f"{prefix}{element.tag}#{element.id if element.id else ''}"]
    for child in element.children:
        lines.extend(render_tree(child, prefix + "  "))
    return lines


def render_indented(element, indent=2, level=0):
    """Renders HTML tree in an indented format."""
    space = " " * (level * indent)
    result = f"{space}<{element.tag} id='{element.id}'>"
    if element.text_content:
        result += f"{element.text_content}"
    for child in element.children:
        result += "\n" + render_indented(child, indent, level + 1)
    result += f"\n{space}</{element.tag}>"
    return result
