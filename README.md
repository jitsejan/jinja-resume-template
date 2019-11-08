# Jinja Resume Template

This project contains a simple example on how to build a resume with Python, using Jinja, HTML, Bootstrap and a configuration file. 

## Library overview
- flask - Application to execute the Jinja templates with
- jinja - Library to create templates and populate fields with Python variables
- pdfkit - Tool to write HTML to PDF with Python
- pyyaml - Library to read and write Yaml files with Python

## Getting started

Create the virtual environment to run the project in.

```bash
$ pipenv shell
```

## Creating the PDF

Run the script `run.py` to generate the PDF:

```bash
$ python run.py
```

## Information

Jinja helps to create structures like this:

```html
<header class="col-12">
    <h1>{{ personal.get('name').get('first') }} {{ personal.get('name').get('last') }}</h1>
    <h2>{{ occupation }}</h2>
</header>
```

Everything between `{{` and `}}` is interpreted as Python. The input of the template is a dictionary with the keys `personal` and `occupation`, which are all defined in `data.yml`. All the variables defined in the YAML file can be used in the template. 

```yaml
personal:
  name: 
    first: Pete
    last: Peterson
occupation: Resume builder
```

```python
data = _get_data() # Loads YAML file
template = _get_template() # Loads HTML file
output_text = template.render(**data) # Fills in the variables in the HTML file
```

