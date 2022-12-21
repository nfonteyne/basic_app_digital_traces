from flask import Flask,render_template

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
    todisplay = render_template("film_all.html")
    todisplay+=f"<div class='card'>\n<h1> logger</h1>\n</div>\n"
    script = """
    <script> console.log("logger") </script>"""
    return "I'm a logger" + script

    