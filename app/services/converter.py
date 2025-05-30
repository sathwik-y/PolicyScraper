from markdownify import markdownify as md

def html_to_markdown(html: str) -> str:
    """Convert HTML to markdown with line numbers for easier reference."""
    markdown = md(html)
    numbered_lines = []
    for i, line in enumerate(markdown.split('\n'), 1):
        numbered_lines.append(f"{i}: {line}")
    numbered_markdown = '\n'.join(numbered_lines)
    
    return numbered_markdown
