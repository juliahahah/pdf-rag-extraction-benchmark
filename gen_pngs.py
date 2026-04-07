import markdown
from html2image import Html2Image
import os

hti = Html2Image(custom_flags=['--no-sandbox', '--disable-gpu'], size=(600, 300))

# 1. LlamaParse
llama_md = """
|               | 100     | 80                 | 60 | 40 | 20 |
| ------------- | ------- | ------------------ | -- | -- | -- |
| GPT-4o        |         |                    |    |    |    |
| GPT-4-turbo   | (pass8) | drops to below 25% |    |    |    |
| Claude-3-opus |         |                    |    |    |    |
| GPT-3.5-turbo |         |                    |    |    |    |
"""

# 2. Docling 
docling_md = """
| Model | 100 | 80 | 60 | 40 | 20 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| GPT-4o | | | | | |
| GPT-4-turbo | (pass8) | drops to below 25% | | | |
| Claude-3-opus | | | | | |
| GPT-3.5-turbo | | | | | |
"""

# 3. Fitz (PyMuPDF - missing lines, spaces only)
fitz_txt = """
100 80 60 40 20
GPT-4o
GPT-4-turbo (pass8) drops to below 25%
Claude-3-opus
GPT-3.5-turbo
"""

html_template = """
<html>
<head>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; padding: 20px; font-size: 16px; background: #1e1e1e; color: #d4d4d4; white-space: pre-wrap; }}
        table {{ border-collapse: collapse; width: 100%; margin-top: 10px; margin-bottom: 10px; background: #252526; color: #d4d4d4; font-family: monospace; font-size: 14px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }}
        th, td {{ border: 1px solid #404040; padding: 12px; text-align: left; }}
        th {{ background-color: #333333; font-weight: bold; }}
    </style>
</head>
<body>
{}
</body>
</html>
"""

html_template_text = """
<html>
<head>
    <style>
        body {{ font-family: monospace; padding: 20px; font-size: 16px; background: #1e1e1e; color: #d4d4d4; white-space: pre-wrap; }}
    </style>
</head>
<body>
<pre>{}</pre>
</body>
</html>
"""

# Render Markdown to HTML and inject into template
llama_html = html_template.format(markdown.markdown(llama_md, extensions=['tables']))
docling_html = html_template.format(markdown.markdown(docling_md, extensions=['tables']))
fitz_html = html_template_text.format(fitz_txt)

hti.screenshot(html_str=llama_html, save_as='sample_llama.png')
hti.screenshot(html_str=docling_html, save_as='sample_docling.png')
hti.screenshot(html_str=fitz_html, save_as='sample_fitz.png')

print("Generated sample_llama.png, sample_docling.png, sample_fitz.png")
