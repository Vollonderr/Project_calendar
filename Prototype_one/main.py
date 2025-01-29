from models import get_events, add_event, update_event, delete_event

from datetime import datetime
from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'JH_2tg-LxpEiSMFq3f8Cyey_h'

@app.route('/add', methods=['POST'])
def get_event_add():
	name = request.form['name']
	start = request.form['start']
	end = request.form['end']
	supervisor = request.form['supervisor']
	note = request.form['note']
	importance = request.form['importance']
	status = request.form['status']

	if '' in [name, start, supervisor, note]:
		flash('Ошибка: заполнены не все поля!')
		return redirect("/")
	if end == '':
		add_event(name, start, '0', supervisor, note, importance, status)
		flash("Заметка \"" + name + "\" была успешна добавлена!")
		return redirect("/")
	if datetime.strptime(start, '%Y-%m-%d') > datetime.strptime(end, '%Y-%m-%d'):
		return 'Дата начала срока должна быть после даты конца срока!'
	add_event(name, start, end, supervisor, note, importance, status)
	flash("Мероприятие \"" + name + "\" было успешно добавлено!")
	return redirect("/")

@app.route('/update', methods=['POST'])
def get_event_update():
	name = request.form['name']
	realname = request.form['realname']
	start = request.form['start']
	end = request.form['end']
	supervisor = request.form['supervisor']
	note = request.form['note']
	importance = request.form['importance']
	status = request.form['status']
	ROWID = request.form['ROWID']

	if '' in [name, start, supervisor, note]:
		flash('Ошибка: заполнены не все поля!')
		return redirect("/")
	if end == '':
		update_event(name, start, '0', supervisor, note, importance, status, ROWID)
		flash("Мероприятие \"" + realname + "\" было успешно обновлено!")
		return redirect("/")
	if datetime.strptime(start, '%Y-%m-%d') > datetime.strptime(end, '%Y-%m-%d'):
		return 'Дата начала срока должна быть после даты конца срока!'
	update_event(name, start, end, supervisor, note, importance, status, ROWID)
	flash("Мероприятие \"" + realname + "\" было успешно обновлено!")
	return redirect("/")

@app.route('/delete', methods=['POST'])
def get_del():
	ROWID = request.form['ROWID']
	name = request.form['name']
	delete_event(ROWID)
	flash("Мероприятие \"" + name + "\" было успешно удалено!")
	return redirect("/")

@app.route('/')
def index():
	return render_template("Notes.html", **{"notes": get_events()})

if __name__ == '__main__':
	app.run(debug=True)