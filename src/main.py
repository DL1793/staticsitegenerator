from textnode import *
from generate_content import copy_static, recursive_copy
from extracttitle import extract_title
from generatepage import generate_pages_recursive

def main():

    copy_static('static', 'public')
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()