from flask import Flask
from flask import render_template

myapp_obj = Flask(__name__)

name = 'Lisa'
city_names = ['Paris', 'London', 'Rome', 'Tahiti']

@myapp_obj.route('/')
def home():
    #name = 'Lisa'
    #city_names = ['Paris', 'London', 'Rome', 'Tahiti']
    output = """
    <html>
    <head>
        <h1>Welcome """ + name + """!</h1>
    </head>
    <body>
        <a href="www.google.com">not google</a>
        <ul>"""
    for city in city_names:
        output += f"<li>{city}</li>\n"
    output += """
        </ul>
    </body>
    </html>
    """

    return output
