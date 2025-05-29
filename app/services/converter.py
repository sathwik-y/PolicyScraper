from markdownify import markdownify as md

def html_to_markdown(html: str) -> str:
    markdown = md(html)
    return markdown
