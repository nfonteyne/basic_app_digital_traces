from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from decouple import config

app = Flask(__name__)

class SessionGoogle:
    def __init__(self, url_login, url_auth, login, pwd):
        self.ses = requests.session()
        login_html = self.ses.get(url_login)
        soup_login = BeautifulSoup(login_html.content).find('form').find_all('input')
        my_dict = {}
        for u in soup_login:
            if u.has_attr('value'):
                my_dict[u['name']] = u['value']
        # override the inputs without login and pwd:
        my_dict['Email'] = login
        my_dict['Passwd'] = pwd
        self.ses.post(url_auth, data=my_dict)

    def get(self, URL):
        return self.ses.get(URL).text

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
    <script>
var n = localStorage.getItem('on_load_counter');

if (n === null) {
  n = 0;
}
n++;

localStorage.setItem("on_load_counter", n);

nums = n.toString().split('').map(Number);
document.getElementById('CounterVisitor').innerHTML = '';
for (var i of nums) {
  document.getElementById('CounterVisitor').innerHTML += '<span class="counter-item">' + i + '</span>';
}

</script>"""
    url_login = "https://accounts.google.com/ServiceLogin"
    payload = {'us':config('login'),'pwd':config('pwd')}
    url_auth = "https://accounts.google.com/ServiceLoginAuth"
    r = requests.post(url_auth,  data=payload)
    req = requests.get("https://analytics.google.com/analytics/web/#/report-home/a250924533w344992688p281198723", cookies = r.cookies)
    return todisplay + script + str(req.text)

if __name__ == "__main__":
    app.run()