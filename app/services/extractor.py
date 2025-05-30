def extract_content(markdown_text, line_ranges):
    """Extract the actual content from each line"""
    lines = markdown_text.split('\n')
    extracted_lines = []
    
    for line in line_ranges.split('\n'):
        if '-' in line:
            try:
                start, end = map(int, line.split('-'))
                start = start - 1
                end = end - 1
                
                if 0 <= start< len(lines) and 0 <= end < len(lines):
                    for i in range(start, end + 1):
                        line = lines[i]
                        if ':' in line and line.split(':', 1)[0].strip().isdigit():
                            cleaned_line = line.split(':', 1)[1]  
                        else:
                            cleaned_line = line
                        extracted_lines.append(cleaned_line)
            except ValueError:
                continue
    
    return '\n'.join(extracted_lines)