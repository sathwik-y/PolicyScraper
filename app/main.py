from fastapi import FastAPI, HTTPException
from app.services.scraper import get_html_from_url
from app.services.converter import html_to_markdown
import app.services.llm_parser as llm
# from app.services.line_extractor import extract_lines_by_number
app = FastAPI()

@app.get("/scrape")
async def scrape_and_extract(url):
    try:
        html = get_html_from_url(url)
        markdown = html_to_markdown(html)
        
        with open("output.md", "w", encoding="utf-8") as file:
            file.write(markdown)
        
        line_numbers = llm.extract_line_numbers(markdown)
        print("\n--- LINE NUMBERS ---\n", line_numbers)
        
        # lines = extract_lines_by_number(markdown, line_numbers)
        # final_content = llm.extract_policy_content(lines)
        # print("source=", url, "extracted=", final_content)

    except Exception as e:
        import traceback
        print(f"Error in route handler: {e}")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))