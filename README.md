# Jinja Resume Template

This project contains a simple example on how to build a resume with Python using Jinja, HTML, Bootstrap and a data file. In the past I have always created my resume with Latex, but to make life a little easier I chose to switch to a combination of Python and HTML. Maintaining a Latex document is cumbersome and it is difficult to divide the data from the style. By using Jinja it is straightforward to separate the resume data from the actual layout. And the most important part, I can stick to Python!

## Library overview
- [flask](https://palletsprojects.com/p/flask/) - Application to render the Jinja templates with.
- [jinja](https://palletsprojects.com/p/jinja/) - Library to create templates and populate fields with Python variables.
- [pdfkit](https://pypi.org/project/pdfkit/) - Tool to write HTML to PDF with Python.
- [pyyaml](https://pypi.org/project/PyYAML/) - Library to read and write Yaml files with Python.

## Getting started

Clone this repository and navigate inside the folder.

```bash
~/code/ $ git clone https://github.com/jitsejan/jinja-resume-template.git
~/code/ $ cd jinja-resume-template
```

Create the virtual environment with [pipenv](https://pipenv.kennethreitz.org/en/latest/) to run the project in.

```bash
~/code/jinja-resume-template $ pipenv shell
Creating a virtualenv for this project…
Pipfile: /Users/jitsejan/code/jinja-resume-template/Pipfile
Using /Library/Frameworks/Python.framework/Versions/3.7/bin/python3 (3.7.4) to create virtualenv…
⠇ Creating virtual environment...Already using interpreter /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
Using base prefix '/Library/Frameworks/Python.framework/Versions/3.7'
New python executable in /Users/jitsejan/.local/share/virtualenvs/jinja-resume-template-97zV94Wt/bin/python3
Also creating executable in /Users/jitsejan/.local/share/virtualenvs/jinja-resume-template-97zV94Wt/bin/python
Installing setuptools, pip, wheel...
done.
Running virtualenv with interpreter /Library/Frameworks/Python.framework/Versions/3.7/bin/python3

✔ Successfully created virtual environment!
Virtualenv location: /Users/jitsejan/.local/share/virtualenvs/jinja-resume-template-97zV94Wt
Launching subshell in virtual environment…
 . /Users/jitsejan/.local/share/virtualenvs/jinja-resume-template-97zV94Wt/bin/activate
```

Install the dependencies:

```bash
jinja-resume-template-97zV94Wt ~/code/jinja-resume-template $ pipenv install
Pipfile.lock not found, creating…
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
✔ Success!
Updated Pipfile.lock (546278)!
Installing dependencies from Pipfile.lock (546278)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 8/8 — 00:00:10
```

## Creating the PDF

Execute the script `run.py` to generate the PDF:

```bash
jinja-resume-template-97zV94Wt ~/code/jinja-resume-template $ pipenv run python run.py
Loading pages (1/6)
Counting pages (2/6)
Resolving links (4/6)
Loading headers and footers (5/6)
Printing pages (6/6)
Done
```

## Information

Jinja helps to create structures like this:

```html
<header>
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

The following Python script will load the YAML and the HTML and save the populated template to `output_text`.

```python
def _get_data():
    """ Load the data from the YAML file """
    with open(DATA_FILE, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

def _get_template():
  	""" Retrieve the template """
    template_loader = jinja2.FileSystemLoader(searchpath="templates")
    template_env = jinja2.Environment(loader=template_loader)
    return template_env.get_template(TEMPLATE_FILE)

# Loads YAML file
data = _get_data()
# Loads HTML file
template = _get_template()
# Fills in the variables in the HTML file
output_text = template.render(**data)
```

### Jinja for-loop

With Jinja it is also easy to loop through lists and dictionaries. Below I have defined the `languages` variable with two elements where each element has a `description`. 

```yaml
languages:
  English:
    description: Full professional proficiency
  Italian:
    description: Elementary proficiency
```

In the HTML we use `{%` and `%}` to indicate Python code is executed. 

```html
<ul>
{% for dict_item in languages %}
    <li>{{dict_item}}: {{ languages[dict_item]['description'] }}</li>  
{% endfor %}  
</ul>
```

In the above case I use it for a `for`-loop, but the same syntax is used for conditionals too. For example, you could write a condition like the following:

```html
{% if social.get('github') not None %}
	<div class="social">{{ social.get('github') }}</div>
{% endif %}
```

For further Jinja tricks, take a look at their [documentation](https://jinja.palletsprojects.com/en/2.10.x/). Take a look at my [Github repo](https://github.com/jitsejan/jinja-resume-template) for the code, clone it and play with the template.