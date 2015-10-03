from flask import Flask
from flask import render_template

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
	return 'Index Page'

@app.route("/hello")
@app.route("/hello/<name>")
def hello(name = None):
	return render_template('hello.html', name=name)
	
@app.route('/map')
@app.route("/map/<lat>/<long>/<zoom>")
def map(lat=None, long=None, zoom=None):
	return render_template('map.html', lat=lat, long=long, zoom=zoom)


@app.route('/plot')
def plotIndex():
	pass # show list of datasets available

@app.route('/plot/<file>/<render>')
def plot(file, render=False):
	file = get_file(file, render):
	return render_template('plot.html', file)

	
if __name__ == "__main__":
	app.run()