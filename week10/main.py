from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

print(HTMLResponse)

#############################################################
## Step 1: Return Basic HTML Over an API Endpoint
#############################################################
@app.get("/", response_class=HTMLResponse)
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Home</title>
    </head>
    <body>
        <h1>Welcome to FastAPI!</h1>
    </body>
    </html>
    """
    return html_content
#############################################################
# Step 2: Level Up Your FastAPI App With Jinja2 Templates
#############################################################
import random
from string import hexdigits
from jinja2 import Template

@app.get("/colors", response_class=HTMLResponse)
def home():
    hex_chars = "".join(random.choices(hexdigits.lower(), k=6))
    hex_color = f"#{hex_chars}"
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Random Color Generator</title>
        <style>
            body {
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background-color: {{ color }};
                color: white;
                font-size: 120px;
                font-family: monospace;
            }
        </style>
    </head>
    <body>
        <div id="color-code">{{ color }}</div>
    </body>
    </html>
    """

    html_content = Template(html_template)
    website = html_content.render(color=hex_color)

    return website

##############################################################
# Step 3: Serve Static Files in FastAPI
##############################################################
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/jinja", response_class=HTMLResponse)
def home(request: Request):
    hex_chars = "".join(random.choices(hexdigits.lower(), k=6))
    hex_color = f"#{hex_chars}"
    context = {
        "color": hex_color,
    }
    return templates.TemplateResponse(
        request=request, name="color.html", 
        context=context
    )