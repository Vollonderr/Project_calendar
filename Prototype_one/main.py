from models import get_events, add_event, update_event, delete_event

from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

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
		return 'Заполнены не все поля!'
	if end == '':
		add_event(name, start, '0', supervisor, note, importance, status)
		return 'Однодневное мероприятие добавлено'
	if datetime.strptime(start, '%Y-%m-%d') > datetime.strptime(end, '%Y-%m-%d'):
		return 'Дата начала срока должна быть после даты конца срока!'
	add_event(name, start, end, supervisor, note, importance, status)
	return 'Многодневное мероприятие добавлено'

@app.route('/update', methods=['POST'])
def get_event_update():
	name = request.form['name']
	start = request.form['start']
	end = request.form['end']
	supervisor = request.form['supervisor']
	note = request.form['note']
	importance = request.form['importance']
	status = request.form['status']
	ROWID = request.form['ROWID']

	print(start, end)
	if '' in [name, start, supervisor, note]:
		return 'Заполнены не все поля!'
	if end == '':
		update_event(name, start, '0', supervisor, note, importance, status, ROWID)
		return 'Однодневное мероприятие обновлено'
	if datetime.strptime(start, '%Y-%m-%d') > datetime.strptime(end, '%Y-%m-%d'):
		return 'Дата начала срока должна быть после даты конца срока!'
	update_event(name, start, end, supervisor, note, importance, status, ROWID)
	return 'Многодневное мероприятие обновлено'

@app.route('/delete', methods=['POST'])
def get_del():
	ROWID = request.form['ROWID']
	delete_event(ROWID)
	return 'Мероприятие удалено'

@app.route('/')
def index():
	return render_template("Notes.html", **{"notes": get_events()})

if __name__ == '__main__':
	app.run(debug=True)