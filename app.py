from flask import Flask
from flask import render_template

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
	return 'Index Page'

@app.route('/plot')
def plotIndex():
	pass # show list of datasets available

@app.route('/plot/<file>/<render>')
def plot(file, render=False):
	file = get_file(file, render):
	return render_template('plot.html', file)

	
if __name__ == "__main__":
	app.run()