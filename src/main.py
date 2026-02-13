from textnode import *
from generate_content import copy_static, recursive_copy
from extracttitle import extract_title
from generatepage import generate_pages_recursive
import sys

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    copy_static('static', 'docs')
    generate_pages_recursive("content", "template.html", "docs", basepath)

if __name__ == "__main__":
    main()