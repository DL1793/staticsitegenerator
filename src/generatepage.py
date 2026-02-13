from markdowntoblock import markdown_to_html_node
from extracttitle import extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = None
    template = None
    html = ""
    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as f:
        template = f.read()
    nodes = markdown_to_html_node(markdown)
    html = "".join([node.to_html() for node in nodes.children])
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)
    print(dest_path)
    with open(dest_path, "w") as f:
        f.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for path in os.listdir(dir_path_content):
        source_path = os.path.join(dir_path_content, path)
        dest_path = os.path.join(dest_dir_path, path)
        file_root, file_ext = os.path.splitext(dest_path)
        if file_ext == ".md":
            dest_path = file_root + ".html"
        if os.path.isfile(source_path):
            print(dest_path)
            generate_page(source_path, template_path, dest_path)
        elif os.path.isdir(source_path):
            generate_pages_recursive(source_path, template_path, dest_path)