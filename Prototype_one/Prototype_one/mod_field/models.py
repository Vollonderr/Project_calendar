import sqlite3

def get_events():
	res = []
	con = sqlite3.connect("Instance\Events.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM Events")
	rows = cur.fetchall()
	for i in rows:
		res.append(list(i))
	con.commit()
	con.close()
	return res

def get_workers():
	res = []
	con = sqlite3.connect("Instance\Workers.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM Workers")
	rows = cur.fetchall()
	for i in rows:
		res.append(list(i))
	con.commit()
	con.close()
	return res

def get_colors():
	res = []
	con = sqlite3.connect("mod_field\instance\Colors.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM Colors")
	rows = cur.fetchall()
	for i in rows:
		res.append(list(i))
	con.commit()
	con.close()
	return res

def add_event(name, start, end, supervisor, note, importance, status):
	con = sqlite3.connect('Instance\Events.db')
	cur = con.cursor()
	cur.execute('INSERT INTO events (Name, Start, End, Supervisor, Note, Importance, Status) VALUES (?, ?, ?, ?, ?, ?, ?)', (name, start, end, supervisor, note, importance, status))
	cur.execute('UPDATE events SET ID = ? WHERE ROWID = ?', (str(cur.lastrowid), str(cur.lastrowid)))
	con.commit()
	con.close()

def update_event(name, start, end, supervisor, note, importance, status, ROWID):
	con = sqlite3.connect('Instance\Events.db')
	cur = con.cursor()
	cur.execute('UPDATE events SET name = ?, start = ?, end = ?, supervisor = ?, note = ?, Importance = ?, Status = ?, ID = ? WHERE ROWID = ?', (name, start, end, supervisor, note, importance, status, ROWID, ROWID))
	con.commit()
	con.close()

def update_colors(text, BG, BGLOW, lines):
	con = sqlite3.connect('mod_field\instance\Colors.db')
	cur = con.cursor()
	cur.execute('UPDATE colors SET text = ?, BG = ?, BGLOW = ?, lines = ? WHERE ROWID = ?', (text, BG, BGLOW, lines, 1))
	con.commit()
	con.close()

def delete_event(ROWID):
	con = sqlite3.connect('Instance\Events.db')
	cur = con.cursor()
	cur.execute('DELETE FROM events WHERE ROWID = ?', (ROWID, ))
	con.commit()
	con.close()