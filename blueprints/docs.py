from flask import Blueprint
import markdown
import os

app = Blueprint('docs', 'docs', url_prefix="/docs")

@app.route('/')
def _():
    return 'Base Docs endpoint<br>' + ' '.join([f"<a href='{x}'>{x}</a>" for x in os.listdir('docs')])

@app.route('/<doc>')
def __(doc):
    try:
        with open(f'docs/{doc}') as _z: doc = markdown.markdown(_z.read())
        return str(doc) + '<br>' + 'Available Docs <br>' + ' '.join([f"<a href='{x}'>{x}</a>" for x in os.listdir('docs')])
    except:
        return 'Document could not be opened'
