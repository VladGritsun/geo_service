from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)
app.secret_key = "geo_service"


@app.route('/')
def index():
	return render_template('homepage.html')

@app.route('/', methods=['POST'])
def location():
	location = request.form['location']
	print location
	# look up location
	return redirect('/') # pass on geojson

if __name__ == "__main__":
	app.run(debug=True)