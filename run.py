from flask import render_template
import json
import yaml
import pdfkit
import jinja2

TEMPLATE_FILE = "cv_en.html"
DATA_FILE = "data/data.yml"
OUTPUT_HTML = "output/output.html"
OUTPUT_PATH = "output/output.pdf"

def _get_data():
    with open(DATA_FILE, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

def _get_template():
    template_loader = jinja2.FileSystemLoader(searchpath="templates")
    template_env = jinja2.Environment(loader=template_loader)
    return template_env.get_template(TEMPLATE_FILE)

def _generate_html_output():
    data = _get_data()
    template = _get_template()
    output_text = template.render(**data)
    with open(OUTPUT_HTML, 'w') as ofile:
        ofile.write(output_text)

def generate_pdf_output():
    _generate_html_output()
    options = {
        'dpi': 500,
        'page-size': 'A4',
        'margin-top': '0.25in',
        'margin-right': '0.25in',
        'margin-bottom': '0.25in',
        'margin-left': '0.25in',
        'encoding': "UTF-8",
        'custom-header' : [
            ('Accept-Encoding', 'gzip')
        ],
        'no-outline': None,
    }
    pdfkit.from_file(input=OUTPUT_HTML,
                     output_path=OUTPUT_PATH, 
                     options=options)

def main():
    generate_pdf_output()


if __name__ == "__main__":
    main()
