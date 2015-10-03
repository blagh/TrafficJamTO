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
	
@app.route("/map")
def map(center, zoom)
	return render_tempalte('map.html', center=center, zoom=zoom)
	
if __name__ == "__main__":
	app.run()