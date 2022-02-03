import requests as rq
import collections
import os
import pygal
from pygal.style import Style
from flask import Flask, request, send_file

app = Flask('__name__')
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
target = os.path.join(APP_ROOT,'static/images/')

# custom_stle = Style(colors=('#FFD43B', '#FFBF00', '#E95355', '#306998', '#DE3163'))

def GetLaguages_of_user(username):
    url = f"https://api.github.com/users/{username}/repos?per_page=100&page=1"
    data = rq.get(url).json()
    languages = [i['language'] for i in data]
    counter = collections.Counter(languages)
    lang = ["Other" if i is None else i for i in counter.keys()]
    data = list(int(i) for i in counter.values())
    return lang,data

# http://localhost:5000/api/gituser/language/showPieChart/?username=suriya4code
@app.route("/api/gituser/language/showPieChart/",methods=["GET"])
def draw_PieChart():
    username = request.args.get("username")
    lang, data = GetLaguages_of_user(username)
    pie_chart = pygal.Pie()
    # pie_chart = pygal.Pie(style=custom_stle)
    for i,j in zip(lang,data):
        pie_chart.add(i,j)
    return pie_chart.render_response(title=f"{username}'s languages")

# http://localhost:5000/api/gituser/language/showHalfPieChart/?username=suriya4code
@app.route("/api/gituser/language/showHalfPieChart/",methods=["GET"])
def draw_HalfPieChart():
    username = request.args.get("username")
    lang, data = GetLaguages_of_user(username)
    pie_chart = pygal.Pie(half_pie=True)
    for i,j in zip(lang,data):
        pie_chart.add(i,j)
    return pie_chart.render_response(title=f"{username}'s languages")


if __name__ == '__main__':
#     uvicorn.run(app)
    app.run(debug = True)
