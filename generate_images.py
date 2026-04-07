import fitz
from docling.document_converter import DocumentConverter
import markdown
from html2image import Html2Image
import os

pdf_path = "Benchmarking_Collaborative_AI_Agents.pdf"
doc = fitz.open(pdf_path)

# Find page with "LM-Simulated User"
page_num = 0
for i in range(len(doc)):
    text = doc[i].get_text()
    if "LM-Simulated User" in text or "Single-Control" in text or "Dual-Control" in text:
        page_num = i
        break

print(f"Using page {page_num}")

# 1. Capture original PDF page as image
page = doc[page_num]
pix = page.get_pixmap(dpi=150)
pix.save("sample_pdf.png")

# 2. PyMuPDF output
fitz_text = page.get_text()
print("PyMuPDF text length:", len(fitz_text))

# 3. Docling output
converter = DocumentConverter()
result = converter.convert(pdf_path)
docling_text = result.document.export_to_markdown()
print("Docling text length:", len(docling_text))

# For Docling, we also want to extract just the chunk related to the page. 
# But for simplicity, we can just extract a substring that matches what we found, or we can just render a representative table.
# Actually, the user wants to see the visual diff for the table. Let's find the section with "Single-Control" or "LM-Simulated User" and extract ~500 chars around it.

def extract_snippet(text, keyword):
    idx = text.find(keyword)
    if idx == -1: return "Keyword not found\n\n" + text[:200]
    start = max(0, idx - 100)
    end = min(len(text), idx + 500)
    return text[start:end]

keyword_to_find = "Single-Control" if "Single-Control" in docling_text else "LM-Simulated User"
if keyword_to_find not in docling_text:
    keyword_to_find = "Dual-Control"

# 4. LlamaParse output (load from the existing parsed markdown)
with open("Benchmarking_Collaborative_AI_Agents_parsed.md", "r", encoding="utf-8") as f:
    llama_text = f.read()

fitz_snippet = extract_snippet(fitz_text, keyword_to_find)
docling_snippet = extract_snippet(docling_text, keyword_to_find)
llama_snippet = extract_snippet(llama_text, keyword_to_find)

print("Fitz:", fitz_snippet[:50])
print("Docling:", docling_snippet[:50])
print("Llama:", llama_snippet[:50])

# HTML Template
html_template = """
<html>
<head>
    <style>
        body { font-family: sans-serif; padding: 20px; font-size: 14px; background: white; white-space: pre-wrap; }
        table { border-collapse: collapse; width: 100%; margin-top: 10px; margin-bottom: 10px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
{}
</body>
</html>
"""

hti = Html2Image(size=(800, 600))
# PyMuPDF is raw text, so we put it in <pre>
hti.screenshot(html_str=f"<html><body style='font-family:monospace; background:white; padding:20px;'><pre>{fitz_snippet}</pre></body></html>", save_as='sample_fitz.png')

# Docling and Llama are markdown
hti.screenshot(html_str=html_template.format(markdown.markdown(docling_snippet, extensions=['tables'])), save_as='sample_docling.png')
hti.screenshot(html_str=html_template.format(markdown.markdown(llama_snippet, extensions=['tables'])), save_as='sample_llama.png')

print("Generated sample_pdf.png, sample_fitz.png, sample_docling.png, sample_llama.png")
