from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, send_from_directory
from datarender import get_data

DATABASE = '/tmp/trafficjamto.db'
DEBUG = True
GOOGLE_API_KEY = 'AIzaSyBtUhdT_gnCH1rsmc54NFm_nK4uscIqhOg'
TOMTOM_API_KEY = 'toronto_trafficjam'

LOCAL_ROOT = 'http://127.0.0.1:5000/'
GITHUB_ROOT = 'https://raw.githubusercontent.com/blagh/TrafficJamTO/master/'

# These are the "Tableau 20" colors as RGB.
TABLEAU20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
for i in range(len(TABLEAU20)):
    r, g, b = TABLEAU20[i]
    TABLEAU20[i] = (r / 255., g / 255., b / 255.)

app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/plot")
@app.route("/plot/<render>")
def plot(render=False):
	data = get_data(file, render)
	return render_template(
		'plot.html', title="HOV lanes & Pan Am Games",
		maps=data['maps'], api_key=GOOGLE_API_KEY,
		github_root=GITHUB_ROOT
	)

@app.route("/datasets/<file>")
def datasets(file):
	return send_from_directory("./datasets/", file)

if __name__ == "__main__":
	app.run()