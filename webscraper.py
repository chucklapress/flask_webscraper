from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests


source = requests.get('http://www.wherethetruck.is').text
soup = BeautifulSoup(source,'lxml')
big_news = soup.find('h1').text
highlight = soup.find('h3').text


app = Flask(__name__)
@app.route('/')
def index():
    big_news = soup.find('h1').text
    highlight = soup.find('h2').text
    return render_template('index.html',**locals())

if __name__ == '__main__':
    app.run(host='0.0.0.0')
