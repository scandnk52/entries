import re
from slugify import slugify

def content_lowercase(content: str) -> str:
    return content.lower()

def clean_empty_lines(text: str) -> str:
    # Converts multiple empty lines into a single newline to prevent excessive spacing.
    return re.sub(r'\n\s*\n+', '\n\n', text)

def normalize_paragraphs(text: str) -> str:
    # Converts single newlines into HTML line breaks (<br>).
    return re.sub(r'\n', '<br>', text)

def convert_links(text: str) -> str:
    # Converts link syntax `[[http://example.com|link text]]` to an HTML anchor tag.
    return re.sub(r'\[\[(https?://\S+)\|(.+?)]]', r'<a href="\1" target="_blank">\2</a>', text)

def convert_spoilers(text: str) -> str:
        # Converts spoiler syntax `[[spoiler:text]]` to a clickable <span> element.
    return re.sub(r'\[\[spoiler:(.+?)]]', r'<span>\1</span>', text)

def render_entry_content(content: str) -> str:
    text = content
    text = clean_empty_lines(text)
    text = normalize_paragraphs(text)
    text = convert_links(text)
    text = convert_spoilers(text)
    return text

def create_title(title: str) -> str:
    return title.lower()

def create_slug(title: str) -> str:
    return slugify(create_title(title))