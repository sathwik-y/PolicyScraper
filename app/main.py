from fastapi import FastAPI, HTTPException
from app.services.scraper import get_html_from_url
from app.services.converter import html_to_markdown
import app.services.llm_service as llm
import app.services.extractor as extractor

app = FastAPI()

@app.get("/scrape")
async def scrape_and_extract(url):
    try:
        html = get_html_from_url(url)
        markdown = html_to_markdown(html)
        
        with open("output.md", "w", encoding="utf-8") as file:
            file.write(markdown)
        
        line_numbers = llm.extract_line_numbers(markdown)
        print(f"Line Numbers: {line_numbers}")
        
        lines = extractor.extract_content(markdown, line_numbers)
        print(f"Extracted {len(lines)} characters")
        result = {
            "source": url,
            "line_numbers": line_numbers,
            "extracted_content": lines,
            "content_length": len(lines),
            "status": "success"
        }
        print(f"----Parsed & Converted the url: {url}------")
        return result

    except Exception as e:
        import traceback
        print(f"Error in route handler: {e}")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))