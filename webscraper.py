from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
import datetime



source = requests.get('http://lunarosa.herokuapp.com')
soup = BeautifulSoup(source.text, 'html.parser')
rows = soup.find_all('h2')
# removed print statement in terminal as not needed
#for row in rows:
#    print(row.get_text())

app = Flask(__name__)
@app.route('/')


def index():
    now = datetime.datetime.now()
    date = now.strftime("%m-%d-%Y")
    rows = soup.find_all('h2')
    for row in rows:
        row.get_text()
    return render_template('index.html',**locals())

if __name__ == '__main__':
    app.run(host='0.0.0.0')
