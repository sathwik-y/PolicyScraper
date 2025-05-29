import os
import anthropic 
from dotenv import load_dotenv

load_dotenv()
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")

client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)

def extract_line_numbers(markdown_text):
    try:
        prompt = f"""
        This is a markdown file of a Return Policy. 
        {markdown_text}
        Carefully review the entire markdown and return me the line numbers from the start of the
        "Return Policy" heading. Include all the content from that line in your search and discard where the content ends
        """
        response = client.messages.create(
                model="claude-3-5-sonnet-20241022", 
                max_tokens=4000,
                messages=[
                    {
                        "role": "user", 
                        "content": prompt
                    }
                ]
            )
        return response.content[0].text
    except Exception as e:
        return f"Error: {str(e)}"
