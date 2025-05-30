import os
import anthropic 
from dotenv import load_dotenv

load_dotenv()
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")

client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)

def extract_line_numbers(markdown_text):
    """Extract the line numbers from the markdown"""
    try:
        # prompt = f"""
        # You are tasked with extracting line numbers of a given markdown content. 
        # The markdown content is converted from html page. 
        # The purpose of the extraction is to include only necessary to upload to the
        # knowledge base of the company and omitting irrelevant information for the purpose 
        # of the page
        # {markdown_text}
        # """
        prompt = f"""
        You are tasked with identifying useful content from markdown converted from HTML.
        Return ONLY line number ranges in this exact format, one per line:
        START-END
        START-END
        
        For single lines, use: LINE-LINE
        
        Example output:
        1-5
        12-18
        25-25
        
        Markdown content:
        {markdown_text}
        """
        response = client.messages.create(
                model="claude-sonnet-4-20250514", 
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

    
