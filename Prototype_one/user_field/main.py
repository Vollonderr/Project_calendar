from models import get_events, get_workers
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("Notes.html", **{"events": get_events(), "workers": get_workers()})

if __name__ == '__main__':
	app.run(debug=True)