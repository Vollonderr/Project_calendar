from models import get_events, get_workers, get_colors, update_colors
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = '/$_M2{w~^#iTX*C4>y{4AsUIO'

@app.route('/update_colors', methods=['POST'])
def get_colors_update():
	text = request.form['text']
	BG = request.form['BG']
	BGLOW = request.form['BGLOW']
	lines = request.form['lines']
	update_colors(text, BG, BGLOW, lines)
	flash("Стиль успешно обновлен!")
	return redirect("/")

@app.route('/')
def index():
	return render_template("Notes.html", **{"events": get_events(), "workers": get_workers(), "colors": get_colors()})

if __name__ == '__main__':
	app.run(debug=True)