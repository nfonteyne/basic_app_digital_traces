from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello_world():
    prefix_google = """
    <!-- Google tag (gtag.js) -->
<script async 
src="https://www.googletagmanager.com/gtag/js?id=UA-250924533-1"></script> 
<script>
 window.dataLayer = window.dataLayer || []; 
 function gtag(){dataLayer.push(arguments);} 
 gtag('js', new Date());
 
 gtag('config', 'UA-250924533-1'); 
</script>
"""
    return prefix_google + "Hello World"

@app.route('/logger', methods=["GET"])
def log():
    todisplay = render_template("main.html")
    todisplay+=f"<div class='card'>\n<h1> logger </h1>\n</div>\n"
    script = """
    <script> console.log("logger") </script>"""
    req = requests.get("https://analytics.google.com/analytics/web/#/report-home/a250924533w344992688p281198723")
    return todisplay + script + str(req.text)
